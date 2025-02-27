# Sprint 05
## Desafios:
&nbsp;&nbsp;&nbsp; Após a finalização dos curso havia o desafio para ser realizado. Ele consistia em manipulação de dados no S3 Select. 

&nbsp;&nbsp;&nbsp; Os dados manipulados deviam ser conseguidos na página de dados abertos do governo e esses dados deveriam diferenciar de todos os colegas. A tabela que escolhi é sobre os cursos técnicos que existem no Brasil em 2023, essa tabela apresenta desde a região que a escola reside até o número de matrículas que existem em cada curso. A tabela de dados que escolhi está no diretório Tableas_Consulta, que está em 2.Evidências, e tem o nome de [escolas_tecnicas_2023.csv](https://github.com/rehbeinp/EstagioC_UOL/tree/main/Sprint05/Evid%C3%AAncias/escolas_tecnicas_2023.csv).

&nbsp;&nbsp;&nbsp; No desafio deveriam ser realizadas o menor número de querys possível e atender aos requisitos tendo ao menos:
* 2 parâmetros lógicos;
* 1 função condicional;
* 1 função de converção;
* 1 função de string;
* 2 funções de agregação;
* 1 função de data.

&nbsp;&nbsp;&nbsp; Assim realizei duas querys, uma com parâmetros lógicos, função condicional, função de converção e função de string e outra com as funções de agregação. 

&nbsp;&nbsp;&nbsp; A [primeira query](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/desafio01.py):
- Converti o ano '2023', que estava em string, para tipo data deixando-o '2023-01-01'.
- Realizei o upper na região que as escolas residem, deixando tudo em caixa alta.
- Selecionei o nome da entidade, área do curso e nome curso profissionalizante em que a área do curso fosse de Informação e comunicação ou de Gestão e negócios mas não fossem de Infraestrutura, isso usando parâmetros lógicos.
- Coloquei uma condição de mudar o tipo da informação na localidade (TP_LOCALIZACAO) colocando ao invés de números '1' e '2', os correspondentes que é urbana e rural (de acordo com o manual dos dados disponibilizado).
- Converti a quantidade de matrículas por curso técnico de string para inteiro.

Resultado: [results_desafio01.csv](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/results_desafio01.csv)

<img src=../Evidências/img_desafio01.png width=600>

&nbsp;&nbsp;&nbsp; O código que usei nas consultas, nomeado de [desafio01.py](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/desafio01.py) , está na pasta Códigos que está no diretório Evidências. E o resultado, nomeado  [results_desafio01.csv](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/results_desafio01.csv) está na pasta Resultados, que está na pasta Evidências.

&nbsp;&nbsp;&nbsp; Na [segunda query](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/desafio02.py):

- Utilizei o min selecionando o menor número de matrículas que ocorreu em 2023 em algum curso.
- Utilizei o max selecionando o maior número de matrículas que ocorreu em 2023 em algum curso.
- Utilizei o sum que resultou no total de cursos que teve em 2023.
- Utilizei o sum que resultou no total de mátriculas que teve em 2023.
- Utilizei o sum que resultou no total de mátriculas e no total de cursos técnicos e dividi, conseguindo a média de matrículas por curos técnico que teve me 2023.

Resultado: [results_desafio02.csv](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/results_desafio02.csv)

<img src=../Evidências/img_desafio02.png width=600>

&nbsp;&nbsp;&nbsp; O código que usei nas consultas, nomeado de [desafio02.py](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/desafio02.py), está na pasta Códigos que está no diretório Evidências. E o resultado, nomeado [results_desafio02.csv](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint05/Evid%C3%AAncias/results_desafio02.csv), está na pasta Resultados que está na pasta Evidências. 

&nbsp;&nbsp;&nbsp; Não foi possível realizar a função de data pois os dados com informações sobre o ano estavam em tipo string, realizei a converção para tipo data, mas o S3 Select, por ser um pouco limitado, não permite a utilização de colunas criadas na consulta, só permite a utilização de colunas que ja estão na tabela, me impedindo de usar a função de data.

## Difuculdades:
&nbsp;&nbsp;&nbsp; Pelo S3 Select ser um pouco limitado ocorreu algumas dificuldades na consulta. Ainda a maior parte das dificldade foi na conexão do S3 ao console, para serem realizadas as consultas em script Python.