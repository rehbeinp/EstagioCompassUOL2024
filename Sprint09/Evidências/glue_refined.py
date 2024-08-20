import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as Func
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, IntegerType
import pandas as pd
from datetime import date
from pyspark.sql.functions import col, lit, monotonically_increasing_id


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH', 'S3_TARGET_PATH'])
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


data_hoje = (f"PARQUET/{date.today().year}/0{date.today().month}/{date.today().day}")
                 
#caminho parquet, lendo df spark
df = spark.read.parquet(source_file)


# adiconando id para cada artista

# selecionando o nome dos artistas 
dataframe_nomes_art = df.dropDuplicates(["nomeArtista"]).select("nomeArtista")
dataframe_nomes_art = dataframe_nomes_art.withColumnRenamed("nomeArtista", "nome")

# adicionando ids aos nomes dos artistas
dataframe_nomes_art = dataframe_nomes_art.withColumn("idArtista", monotonically_increasing_id())

# join no data frame base, adicionando o idArtista
df1 = df.join(dataframe_nomes_art, df.nomeArtista == dataframe_nomes_art.nome, 'inner').select(df.idFilme, df.tituloPrincipal, df.anoLancamento, df.generoFilme, df.notaMedia, df.generoArtista, dataframe_nomes_art.idArtista, df.nomeArtista, df.anoNascimento)

# tornando as colunas inteiras
df2 = df1.withColumn("anoLancamento", col("anoLancamento").cast("int"))
dataframe = df2.withColumn("anoNascimento", col("anoNascimento").cast("int"))


# adicionando seculo de lançamento

# selecionando o ano de lancamento dos filmes 
df_ano = dataframe.dropDuplicates(["anoLancamento"]).select("anoLancamento")

# usar função map do rdd
dados = df_ano.rdd.map(lambda x: (x["anoLancamento"], ((x["anoLancamento"]//10) * 10)))
schema = StructType([
    StructField("anoLanc", IntegerType(), True),
    StructField("secLancamento", IntegerType(), True)
])

# criar um df com os dados rdd, adicionando um schema
df_sec = spark.createDataFrame(dados, schema)

#join com o dataframe, adicionando o seculo
df_id_art_sec = dataframe.join(df_sec, dataframe.anoLancamento == df_sec.anoLanc, 'inner').select(dataframe.idFilme, dataframe.tituloPrincipal, dataframe.anoLancamento,  df_sec.secLancamento, dataframe.generoFilme, dataframe.notaMedia, dataframe.idArtista, dataframe.nomeArtista, dataframe.generoArtista, dataframe.anoNascimento)


# separando os generos dos filmes

#selecionando o id e o genero do filme
df_gen = df_id_art_sec.dropDuplicates(["idFilme"]).select("generoFilme","idFilme")

#renomeando a coluna
df_gen = df_gen.withColumnRenamed("idFilme", "filme").withColumnRenamed("generoFilme", "genero")

# selecionando os genero que existem
gen = df_gen.dropDuplicates(["genero"]).select("genero")

#listando os genero
gen = list(gen.select("genero").toPandas()["genero"])
lista = []

# pegando cada string de conjunto de genero e separando cada genero
for elem in gen:
    genero_sep = elem.split(",")
    for e in genero_sep:
        # adicionando o genero separado em uma lista, caso ja nao esteva
        if e not in lista:
            lista.append(e)


for genero in lista:
    # seleciona os ids de filmes que tem o genero, e cria uma linha para cada genero
    df_genero = df_gen.select("filme").where(col("genero").rlike(f'{genero}$'))
    df_genero = df_genero.select("filme")
    df_genero = df_genero.withColumn("generoFilme", lit(genero))
    if genero == lista[0]:
        df_uniao_gen_fil = df_genero
    else:
        df_uniao_gen_fil = df_uniao_gen_fil.union(df_genero)

df_gen_completo = df_uniao_gen_fil

# join, a partir do id do filme, para adicionar cada linha de genero ao data frame
df_id_art_sec_gen = df_id_art_sec.join(df_gen_completo, df_id_art_sec.idFilme == df_gen_completo.filme, 'inner').select(df_id_art_sec.idFilme, df_id_art_sec.tituloPrincipal, df_id_art_sec.anoLancamento,  df_id_art_sec.secLancamento, df_gen_completo.generoFilme, df_id_art_sec.notaMedia, df_id_art_sec.idArtista, df_id_art_sec.nomeArtista, df_id_art_sec.generoArtista, df_id_art_sec.anoNascimento)


#adicionando id ao genero do filme

#selecionando o genero
df_gen_id = df_uniao_gen_fil.dropDuplicates(["generoFilme"]).select("generoFilme")

#adicionando id
df_gen_id = df_gen_id.withColumn("idGeneroFilme", monotonically_increasing_id())

#join pra adicionar a coluna id genero filme
df_completo = df_id_art_sec.join(df_gen_id, df_id_art_sec.generoFilme == df_gen_id.generoFilme, 'inner').select(df_id_art_sec.idFilme, df_id_art_sec.tituloPrincipal, df_id_art_sec.anoLancamento,  df_id_art_sec.secLancamento, df_id_art_sec.generoFilme, df_gen_id.idGeneroFilme,  df_id_art_sec.notaMedia, df_id_art_sec.idArtista, df_id_art_sec.nomeArtista, df_id_art_sec.generoArtista, df_id_art_sec.anoNascimento)


# dimensão artista
dim_art = df_completo.select("idArtista", "nomeArtista", "generoArtista", "anoNascimento").where("idArtista != 17179870826").distinct()
# garantindo que as colunas sejam do tipo certo
dim_artista = dim_art.withColumn("anoNascimento", col("anoNascimento").cast("int"))
# saida dim_artista
dim_artista.write.partitionBy("generoArtista").parquet(f'{target_path}/{data_hoje}/artista/')

#dimensão filme
dim_f = df_completo.select("idFilme", "tituloPrincipal", "anoLancamento").distinct()
# garantindo que as colunas sejam do tipo certo
dim_filme = dim_f.withColumn("anoLancamento", col("anoLancamento").cast("int"))
# saida dim_filme
dim_filme.write.partitionBy("anoLancamento").parquet(f'{target_path}{data_hoje}/filme/')

#dimensão genero
dim_genero = df_completo.select("idGeneroFilme", "generoFilme").distinct()
# saida dim_genero
dim_genero.write.parquet(f'{target_path}{data_hoje}/genero/')

# fato
fato = df_completo.select("idFilme", "idArtista","idGeneroFilme","notaMedia", "secLancamento").distinct()
# garantindo que as colunas sejam do tipo certo
fato = fato.withColumn("secLancamento", col("secLancamento").cast("int"))

# saida fato
fato.write.partitionBy("secLancamento").parquet(f'{target_path}/{data_hoje}/fato/')


job.commit()
