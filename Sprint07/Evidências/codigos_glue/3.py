import sys
import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as F
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
s3 = boto3.client('s3')

# Define o schema
schema = StructType([
    StructField("nome", StringType(), True),
    StructField("sexo", StringType(), True),
    StructField("total", IntegerType(), True),
    StructField("ano", StringType(), True)
])

# Lê o arquivo CSV com o schema definido
dataframe = spark.read.schema(schema).csv(source_file)
nomes_maiusculo = dataframe.select(upper("nome").alias("nome"), "sexo", "total", "ano")

nomes_maiusculos=nomes_maiusculo.write.partitionBy("sexo", "ano").json('s3://atividade-sprint07/lab-glue/frequencia_registro_nomes_eua')

job.commit()
'''Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3.Atenção aos requisitos:
A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do paths3://<BUCKET>/lab-glue/
O formato deve ser JSON
O particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem)

Escrever o código necessário para alterar a caixa dos valores da coluna nome paraMAIÚSCULO.'''