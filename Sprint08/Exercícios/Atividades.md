# Sprint 08:
## Atividades:
&nbsp;&nbsp;&nbsp; Haviam atividades para serem realizadas, uma sobre gerar dados e outra sobre manipulá-los com Spark.
### Geração em massa de dados:
&nbsp;&nbsp;&nbsp; As atividades de gerar dados em massa deveriam ser desenvolvidas em Python.
* Etapa 01: Inicializar uma lista com 250 números aleatórios,  [código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/ativ1_números_aleatórios.py).
* Etapa 02: Declar uma lista contendo 20 animais, ordená-los em ordem ordem descente, interar os itens e gravá-los em um arquivo em formato csv, [código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/ativ1_animais_aleatórios.py).
* Etapa 03: Gerar um Dataset com 10 milhões de nomes de pessoas, [código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/ativ1_nomes_aleatorios.py).

### Manipulação de dados com Apache Spark:
&nbsp;&nbsp;&nbsp; Nessa atividade foi usado o Dataset de nomes gerado na atividade anterior. 
* Etapa 01: criar o dataframe a partir do arquivo de nomes aleatórios e listar alguns nomes.
* Etapa 02: renomear a coluna para nomes, e imprimir 10 linhas do dataframe:

<img src= ../Evidências/ativ2_etapa1.png width=500 >

* Etapa 03: adicionar uma noma coluna chamada escolaridade ao dataframe, dando os valores 'médio', 'fundamental' e 'superior' de forma aleatória. Não consegui fazer uso do Spark em um Script Python e usei apenas o terminal, sendo assim era impossível, até onde eu sei, gerar os valores de forma aleatória a partir do Spark, então criei um [código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/ativ1_escolaridade.py) em python que gerava essa coluna. Para atribuir essas valores aos nomes usei o método rand, que gera números aleatórios entre 0 e 1, adicionando uma coluna rand em cada dataframe.

<img src= ../Evidências/ativ2_etapa2.png width=500 >
<img src= ../Evidências/ativ2_etapa1.1.png width=500 >

&nbsp;&nbsp;&nbsp; Após adicionar a coluna rand, fiz um join entre os dataframes: 

<img src= ../Evidências/ativ2_etapa3.png width=500 >

* Etapa 04: adicionar uma nova coluna chamada país ao dataframe, atribuindo de forma aleatória algum dos 13 países da América do Sul. Da mesma forma, gerei a colula a partir de um [código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/ativ1_pais.py) Python, e após ler, renomear, e adicionar uma coluna com os valores rand, a adicionei ao dataframe df_nome a partir de um join.

<img src= ../Evidências/ativ2_etapa4.png width=500 >
<img src= ../Evidências/ativ2_etapa4.1.png width=500 >

* Etapa 05: adicionar uma nova coluna chamada anoNascimento ao dataframe, a adicionar a cada linha um valor aleatório entre 1945 e 2010. Da mesma forma, gerei a colula a partir de um [código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint08/Evid%C3%AAncias/ativ1_ano_nascimento.py) Python, e após ler, renomear, e adicionar uma coluna com os valores rand, a adicionei ao dataframe df_nome a partir de um join.

<img src= ../Evidências/ativ2_etapa5.png width=500 >
<img src= ../Evidências/ativ2_etapa5.1.png width=500 >

* Etapa 06: selecionar as pessoas que nascem nesse século, armazenar o resultado em outro dataframe df_select e mostrar 10 linhas do resultado:

<img src= ../Evidências/ativ2_etapa6.png width=500 >

* Etapa 07: usando SparkSQL selecionar as pessoas que nascem nesse século, armazenar o resultado em outro dataframe df_select e mostrar 10 linhas do resultado:

<img src= ../Evidências/ativ2_etapa7.png width=500 >

* Etapa 08: contar o número de pessoas que nasceram na geração Millenals: 

<img src= ../Evidências/ativ2_etapa8.png width=500>

* Etapa 09: usando SparkSQL contar o número de pessoas que nasceram na geração Millenals:

<img src= ../Evidências/ativ2_etapa9.png width=500>

* Etapa 10: usando SparkSQL obter a quantidade de pessoas para cada país da geração Z:

<img src= ../Evidências/ativ2_etapa10.png width=500>