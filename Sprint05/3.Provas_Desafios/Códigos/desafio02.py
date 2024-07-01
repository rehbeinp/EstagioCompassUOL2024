#2 função de agregação:

#resultado: número mínimo de matrículas que foi realizada em um curso, número maximo de matrículas que foi 
#realizada em um curso, quantidade total de matrículas realizadas em 2023, quantidade de matrículas por curso em 2023

import boto3

session=boto3.Session(
    profile_name='AdministratorAccess')
s3=session.client('s3')

resp = s3.select_object_content(
    Bucket="bucket-saprint05",
    Key="escola_tecnicas.csv",
    ExpressionType='SQL',
    Expression="SELECT MIN(cast(QT_MAT_CURSO_TEC as int)), MAX(cast(QT_MAT_CURSO_TEC as int)), sum(cast(QT_MAT_CURSO_TEC as int)), ((sum(cast(QT_MAT_CURSO_TEC as int)))/(sum(cast(QT_CURSO_TEC as int)))) FROM s3object",
    InputSerialization = {'CSV': {"FileHeaderInfo": "Use", "FieldDelimiter":";"},'CompressionType':'NONE'},
    OutputSerialization = {'CSV': {}},
)

for evento in resp['Payload']:
    if 'Records' in evento:
        records = evento['Records']['Payload'].decode('utf-8')
        print(records)