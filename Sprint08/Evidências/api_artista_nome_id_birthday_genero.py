import json
import boto3 
import requests
import os
from datetime import date

os.chdir('/tmp/')

def lambda_handler(event, context):
    token=""
    # função de upload do objeto
    def upload_objeto(file_name):
        os.chdir('/tmp/')
        s3_client = boto3.client('s3')
        bucket_name = 'raw-zone-paula-rehbein'
        data_hoje = (f"{date.today().year}/0{date.today().month}/0{date.today().day}")
        object_name=f'Raw/TMDB/JSON/{data_hoje}/{file_name}'
        resposta = s3_client.upload_file(file_name, bucket_name, object_name)
        return resposta
    
    # funçaõ de gravar arquivo
    def escrevendo_arquivo(nome, dados):
        with open(nome, "w", encoding='utf-8') as arquivo:
            json.dump(dados, arquivo)
        arquivo.close()
        
        return nome   # retorna o nome do arquivo
    
    # chamada api generos
    def genero_filmes(token):
        generos=[]
        url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        for id in data['genres']:
            df={"id": id['id'],
                "genero": id['name']
                }             #pegando o id e nome do genero
            generos.append(df)
            
        return generos
    
    
    def id_artistas(token):
        id_artistas=[]
        
        #gerando os ids dos artistas, range=41 pois há 41 paginas
        for i in range (44):                   
            url = f"https://api.themoviedb.org/3/person/changes?end_date=2022-12-31&page={i+1}"

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {token}"
            }

            response = requests.get(url, headers=headers)
            data = response.json()
        
            for id in data['results']:
                df={"id":id['id']}             #pegando o id
                id_artistas.append(df)
        
        return id_artistas             #retornando o id
    
    # função que gera os ids, nome, genero, e data de nascimento ds artistas. Parâmetro é o id do artista
    def nome_birthday_gender_artista(id,token):
        
        #chamando os dados dos artistas atravez dos ids
        url = f"https://api.themoviedb.org/3/person/{id}?language=en-US" 
        
        # iniciando uma variavel
        df=None                
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        
        response = requests.get(url, headers=headers)
        data = response.text
        json_data = json.loads(data)
        
        #vendo se o resultado da chamada tem todos os dados que preciso              
        if ('id' and 'name' and 'birthday' and 'gender') in json_data:  
            
            # vendo se o json_data nao é igual a none
            if json_data['birthday'] != None:
                df = {
                    "id": json_data['id'],
                    "nome": json_data['name'],
                    "dataNascimento": json_data['birthday'],
                    "genero": json_data['gender']
                    }
                
        return df      #retorna variavel com o id, nome, dataNascimento e genero dos artistas

    #chamando a função que gera a lista de generos filmes e os ids
    dados_generos=genero_filmes(token)
    
    # funçaõ que grava os dados em um arquivo
    nome_arquivo_generos="genero_filmes.json"
    genero = escrevendo_arquivo(nome_arquivo_generos, dados_generos)
    
    # upload de genero_filmes para o bucket
    upload_objeto(genero)

    # chamando a função id_artista e salvadno os ids em uma variavel
    id_art=id_artistas(token)
    
    # pegando o ultimo elemento da lista para controle
    ultimo_elemento = id_art[-1:]
    ultimo_elemento = str(ultimo_elemento)
    ultimo_elemento = ultimo_elemento.strip("[]").strip("{}").strip("'id'").strip(":")
    ultimo_elemento=int(ultimo_elemento)
    registro=a=p=0   #variavel para contar os registros
    artistas=[]
    
    # for com variavel dos ids, pegando id por id
    for id in id_art:
        num_id = str({id['id']})
        num_id=num_id.strip("{}")
        #chamando a função dos dados dos artistas com o id gerado pela função id_artistas
        art = nome_birthday_gender_artista(num_id,token)
        
        if ultimo_elemento == num_id and art != None:
            artistas.append(art)
            
            # salvando os arquivos da lista filmes
            nome_arquivo=f"dados_artistas_{a}.json"
                
            #função que escreve os dados em um arquivo e retorna o nome do arquivo
            nome_arq = escrevendo_arquivo(nome_arquivo, artistas)
            
            # função que faz o upload para o bucket 
            upload_objeto(nome_arq)
        
        #averiguando se é o ultimo elemento e salvando a lista em um arquivo se ele for nulo
        elif ultimo_elemento==num_id and art==None:
            
            # salvando os arquivos da lista filmes sem o ultimo elemento que é nulo
            nome_arquivo=f"dados_artistas_{a}.json"
                
            #função que escreve os dados em um arquivo e retorna o nome do arquivo
            nome_arq = escrevendo_arquivo(nome_arquivo, artistas)
            
            # função que faz o upload para o bucket 
            upload_objeto(nome_arq)
            
        
        # averiguando se a função nao retornou resultado nulo
        elif art != None:
            if p>a:
                # salvando os arquivos da lista artistas
                nome_arquivo_artistas=f"dados_artistas_{a}.json"
                
                #função que escreve os dados em um arquivo e retorna o nome do arquivo
                nome_arq_artistas = escrevendo_arquivo(nome_arquivo_artistas, artistas)
                
                # função que faz o upload para o bucket 
                upload_objeto(nome_arq_artistas)
                
                # atualizando o valor de a, e iniciando a lista artistas vazia 
                a=p
                artistas=[]
                artistas.append(art)
            else:
                
                artistas.append(art)
                
                # variavel para controlar a quantidade de dados salvos por arquivo
                registro=registro+1
                
                # variavel que muda a cada 100 registros, usada no nome dos arquivos para controle
                p=registro//100