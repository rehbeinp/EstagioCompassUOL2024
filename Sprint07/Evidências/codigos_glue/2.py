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

with open("schema_dataframe.json", "w") as arquivo:
        arquivo.write(schema)
        
bucket_name="aws-glue-assets-851725533691-us-east-1"
file_name = 'schema_dataframe.json'
object_name='sparkHistoryLogs/schema_dataframe.json'
resposta = s3.upload_file(file_name, bucket_name, object_name)

job.commit()