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

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Define o schema
schema = StructType([
    StructField("nome", StringType(), True),
    StructField("sexo", StringType(), True),
    StructField("total", IntegerType(), True),
    StructField("ano", StringType(), True)
])

# Lê o arquivo CSV com o schema definido
dataframe = spark.read.schema(schema).csv(source_file)
maior_masc=dataframe.groupBy("ano","sexo","nome").agg(max("total")).where(Func.col("sexo")=='M').limit(1)

# Converte o DataFrame para DynamicFrame
dynamic_frame = DynamicFrame.fromDF(maior_masc, glueContext, "dynamic_frame")

# Mostra o esquema do DynamicFrame
dynamic_frame.printSchema()

glueContext.write_dynamic_frame.from_options(
        frame=dynamic_frame,
        connection_type = "s3",
        connection_options = {"path": target_path},
        format="csv")
    
job.commit()

''' qual foi o nome masculino com mais registros e em que ano ocorreu.'''