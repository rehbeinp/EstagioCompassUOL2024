# Sprint 10
## Desafio final - Parte 05
&nbsp;&nbsp;&nbsp; O desafio foi formado pela formação de Dashboards que respondessem ou falassem sobre o assunto definido para análise.


###  [Idade, Gênero e Participação dos Artistas em Filmes de Fantasia Sci-Fi e Categorias de Destaque](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint10/Evid%C3%AAncias/Idade%20Genero%20e%20Participa%C3%A7%C3%A3o%20dos%20Artistas%20em%20Filmes%20de%20Fantasia%20Sci-Fi%20e%20Categorias%20de%20Destaque.pdf): 


&nbsp;&nbsp;&nbsp; O assunto de análise definido na Sprint 06 mudou ao longo das Sprints, sendo formado no fim por duas perguntas que se complementam. Os gráficos respondem mais que as perguntas definidas, dei uma atenção também aos temas definidos por Squad, Fantasia e Ficção Científica no meu caso, fazendo uma breve análise que tem relação com as perguntas defidas. Ambas as perguntas e os insigths conseguidos a partir do Dashboard são:
#### Que idade os atores e atrizes tem quando fazem filmes bem avaliados? Com quais gêneros que eles se destacaram com essa idade?

* É perceptível na análise que existe diferença de idade entre homens e mulheres e existe diferença entre as categorias de filmes que eles se destacam.
* Os homens em todas as categorias são mais velhos que as mulheres, que varia de 10 a 3 anos a mais que elas.
* A categoria que os artistas em geral tem uma idade mais avançada é Documentário, a que eles têm uma idade mais jovem é no Romance. 
* Em todas as categorias os homens são mais númerosos que as mulheres, inclusive em Fantasia e Ficção Científica.
* Em Documentário é uma das categorias que menos tem mulheres no elenco, o que pode ser atribuído a quando o elenco precisa de artistas mais velhos as mulheres são ainda menos contratadas que os homens. Ou ainda, as mulheres não são escolhidas para gêneros que são considerados masculinos.
* Em Romance as mulheres tem a porcentagem de contratação maior comparada com as outras categorias, e é a categoria que também possui as mulheres mais jovens em comparação com os outros gêneros de filmes. Ou seja, quando há necessidade de um elenco mais jovem as mulheres não são tão excluídas como nos elencos mais velhos. A participação das atrizes também pode ser pelo Romance ser considerado uma categoria feminina, tendo assim mais espaço para as atrizes.
*  As categorias com maior nota média por participação feminina são semelhantes as categorias com maior nota média por participação masculina, como esporte, biografia e crime, em ambas essas categorias as mulheres tem uma nota média maior que os homens. Ainda nessa mesma análise a maior idade média feminina é igual a menor idade média masculina. 
* Ainda, em Esporte as mulheres tem a idade média menor e os homens a idade média maior. As mulheres também tem apenas 5% de participação nessa categoria. A idade jovem e a pouca participação das mulheres pode ser pela categoria esporte ser considerada masculina, e assim apenas mulheres que formassem um atrativo maior aos homens seriam escolhidas para participar, como mulheres jovens. Isso apesar das mulheres apresentarem um número melhor de avaliação em comparação com os homens no esporte. 


#### A idade que os atores e atrizes fazem filmes bem avaliados muda ao longo dos séculos?
* De acordo com a análise, a idade dos artistas aumenta ao longo dos séculos. Isso pode ser atribuído ao aumento da longevidade de vida que melhora com o tempo. 
* É notavel que as mulheres sempre são mais jovens que os homens na história do cinema. Também é apenas a partir dos anos 2000 que elas ficam acima da idade média geral, enquanto os homens apenas alcançam a marca nos anos 1910 e 1930, estando em todos os outros séculos sempre acima da idade média geral. 

####  Comparação entre Fantasia e Ficção Científica:
* Os filmes de fantasia são mais númerosos e mais bem avaliados que os de Ficção Científica. 
* Os artistas de Fantasia também tem uma idade mais variada, de aproximadamente 20 a 75 anos, que os de Ficção Científica, que tem entre 20 a menos de 50 anos.

