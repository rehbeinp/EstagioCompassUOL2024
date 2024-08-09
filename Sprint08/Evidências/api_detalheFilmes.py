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
    
    # função que pega os ids dos filmes
    def id_filmes(token):
        id_filmes=[]
        #gerando os ids dos filmes, range=45 pois 'total_pages': 45
        for i in range (45):                   
            url = f"https://api.themoviedb.org/3/movie/changes?end_date=2020-12-31&page={i+1}"

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {token}"}

            response = requests.get(url, headers=headers)
            data = response.json()
        
            for id in data['results']:
                df={"id":id['id']}             #pegando o id
                id_filmes.append(df)
        
        return id_filmes                    #retornando o id


    # função que gera o id do imdb e genero dos filmes. Parâmetro é o id do filme
    def genero_filmes(id,token):
        gen=[]
        #chamando os dados dos filmes atravez dos ids
        url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
        
        # iniciando uma variavel       
        df=None        
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        
        response = requests.get(url, headers=headers)
        data = response.text
        json_data = json.loads(data)
        
        #vendo se o resultado da chamada tem os todos os dados que preciso              
        if ('imdb_id' and 'genres') in json_data and json['imbd_id']!=None:
            
            # vendo se o json_data nao é igual a none
            if json_data['imdb_id'] != None:
                for genero in json_data['genres']:
                    df=str(genero['name'])
                    gen.append(df)
                
                gen=str(gen).strip("[]")
                df = {"idFilme": json_data['imdb_id'],
                "generoFilme": gen}
        
        return df


    #chamando a função para gerar os ids dos filmes e salvando em uma variável
    id_fil=id_filmes(token)
    
    # pegando o ultimo elemento da lista para controle
    ultimo_elemento = id_fil[-1:]
    ultimo_elemento = str(ultimo_elemento)
    ultimo_elemento = ultimo_elemento.strip("[]").strip("{}").strip("'id'").strip(":")
    ultimo_elemento=int(ultimo_elemento)
    registro=a=p=0
    filmes=[]
    
    # for com variavel dos ids, pegando id por id
    for id in id_fil:
        num_id = str({id['id']})
        num_id=num_id.strip("{}")
        num_id=int(num_id)
        #chamando a função dos dados dos filmes com o id gerado pela função id_filmes
        filme_gen = genero_filmes(num_id,token)
        
        #averiguando se é o ultimo elemento e salvando ele na lista em um arquivo se nao for nulo
        if ultimo_elemento == num_id and filme_gen != None:
            filmes.append(filme_gen)
            
            # salvando os arquivos da lista filmes
            nome_arquivo=f"filmes_id_e_genero_{a}.json"
                
            #função que escreve os dados em um arquivo e retorna o nome do arquivo
            nome_arq = escrevendo_arquivo(nome_arquivo, filmes)
            
            # função que faz o upload para o bucket 
            upload_objeto(nome_arq)
        
        #averiguando se é o ultimo elemento e salvando a lista em um arquivo se ele for nulo
        elif ultimo_elemento==num_id and filme_gen==None:
            
            # salvando os arquivos da lista filmes sem o ultimo elemento que é nulo
            nome_arquivo=f"filmes_id_e_genero_{a}.json"
                
            #função que escreve os dados em um arquivo e retorna o nome do arquivo
            nome_arq = escrevendo_arquivo(nome_arquivo, filmes)
            
            # função que faz o upload para o bucket 
            upload_objeto(nome_arq)
            
        # averiguando se a função nao retornou resultado nulo 
        elif  filme_gen!=None:
            
            # se passou de 100 registros salva os dados em um arquivo
            if p>a:
                # salvando os arquivos da lista filmes
                nome_arquivo=f"filmes_id_e_genero_{a}.json"
                
                #função que escreve os dados em um arquivo e retorna o nome do arquivo
                nome_arq = escrevendo_arquivo(nome_arquivo, filmes)
                
                # função que faz o upload para o bucket 
                upload_objeto(nome_arq)
                
                # atualizando o valor de a, e iniciando a lista filmes vazia 
                a=p
                filmes=[]
                filmes.append(filme_gen)
            
            #se não é o ultimo ou o centesimo continua a lista
            else:
                filmes.append(filme_gen)
                # variavel para controlar a quantidade de dados salvos por arquivo
                registro=registro+1
                # variavel que muda a cada 100 registros, usada no nome dos arquivos para controle
                p=registro//100
 