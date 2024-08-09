import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as Func
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from awsglue.dynamicframe import DynamicFrame
import pandas as pd
from datetime import date

data_hoje = (f"{date.today().year}/0{date.today().month}/0{date.today().day}")
## @params: [JOB_NAME] declarando variaveis de ambiente para a entrada dos dados do csv e dos jsons
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_CSV', 'S3_INPUT_PATH_json_ART','S3_INPUT_PATH_json_FIL','S3_TARGET_PATH'])
source_file_csv= args['S3_INPUT_PATH_CSV']
source_file_art = args['S3_INPUT_PATH_json_ART']
source_file_fil = args['S3_INPUT_PATH_json_FIL']
target_path = args['S3_TARGET_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
 
# função para retirar os acentos das palavras
@Func.pandas_udf('string')
def strip_accents(s: pd.Series) -> pd.Series:
    return s.str.normalize('NFKD').str.encode('ascii', 'ignore').str.decode('utf-8')

#função de saida do data frame
def saida(dataframe):
    # Converte o df_genero para DynamicFrame
    dynamic_frame = DynamicFrame.fromDF(dataframe, glueContext, "dynamic_frame")
    
    # saida 
    glueContext.write_dynamic_frame.from_options(
            frame=dynamic_frame,
            connection_type = "s3",
            connection_options = {"path":  f"{target_path}{data_hoje}", "partitionKeys": ["anoLancamento"]},
            format="parquet")
            
# PARTE 01
#caminho csv, lendo df spark
df = spark.read.csv(source_file_csv,header=True,inferSchema=True,sep="|")

#trabalhando os dados do csv
dataframe_csv=df.select("id", upper("tituloPincipal").alias("tituloPincipal") ,"anoLancamento", upper("genero").alias("generoFilme"), "notaMedia", upper("generoArtista").alias("generoArtista"), upper("nomeArtista").alias("nomeArtista"), "anoNascimento").where("notaMedia > 8.0")
dataframe_csv = dataframe_csv.withColumnRenamed("id", "idFilme")
dataframe_csv = dataframe_csv.withColumn('nomeArtista', strip_accents('nomeArtista'))

# Parte 02
# selecionando as colunas que não tem o ano de nascimento dos artistas
df_CSV_DT_NULA = dataframe_csv.filter(dataframe_csv.anoNascimento == r'\N')
df_CSV_DT_NULA1 = df_CSV_DT_NULA.select("idFilme","tituloPincipal","anoLancamento","generoFilme","notaMedia","generoArtista","nomeArtista")

# selecionando as colunas que tem o ano de nascimento dos artistas
dataframe_csv_DATA_COMPL = dataframe_csv.filter(dataframe_csv.anoNascimento != r'\N')

# Parte 03
#caminho dos dados dos artistas
for i in range (10):
    #trabalhando os dados dos artistas
    dataframe_art = spark.read.json(f"{source_file_art}dados_artistas_{i}.json")
    dataframe_art = dataframe_art.select("id", upper("nome").alias("nomeArtista"), year("dataNascimento").alias("anoNascimento"), "genero")
    dataframe_art = dataframe_art.withColumnRenamed("genero", "idGeneroArtista")
    dataframe_art = dataframe_art.withColumnRenamed("id", "idArtista")
    dataframe_art = dataframe_art.withColumn('nomeArtista', strip_accents('nomeArtista'))
    if i>0:
        # unindo em uma só tabela
        df_uniao_art = df_uniao_art.union(dataframe_art)
    else:
        df_uniao_art = dataframe_art
df_uniao_art = df_uniao_art.distinct()

# selecionando o nome e ano de nascimento dos artistas
df_art_join = df_uniao_art.select("nomeArtista","anoNascimento")

# Parte 04
# inner join para completar os anos da tabela csv que não tem o ano de nascimento dos artistas
dataframe_CSV_JOIN_DATA = df_CSV_DT_NULA1.join(df_art_join, df_CSV_DT_NULA1.nomeArtista == df_art_join.nomeArtista, 'inner').select(df_CSV_DT_NULA1.idFilme, df_CSV_DT_NULA1.tituloPincipal, df_CSV_DT_NULA1.anoLancamento, df_CSV_DT_NULA1.generoFilme, df_CSV_DT_NULA1.notaMedia,df_CSV_DT_NULA1.generoArtista, df_CSV_DT_NULA1.nomeArtista, df_art_join.anoNascimento)

# uniao das tabelas csv que tem o anoNascimento e a que foi adicionado agora
df_csv_all_years =  dataframe_csv_DATA_COMPL.union(dataframe_CSV_JOIN_DATA)

# Parte 05
# caminho dados filmes
for i in range (36):
    dataframe_fil = spark.read.json(f"{source_file_fil}filmes_id_e_genero_{i}.json")
    dataframe_fil = dataframe_fil.select("idFilme",upper("generoFilme").alias("generoFilme"))
    if i!=0:
        # unindo todas as tabelas de filmes
        df_uniao_fil=df_uniao_fil.union(dataframe_fil)
    else:
        # unindo todas as tabelas de idFilmes e generos
        df_uniao_fil = dataframe_fil
df_uniao_fil=df_uniao_fil.distinct()

#selecionando os filmes que tem o genero nulo
df_CSV_GEN_NULO = df_csv_all_years.filter(df_csv_all_years.generoFilme == r'\N')
df_CSV_GEN_NULO = df_CSV_GEN_NULO.select("idFilme","tituloPincipal","anoLancamento","notaMedia","generoArtista","nomeArtista","anoNascimento")

#selecionando os filmes que não tem o genero nulo
dataframe_csv_GEN_COMPL = df_csv_all_years.filter(df_csv_all_years.generoFilme != r'\N')

# Parte 06
#fazendo um join com os dados csv que nao tem genero pelo idFilme
dataframe_CSV_JOIN_GEN = df_CSV_GEN_NULO.join(df_uniao_fil, df_CSV_GEN_NULO.idFilme == df_uniao_fil.idFilme, 'inner').select(df_CSV_GEN_NULO.idFilme, df_CSV_GEN_NULO.tituloPincipal, df_uniao_fil.generoFilme, df_CSV_GEN_NULO.anoLancamento, df_CSV_GEN_NULO.notaMedia, df_CSV_GEN_NULO.generoArtista, df_CSV_GEN_NULO.nomeArtista, df_CSV_GEN_NULO.anoNascimento)

# fazendo a uniao dos csv que tem os generos com o que foi gerado
df_csv_dados_completos =  dataframe_csv_GEN_COMPL.union(dataframe_CSV_JOIN_GEN)

# Parte 07
saida(df_csv_dados_completos)

job.commit()













