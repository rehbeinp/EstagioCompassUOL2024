#2 parametros logicos
# 1 funçao condicional
# 1 funçaõ de converção
# 1 função de string:

import boto3

session=boto3.Session(
    profile_name='AdministratorAccess')
s3=session.client('s3')

resp = s3.select_object_content(
    Bucket="bucket-saprint05",
    Key="escola_tecnicas.csv",
    ExpressionType='SQL',
    Expression="SELECT case when NU_ANO_CENSO = '2023' then cast('2023-01-01' as timestamp) end as ANO_CENSO, UPPER(NO_REGIAO) as NO_REGIAO, NO_ENTIDADE, NO_AREA_CURSO_PROFISSIONAL, NO_CURSO_EDUC_PROFISSIONAL, CASE when TP_LOCALIZACAO = '1' then 'urbana' else 'rural' end as LOCALIDADE, cast(QT_MAT_CURSO_TEC as int) as quant_matri_curso_tec FROM s3object as s WHERE s.NO_AREA_CURSO_PROFISSIONAL = 'Informação e comunicação' or s.NO_AREA_CURSO_PROFISSIONAL = 'Gestão e negócios' and not s.NO_AREA_CURSO_PROFISSIONAL = 'Infraestrutura' limit 20;",
    InputSerialization = {'CSV': {"FileHeaderInfo": "Use", "FieldDelimiter":";"},'CompressionType':'NONE'},
    OutputSerialization = {'CSV': {}},
)

for evento in resp['Payload']:
    if 'Records' in evento:
        records = evento['Records']['Payload'].decode('utf-8')
        print(records)
