# Sprint 09
## Desafio final - Parte 04
&nbsp;&nbsp;&nbsp; A quarta parte do desafio final foi formada pela modelação dos dados armazenados na camada Trusted. Os dados deviam ser modelados de acordo com o modelo dimensional e armazenados na camada Refined.

&nbsp;&nbsp;&nbsp; Inicialmente considerei os dados que tinha na camada Trusted, que eram: idFilme, tituloPrincipal, anoLancamento, generoFilme, notaMedia, gêneroArtista, nomeArtista e anoNascimento. Tendo em vista esses dados considerei que seria necessário criar algumas colunas antes de modelá-los. Sendo assim segue os passos para a criação do código do [Job do glue](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/glue_refined.py): 
* Primeira parte, coluna idArtista: Após ler o arquivo da camada Truested, selecionei todos os nomes dos artistas e armazenei em um dataframe (*dataframe_nomes_art*). Depois com uma função do spark (*monotonically_increasing_id*) adicionei um id para cada artista, gerando a coluna **idArtista**. Com a coluna completa adicionei-a ao data frame principal por meio de um *join* através da coluna **nomeArtista**. Linha 33 no [arquivo](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/glue_refined.py).
* Segunda parte, coluna secLancamento: Do dataframe, que agora possui a coluna *idArtista*, selecionei os anos de lançametos distintos e adicionei em um dataframe (*df_ano*). Converti esse dataframe spark para um dataframe RDD, e usei a função *map* para fazer uma equação, com cada ano, que retorna o século. Com a coluna século criada, converti novamente o dataframe para spark, e adicionei a coluna **secLancamento** ao dataframe principal por meio de um *join* através da coluna **anoLancamento**. Linha 50 no [arquivo](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/glue_refined.py).
* Terceira parte, coluna generoFilme: 
    * O dataframe possuia a coluna generoFilme, que era composta por todos os gêneros dos filmes juntos, em uma mesma string. Como parte da minha pergunta leva em consideração o gênero dos filmes, decidi separá-los, colocando cada gênero em uma linha. Assim, do dataframe principal, que possui agora também as colunas *idArtista* e *secLancamento*, selecionei os ids dos filmes e os gêneros que correspondiam a esse id e armazenei em um dataframe (*df_gen*). Depois selecionei ainda apenas os gêneros e armazenei em outro dataframe (*gen*), que converti para pandas e depois para tipo lista. 
    * Com a lista dos gêneros criada, peguei cada conjunto de gênero e realizei um *split*, que gerou uma lista (*genero_sep*) com os gêneros que compunham o conjunto de gêneros. Assim cada gênero separado era armazenado em uma outra lista caso já não estivesse nela. 
    * Com uma lista com todos os gênero dos filmes, fiz um for, pegando gênero por gênero, e usando com a função *rlike* do spark, para selecionar os ids dos filmes que tinham aquele gênero. Com os filmes selecionados gerei a coluna generoFilme com o valor padrão do gênero usado na consulta do *rlike*, criando o dataframe (*df_genero*) com as colunas *idFilme* e *generoFilme*.

    Assim todos os dataframes gerados foram unidos em um só (*df_uniao_gen_fil*). Então adicionei a coluna dos gêneros separados ao dataframe principal por meio de um *join* através da coluna *idFilme*. Linha 69 no [arquivo](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/glue_refined.py).
* Quarta parte, idGeneroFilme: Com o dataframe que agora possui as colunas *idArtista* e *secLancamento*, e a coluna *generoFilme* alterada, era necessário adicionar uma coluna com o id do gênero dos filmes. Assim, selecionei cada gênero diferente do dataframe com os gêneros dos filme (*df_uniao_gen_fil*) e adicionei um id a cada gênero por meio da função spark *monotonically_increasing_id*, gerando a coluna idGeneroFilme. Após isso adicionei a coluna gerada ao dataframe principal por meio de um *join*, através da coluna generoFilme. Linha 109 no [arquivo](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/glue_refined.py). 
* Quinta parte, dimensões e fato: Com todas as coluna necessárias criadas, defini as dimensões:
    * Dimensão Artista: Essa dimensão informa as caracteríscas dos artistas como *idArtista*, *nomeArtista*, *generoArtista*, *anoNascimento*. 
    * Dimensão Filmes: Essa dimensão informa as caracteríscas dos filmes como *idFilme*, *tituloPrincipal*, *anoLancamento*.
    * Dimensão Gênero: Essa dimensão tem os dados do gênero como *idGeneroFilme* e o *generoFilme*.
    * Fato: o fato é composto pelo *idFilme*, *idArtista*, *notaMedia*, *idGeneroFilme* e *secLancamento*. O fato é capaz de responder perguntas como O que? (o filme de gênero "tal") Quem? (os artistas) Quando? (século de lançamento).

* Modelo dimensional: 

<img src= ../Evidências/modelo_dimensional.png width=500 >

* Dimensão artista: 

<img src= ../Evidências/dim_artista.png width=500 >

* Dimensão filme:

<img src= ../Evidências/dim_filme.png width=500 >

* Dimensão gênero:

<img src= ../Evidências/dim_genero.png width=500 >

* Fato:

<img src= ../Evidências/fato.png width=500 >

* [Arquivo de organização.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/organização.txt)

## Alteração da camada Trusted: 
&nbsp;&nbsp;&nbsp; Realizei nessa sprint ainda a modificação em uns dados da camada Truested. 
* Alterei o tipo de armazenamento, que antes era armazenado como DynamicFrame, agora é armazenado como sparkDataframe. Mudei pois o Glue não conseguiu ler os dados salvos em Parquet na camada Truested, então a mudança foi necessária. Linha 109 no [arquivo](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/Glue_trusted.py).
* Aterei o nome da coluna *tituloPincipal* para *tituloPrincipal*. Linha 104 no [arquivo](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint09/Evid%C3%AAncias/Glue_trusted.py).

## Alteração na Pergunta do Desafio Final:
&nbsp;&nbsp;&nbsp; As perguntas redefinidas são:
* Que idade os atores e atrizes tem quando fazem filmes bem avaliados? Com quais gêneros que eles se destacaram com essa idade?
* A idade que os atores e atrizes fazem filmes bem avaliados muda ao longo dos séculos?

&nbsp;&nbsp;&nbsp; A alteração da primeira pergunta aconteceu porque fazer uma análise de filmes e séries seria muito pesado, e talvez incompleto, assim optei por focar apenas nos filmes, deixando as séries de lado.

&nbsp;&nbsp;&nbsp; A alteração da segunda pergunta foi total, isso ocorreu principalmente porque a maioria dos dados que precisaria para responder corretamente a pergunta anterior estariam incompletos (como o elenco inteiro de cada filme dos anos 2000). Isso ocorreu pois foquei mais na primeira pergunta, que eu considero mais interessante de ser respondida. Assim alterei a segunda pergunta para ser um complemento da primeira.

&nbsp;&nbsp;&nbsp; Acho importante reafirmar que as perguntas serão respondidas com os dados dos artistas presentes no CSV ingerido na sprint 06, não adicionei artistas, apenas complementei (ou tentei complementar) dados dos mesmos que estivessem nulos.
