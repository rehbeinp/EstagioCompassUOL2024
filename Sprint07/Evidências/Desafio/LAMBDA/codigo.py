import json
import boto3 
import requests                #biblioteca adicionada com layer
import os


def lambda_handler(event, context):
    s3_client = boto3.client('s3')                
    bucket_name = 'raw-zone-paula-rehbein'
    
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer TOKEN_ACESSO"              # chamada de api
    }
    
    response = requests.get(url, headers=headers)          # pegando os dados e salvando em response
    
    with open("genero_filmes.json", "w") as arquivo:       # escrevendo a chamada em um arquivo json
        arquivo.write(response.text)
    
    file_name = 'genero_filmes.json'                                    # nome do arquivo
    object_name='Raw/TMDB/JSON/2024/07/24/genero_filmes.json'           # nome objeto
    resposta = s3_client.upload_file(file_name, bucket_name, object_name)   #fazendo upload do objeto para o bucket