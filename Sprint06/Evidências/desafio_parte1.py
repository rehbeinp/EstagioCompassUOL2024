import boto3
from botocore.exceptions import ClientError
import logging

def user(profilename):                 #função que pede a cahve de acesso do usuário e diz o serviço
    session=boto3.Session(profile_name=profilename)
    s3=session.client('s3')
    return s3


def criar_bucket(nome, s3):    #função criar bucket, parâmetro nome do bucket e usuário
    try:
        s3.create_bucket(Bucket=nome)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_buckets(s3):             #função listar buckets
    try:
        lista_buckets=[]
        s3_client = s3
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:  #Para cada bucket, fazemos um looping para exibir os dados.
            lista_buckets.append(bucket['Name'])    #adiciona os nomes dos buckets numa lista
        return lista_buckets      
    except ClientError as e:
        print(e)
    
   
def upload_object(file_name, bucket, s3, object_name):
    if object_name is None:
        object_name = file_name

    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
      
    return True


#administradoracess 
profilename=input("Profile_name: ")
s3=user(profilename)                #variavel s3


#variaveis para criar bucket
nomebucket=input("Nome do bucket: ")


buckets_existentes=list_buckets(s3)
if nomebucket in buckets_existentes:
    print("Bucket já existe.")
else:
    criar_bucket(nomebucket, s3)
    print("Bucket criado. ")


#quantidade de objetos que serão adicionados no bucket
quant=int(input(f"Quantidade de objetos que quer adicionar no Bucket {nomebucket}: "))


for n in range (quant):
    #variaveis para adicionar objeto no bucket
    nome_chave=input(f"Informe o caminho do objeto: ")
    name=input("Nome do objeto: ")
    upload_object(nome_chave, nomebucket, s3, name)
    print(f"Objeto {name} adicionado ao bucket {nomebucket}. ")
