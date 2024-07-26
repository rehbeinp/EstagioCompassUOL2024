 # Sprint 01 
## Desafios:
&nbsp;&nbsp;&nbsp;Após finalizar os cursos havia dois desafios para serem feitos. Um sobre criar uma conta no GitHub, adicionar um diretório do estágio, e criar repositórios no projeto adicionando a eles os conteúdos vistos ao longo das Sprints. <p>
&nbsp;&nbsp;&nbsp; E o outro desafio, agora sobre Linux, era sobre criar dois Scripts executáveis, um que executa com agendamento (de segunda a quinta, as 15h27m) e o outro manualmente. 
<p>
<p>

### Desafio Linux:
&nbsp;&nbsp;&nbsp;O Script que executa com agendamento tem o nome processamento_de_dados.sh. Ele gera dois diretórios, um chamado _vendas_ e o outro _backup_ (_bakcup_ gerado dentro de _vendas_). Copia o arquivo **dados_de_vendas.csv** de outro diretório, chamado _ecommerce_, para o diretório _vendas_ e para o diretório _backup_. Em _backup_, copia **dados_de_vendas.csv** para o arquivo criado **dados-de-vendas-yyyy/mm/dd.csv** e renomeia **dados-de-vendas-yyyy/mm/dd.csv** para **backup-dados-de-vendas-yyyy/mm/dd.csv**. <p>
&nbsp;&nbsp;&nbsp;Depois de toda esse estruturação ele gera um arquivo **relatorio.txt** (criado dentro de _backup_) que contém infomações expecíficas, como a data e hora que as informações foram geradas, data da primeira e da ultima compra, contidas no arquivo **backup-dados-de-vendas-yyyy/mm/dd.csv**, qual a quantidade total de itens vendidos, e os dez primeiros itens do arquivo **backup-dados-de-vendas-yyyy/mm/dd.csv**. Após terminar de gerar o arquivo **relatorio.txt**, o script campacta **backup-dados-de-vendas-yyyy/mm/dd.csv** e o apaga (o arquivo não compactado). Apaga também o aquivo **dados_de_vendas.csv** de _vendas_. <p>
&nbsp;&nbsp;&nbsp;Script de processamento_de_vendas.sh e terminal com três relatórios criados:
<p>
<img src=../imgs/Script_processamento_de_vendas.png width=300>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   <img src=../imgs/antes_de_gerar_relatorio_fina.png width=350>
<p>

&nbsp;&nbsp;&nbsp; O  [arquivo processamento_de_vendas.sh](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint01/Evid%C3%AAncias/processamento_de_vendas.sh) se encontra na pasta 2.Evidências.

<p>

&nbsp;&nbsp;&nbsp; O Script sem agendamento, consolidador_de_processamento_de_vendas.sh, tem a ordem de criar um arquivo chamado **relatorio_fina.txt** e adicionar nele, a cada três execuções de processamento_de_dados.sh, os dados gerados no arquivo **relatorio.txt**. 
<p>

&nbsp;&nbsp;&nbsp;Script de consolidador_processamento_de_vendas.sh e terminal após gerar o relatório final:
<p>

<img src=../../imgs/Script_consolidador_de_processamento_de_vendas.png width=350> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src=../../imgs/gerando_relatorio_fina.png width=300>
<p>

&nbsp;&nbsp;&nbsp; O arquivo  [consolidador_processamento_de_vendas.sh](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint01/Evid%C3%AAncias/consolidador_de_processamento_de_vendas.sh) se encontra na pasta 2.Evidências.

<p>
<p>

&nbsp;&nbsp;&nbsp;Visualização de parte do relatório final no terminal:
<p>

<img src=../../imgs/cat-de-relatorio_fina.png width=350>
<p>

&nbsp;&nbsp;&nbsp; O arquivo  [relatório_fina.txt](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint01/Evid%C3%AAncias/relatorio_fina.txt) se encontra na pasta 2.Evidências.
<p>

## Dificuldades durante as atividades
&nbsp;&nbsp;&nbsp;Ao longo das atividades propostas pela Sprint 01 foram surgindo desafios e problemas, principalmente durante a segunda atividade, relacionada a linux.
<p>

### Alguns dos problemas da atividade de Linux
&nbsp;&nbsp;&nbsp;Um dos principais problemas foram relacionadas com diretórios, onde o script tentava criar um diretório, que ja existia (*vendas* ou *backup*). Outro empencilho foi a seleção de conteúdos expecíficos (data da primeira e ultima compra) dos arquivos (**backup-dados-de-vendas-yyyy/mm/dd.csv** por exemplo). Além de outras difuculdades mais simples, que com um pouco de pesquisa foram resolvidas. <p>

### Solução dos principais problemas
&nbsp;&nbsp;&nbsp;O caso dos diretórios existentes foi resovido com a implementação do comando _if_. Esse comando impede que um diretório seja criado novamente, caso já exista, passando o processsamento para a próxima etapa. <p>
&nbsp;&nbsp;&nbsp; Já o segundo caso, onde haveriam de ser selecionadas as datas da primeira e última compra. Como não foi encontrado uma ferramenta totalmente expecífica para solucioná-lo, ocorreu a necessidade de criar um arquivo **reserva.txt** onde foi selecionado com head, as primeiras linhas do arquivos **backup-dados-de-vendas-yyyy/mm/dd.csv**, e com o tail foi selecionada a última linha, subsequentemente foi selecionada do **reserva.txt** a quinta coluna (onde estavam as datas), e após isso, finalmente foram passadas as datas necessárias, novamente com tail selecionando as duas últimas linhas de **reserva.txt** para o arquivo **relatorio.txt**. Por fim, ocorreu a remoção de **reserva.txt** que foi usado apenas como ferramenta. <p>