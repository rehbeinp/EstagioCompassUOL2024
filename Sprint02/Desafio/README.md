# Sprint 02
## Desafios:
&nbsp;&nbsp;&nbsp;Após finalizar os cursos havia desafios para serem feitos. Dois sobre manipulação de dados de um banco de uma biblioteca. E mais um sobre normalização de bancos de dados, e modelagem dimensional. <p>
&nbsp;&nbsp;&nbsp; 
<p>
<p>

### Desafio de Manipulação:
&nbsp;&nbsp;&nbsp;As primeiras atividades era sobre manipulação de dados de uma biblioteca, onde na primeira consulta  foi necessário selecionar os [10 livros mais caros](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/2.livros_mais_caros.csv) juntamente com o seu titulo, código, valor, autor e código, e editora e código.
<p>
<img src=../../imgs/livrosmaiscaros.png width=200> 
<p>

&nbsp;&nbsp;&nbsp;Já na segunda consulta era preciso filtrar as  [5 editoras que mais obtinham livros](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/1.editora_mais_livros.csv) na biblioteca e apresentar seu nome, código, e quantidade de livros total.
<p>
<img src=../../imgs/maislivros.png width=200> <p>
&nbsp;&nbsp;&nbsp;Este desafio não foi muito complexo, acredito que não houve dificuldades pelo aprendizado durante curso, sendo essas atividades muitos parecidas com as de prática disponíveis na plataforma.
<p>&nbsp;&nbsp;&nbsp;O resultado de ambas as consultas está disponibilizado em um arquivo CSV, na pasta 2.Evidências, sendo os dois primeiros arquivos.<p>

### Desafio de Normalização e Modelagem:
&nbsp;&nbsp;&nbsp;O presente desafio era sobre a normalização de um banco de dados de uma locadora de carros, modelando-o de forma relacional, e após isso com o resultado da normalização, gerar um modelo dimensional.
<p>

&nbsp;&nbsp;&nbsp;Na normalização evitei a repetição dedos, garantindo que eles estivessem somente em um lugar, relacionei as tabelas pelo código do objeto, e coloquei informações sobre somente um tópico em cada view (tabela) criada. Inicialmente, realizei a separação dos dados por categorias, sendo elas: _cliente, carro, vendedor, tempo, locação, total_ e _combustível_. Sendo cada categoria com o id (código) de cada objeto e informações expecíficas, como nome, estado e país do _cliente_, ou chassi modelo, ano, marca e código do combustível do _carro_. Optei por criar também a categoria _total_, que apresenta a quantidade de dias que foi locado o carro, o preço por dia da locação, a quilometragem que o carro apresenta ao ser locado, o id (código) da locação, e o total (preço) que gerou a locação.
<p>

&nbsp;&nbsp;&nbsp;Já o modelo dimensional, gerado a partir do modelo relacional, as informações foram agrupadas nas categorias: *[dim_cliente](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/dim_cliente_202405171445.sql), [dim_carro](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/dim_carro_202405171446.sql), [dim_vendedor](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/dim_vendedor_202405171447.sql), [dim_tempo](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/dim_tempo_202405171447.sql), [dim__combustível](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/dim_combustivel_202405171446.sql) *e* [fato_locação](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint02/Evid%C3%AAncias/fato_locacao_202405171447.sql)*. Nas dimensões estão presentes dados como nome, código, estado e gênero do vendedor na *dim_vendedor*, ou data e hora da locação, e data e hora da entrega do carro na *dim_tempo*. Na dimensão *fato_locacao* agrupei os dados do fato ocorrido, com o id da locação, id do carro, id do cliente, id do vendedor, data locação, valor por dia, quilometragem do carro, e quantidade de dias locados. Todas as informções da *fato_locacao* respondem perguntas como: Quem alugou? Quando alugou? O que alugou? Quanto pagou? Por quanto tempo ficou alugado? E quem foi o vendedor que fez o aluguel? Cumprindo com o objetivo de responder o fato ocorrido. <p>
&nbsp;&nbsp;&nbsp; Durante o desenvolvimento do desafio foram aparesendo dificuldades, mas não muito complexas, sendo elas resolvidas com um pouco de pesquisa ou averiguação do conteúdo do curso.

&nbsp;&nbsp;&nbsp;A imagem abaixo apresenta a representação do modelo relacional (á esquerda, em cinza), a tabela do banco de dados *tb_locacao* (no meio, em bege), e o modelo dimensional (á direita, em verde). <p>
<img src=../../imgs/ModeloRelacional_e_Dimencinal.png width=600> <p>
&nbsp;&nbsp;&nbsp; Está disponibilizado arquivos SQL com os resultados do modelo dimensional, nessa mesma Sprint02 na pasta 2.Evidências, os nomes iniciam com 'dim_carro' por exemplo (exeto pela 'fato_locacao').
