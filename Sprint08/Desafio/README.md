# Sprint 08
## Desafio final - Parte 03
&nbsp;&nbsp;&nbsp; O desafio foi formado pelo tratamento dos dados ingeridos na primeira (dados do CSV) e na segunda etapa (dados do JSON). Os dados deveriam ser trabalhados no AWS Glue, se tornando limpos e confiáveis, e ser armazenados no S3 na camada Truested, para posteriormente serem consumidos. <p>
&nbsp;&nbsp;&nbsp;Iniciando o desafio no AWS Glue, percebi que muitos dados essênciais para a minha consulta, como o ano de nascimento dos artistas e o gênero dos filmes, estavam nulos. Para conseguir um resultado final mais preciso e não descartar todos os dados nulos (que eram muitos), decidi fazer uma chamada de API que traria esses dados.<p>

*  [Chamada API artistas](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/api_artista_nome_id_birthday_genero.py): Assim organizei o código em funções que seriam chamadas na hora certa. 
    * Função upload_objeto, que faz upload do arquivo para o bucket atravez do nome do aquivo.  
    * Função escrevendo_arquivo, que escreve um arquivo recebendo os dados e o nome do arquivo como parâmetro, retorna o nome do arquivo.
    * Função gênero_filmes, que gera os genêros e os ids dos gêneros dos filmes, retorna uma lista contento os dados.
    * Função id_artistas, que passa página por página armazenando os ids dos artistas, retorna uma variável com os ids.
    * Função nome_birthday_gender_artista, recebe o id do artista e retorna uma variável com o nome, o id, a data de nascimento e o id do gênero do artista. <p>

&nbsp;&nbsp;&nbsp; Assim comecei invocando a função gênero_filmes, e salvando os dados gerados atravez da função escrevendo_arquivo e upload_objeto.

&nbsp;&nbsp;&nbsp; Depois chamo a função id_artista e faço um for na variável retornada, pegando id por id para chamar a função nome_birthday_gender_artista com esse id retornado. Assim é retornado os dados dos artistas, que são armazenados em uma lista. Essa lista, ao completar 100 retornos não nulos salvos, é salva em um arquivo com a função escrevendo_arquivo e armazenada no S3 com a função upload_objeto. 

*  [Chamada API filmes](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/api_detalheFilmes.py): O código da API que pega os dados dos artistas foi organizado da seguinte forma: 
    * Função upload_objeto, que faz upload do arquivo para o bucket atravez do nome do aquivo.  
    * Função escrevendo_arquivo, que escreve um arquivo recebendo os dados e o nome do arquivo como parâmetro, retorna o nome do arquivo.
    * Função id_filmes, recebe o token do TMDB como parâmetro e retorna uma variável contendo os ids dos filmes.
    * Função gênero_filmes, recebe o id do filme e o token do TMBD e retorna, se tiver, o id do IMDB e o gênero do filme. <p>
    
&nbsp;&nbsp;&nbsp; Assim comecei invocando a função id_filmes, e fiz um for com a variável retornada, pegando assim id por id, e chamando a função gênero_filmes com cada id. O retorno da função gênero_filmes foi adicionado em uma lista que, ao completar 100 retornos salvos era escrita em um arquivo com a função escrevendo_arquivo e armazenada no S3 com a função upload_objeto. <p>

&nbsp;&nbsp;&nbsp; Todas os códigos das APIs foram rodadas no AWS Lambda.<p>
<img src=..\..\Sprint08\Evidências\api_artistas.png width=500><p> 

&nbsp;&nbsp;&nbsp; Tendo os dados das chamadas de API coletados era hora de processá-los, assim a partir do código [Glue_completo.py](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/Glue_completo.py) foi realizado o trabalho dos dados. O código foi formado por partes, para completar os dados nulos do CSV:
* Parte 01: Primeiramente foi lido os dados do CSV e selecionadas as colunas: id, tituloPrincipal, anoLancamento, gênero, notaMedia, gêneroArtista, nomeArtista e anoNascimento. Tendo como condição de seleção apenas os dados que tivessem a notaMedia maior que 8.0, que é a nota que considerei para responder as minhas perguntas, e que tivessem o ano de lançamento diferente de nulo. Todas as colunas formadas por string tiveram as letras alteradas para letra maiúscula, e algumas colunas foram renomeadas, como id para idFilme. Ainda na coluna nomeArtista ainda teve os acentos removidos. Formando dessa forma o dataframe_csv.
* Parte 02: Tendo os dados do CSV ligeiramente padronizados, era necessário completar ou remover os dados nulos, assim, selecionei do dataframe_csv todos os dados que tivessem o ano de nascimento dos artistas nulos, e salvei em um data frame (df_CSV_DT_NULA1). Ainda selecionei os dados em que o ano de nascimento dos artistas não eram nulos formando outro data frame (dataframe_csv_DATA_COMPL).
* Parte 03: Tendo os dados do CSV separados era necessário preparar os dados dos artistas armazenados no JSON. Assim selecionei em cada arquvo JSON, o id, nome, data de nascimento (selecionando apenas o ano), e o gênero dos artistas. As colunas formadas por string tiveram as letras alteradas para letra maiúscula, e algumas colunas foram renomeadas e a coluna nome ainda teve os acentos removidos. Depois que o arquivo era trabalhado ele era agrupado em um único data frame (df_uniao_art). E desse data frame (df_uniao_art), eram selecionadas as colunas nomeArtista e anoNascimento que formava o df_art_join.
* Parte 04: Assim, foi realizado um inner join a partir da coluna nomeArtistas, com os datas frames df_CSV_DT_NULA1 e df_uniao_art, com a intenção de preencher os anos de nascimento nulos presentes em df_CSV_DT_NULA1. Foi realizado um inner join pois, caso não houvesse dados para completar algumas colunas elas já seriam descartadas, visto que não se pode trabalhar com dados nulos e que os dados da dos artistas gerados na API seriam os disponíveis para completar. O resultado do inner join (dataframe_CSV_JOIN_DATA) foi unido então com o data frame dataframe_csv_DATA_COMPL, formando um data frame sem datas nulas (df_csv_all_years).
* Parte 05: Com os anos de nascimento completos era necessário completar os gêneros dos filmes que estavam nulos. Dessa forma carreguei e trabalhei os dados dos arquivos que continham os ids e gênero dos filmes (tornando maiúscula a coluna de gênero e renomeando as colunas) e os uni em um só data frame (df_uniao_fil). Após trabalhar os dados dos filmes, selecionei do df_csv_all_years as colunas que tinham gênero nulo (formando o df_CSV_GEN_NULO) e as que não tinhas os gêneros nulos (formando o dataframe_csv_GEN_COMPL).
* Parte 06: Tendo os dados com gênero nulo separados, fiz um inner join a partir da coluna idFilme com os dados de df_uniao_fil e de df_CSV_GEN_NULO, gerando assim o dataframe_CSV_JOIN_GEN, que teria apenas os dados dos filmes que teriam o gênero completo, já descartando os com gênero nulo. Por fim realizei uma união com o dataframe_CSV_JOIN_GEN e o dataframe_csv_GEN_COMPL, formando o df_csv_dados_completos que tem apenas dados não nulos.
* Parte 07: Saida do df_csv_dados_completos para a camada Trusted do bucket.
