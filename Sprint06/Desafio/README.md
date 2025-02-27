# Sprint 06
## Desafio final - Parte 01
### Assunto de análise:
&nbsp;&nbsp;&nbsp;Antes do início da primeira parte do desafio é necessário definir sobre o que vai ser a análise final e o assunto de foco do desafio. Os assuntos que vou desenvolver serão:
* Que idade os atores e atrizes tem quando fazem séries/filmes bem avaliados? Com quais gêneros que eles se destacaram com essa idade?
* Quais os filmes de Sci-FI mais bem avaliados nos anos 2000 (2000-2009)? Qual a porcentagem de mulheres que trabalharam nesses filmes?

&nbsp;&nbsp;&nbsp; O primeiro assunto será uma análise sobre a idade que os atores mais produzem filmes e séries de destaque, se a idade tem ou não influência nesse destaque dos homens e das mulheres. Ainda nesse mesmo tópico, averiguar com quais gêneros que eles tiveram esse destaque, se essse gênero tem ou não alguma ligação com a idade e gênero dos profissionais na hora de fazer produções bem-avaliadas.

&nbsp;&nbsp;&nbsp; O segundo tópico é sobre os filmes mais bem avaliados do gênero Sci-FI nos anos 2000 e qual a porcentagem de mulheres que trabalharam nesses filmes. Essa análise tem como foco averiguar a participação de mulheres em filmes de destaques nessa época e categoria.

### Desafio:
&nbsp;&nbsp;&nbsp; O desafio então foi formado pela ingestão batch dos dados. Onde era necessário criar um bucket e fazer upload de objetos a esse bucket, isso por meio de um script Python, que por fim seria executado em um container no docker.
#### [Script Python](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint06/Evid%C3%AAncias/desafio_parte1.py):
&nbsp;&nbsp;&nbsp; O código python foi formado por quatro funções, sendo elas:
* Função de Login (user): essa função recebe o AdministradorAcess do usuário e retorna uma variável com a sessão do usuário e seu acesso. Essa variável é usada nas outras funções.
* Função de criar bucket (criar_bucket): Nessa função é recebido o nome do bucket que o usuário deseja criar e a variável gerada na função de Login. Com esses parâmetros ele cria o bucket caso ele já não exista na conta desse usuário e se o bucket for válido.
* Função listar buckets (list_buckets): Nessa função é recebido a variável gerada na função de Login, e é retornado uma lista com o nome dos buckets que tem na conta desse usuário.
* Função upload de objetos (upload_object): Nessa função são recebidos os parâmetros caminho do objeto, nome do bucket, a variável gerada na função de Login e o nome do objeto, e a partir desses parâmetros ele faz o upload do objeto no bucket anteriormente informado.<p>
&nbsp;&nbsp;&nbsp; O script então pede o profile_name, ou AdministradorAcess, para o usuário e invoca a função de Login. Após isso ele pede o nome do bucket. Então ele invoca, com a variável de login, a função listar buckets, que gera uma lista com os buckets que existem na conta do usuário. Com essa lista e o nome do bucket, ele averigua se já não existe na conta do usuário um bucket com esse mesmo nome. Caso já exista ele informa que o bucket ja existe e passa para o próximo passo. Caso não exista é invocado a função criar bucket, que cria um bucket com o nome fornecido, isso é claro, se o nome for único no mundo, respeita as regras de nomenclatura. Caso não respeite, será retornado o erro ao usuário. <p>
&nbsp;&nbsp;&nbsp; Após criar o bucket, o script pede ao usuário quantos objetos ele deseja adicionar ao bucket, a quantidade informada é adicionada em um for in range, que pede o caminho do objeto e o nome do objeto ao usuário. Com essas informações ele adiciona o objeto ao bucket inicialmente informado. Após concluír o upload do objeto ele informa que "O objeto taltal for adicionado ao bucket taltal.", isso é repetido até a quantidade de objetos informada ser adicionada ao bucket.   

#### [Dockerfile](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint06/Evid%C3%AAncias/desafio_Dockerfile):
&nbsp;&nbsp;&nbsp; No Dokerfile é usado como referência uma imagem paython, e são instalados o pip, o boto3, o botocore e o aws cli, além de serem copiados os arquivos parte1.py, movies.csv e series.csv para o diretório RawZone do container.

#### Execução:
&nbsp;&nbsp;&nbsp; Ocorreu então o build da imagem  e a  criação do volume ([comandos](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint06/Evid%C3%AAncias/desafio_1comandos_docker.txt)): <p>
<img src=..\..\Sprint06\Evidências\desafio_imagem1.png width=500><p>
&nbsp;&nbsp;&nbsp; Após isso executei um container no modo interativo e com o terminal bash ([comando](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint06/Evid%C3%AAncias/desafio_1comandos_docker.txt)), isso com o volume referênciado: <p>
<img src=..\..\Sprint06\Evidências\desafio_imagem2.png width=500> <p>
&nbsp;&nbsp;&nbsp; Fazendo a conexão com aws pelo terminal, : <p>
<img src=..\..\Sprint06\Evidências\desafio_imagem3.png width=500> <p>
&nbsp;&nbsp;&nbsp; Exectando o código python pelo terminal do container, criando o bucket e fazendo upload de objeto ([nome dos objetos](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint06/Evid%C3%AAncias/desafio_1nome_objeto.txt)): <p>
<img src=..\..\Sprint06\Evidências\desafio_imagem4.png width=500>