## Gráficos:
&nbsp;&nbsp;&nbsp; Os gráficos e o DashBoard foram desenvolvidos no QuickSight. Os filtros, agrupamentos e colunas escolhidas estão disponíveis abaixo.
* Idade que Atores/Atrizes Fazem Filmes de Sucesso ao Longo dos Séculos:
Nesse Gráfico eu fiz a média das idades dos atores e atrizes ao longo dos séculos.

<img src= ../Evidências/idade_seculos_quick.png width=250>  <img src= ../Evidências/idade_ao_logo_dos_seculos.png width=300>  

* Média de idade dos Artistas por Categoria de Filme (Considerando as 10 Principais Categorias de Filmes):
Fiz a média das idade por categoria, considerando as 10 categorias mais frequentes.

<img src= ../Evidências/idade_por_categoria_quick.png width=250>  <img src= ../Evidências/idade_categoria_filtro.png width=250>  <img src= ../Evidências/idade_media_por_categoria.png width=350> 

* Idade Média por Nota de Fantasia e Sci-Fi: Uma análise comparando a participação de artistas suas idade e as notas médias das categorias de Fantasia e Sci-Fi, categorias da Squad 04.

<img src= ../Evidências/dispersao_fantasia_scifi_quick.png width=250>  <img src= ../Evidências/filtro_partc_gen_fantasia_scifi.png width=250>  <img src= ../Evidências/nota_media_por_idade_em_fantasia_scifi.png width=400> 

* Categorias com Maior Nota Média por Participação Feminina: Ordenado por nota média e filtrado por gênero do artista.

<img src= ../Evidências/categorias_por_genero_mulheres.png width=250>  <img src= ../Evidências/categoria_por_genero_mulheres_filtro.png width=250>  <img src= ../Evidências/nota_media_partc_feminina.png width=350> 

* Categorias com Maior Nota Média por Participação Masculina:  Ordenado por nota média e filtrado por gênero do artista.

<img src= ../Evidências/categoria_por_genero_homens.png width=250>  <img src= ../Evidências/categoria_por_genero_homens_filtro.png width=250>  <img src= ../Evidências/nota_media_part_masculina.png width=350>

* Participação de Homens e Mulheres Por Categoria de Filme (Considerando as 3 Categorias com Nota Média Maior): Ordenada por nota média e filtrada por melhores 3.

<img src= ../Evidências/genero_maior_nota_media_quick_part_gene.png width=250>  <img src= ../Evidências/participacao_gen_cat_bem_avaliadas.png width=350>

* Participação de Homens e Mulheres em Fantasia e Sci-Fi: Filtrado pelas categorias Fantasia e Ficção Científica

<img src= ../Evidências/part_genero_fantasia_scifi_quick.png width=250>  <img src= ../Evidências/filtro_partc_gen_fantasia_scifi.png width=250>  <img src= ../Evidências/partc_gen_fantasia_scifi.png width=350>

* Participação de Homens e Mulheres por Categoria de Filme (Considerando as 10 Categorias Mais Frequentes de Filmes): Filtrado pelas 10 maiores categorias.

<img src= ../Evidências/categorias_mais_frequentes_participacao_genero.png width=250>  <img src= ../Evidências/categoria_frequenetes_part_gen_filtro.png width=250>  <img src= ../Evidências/Perticipacao_genero_cat_freq.png width=300>

* Insight Idade Média das Mulheres:

<img src= ../Evidências/insigth_quick.png width=250> <img src= ../Evidências/filtro_insight_mulheres.png width=250>  <img src= ../Evidências/insigth_mulheres.png width=500>

* Insight Idade Média das Homens:

<img src= ../Evidências/insigth_quick.png width=250> <img src= ../Evidências/filtro_insight_homens.png width=250>  <img src= ../Evidências/insigth_homens.png width=500> 

## Alteração na camada Refined:
&nbsp;&nbsp;&nbsp; Tive a necessidade de realizar uma alteração no código da Sprint 09. A alteração se dá por ter colocado uma linha que exclui um artista pelo seu id e ao executar o código novamente o id for redefinido, excluindo outro artista e deixando o errado. O artista excluido tem o ano de nascimento errado, o que o deixa com uma idade de mais de mil anos. Sem excluir esse artista tive que adicionar filtros para limitar a idade até 120 anos no QuickSigth. O [código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint10/Evid%C3%AAncias/glue_refined.py) foi alterado na linha 122.