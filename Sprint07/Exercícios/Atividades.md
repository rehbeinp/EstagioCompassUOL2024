# Sprint 07:
## Atividades:
&nbsp;&nbsp;&nbsp; Haviam duas ativiades para serem realizadas, uma no console do AWS Glues e outra sobre Spark.

### Spark:
&nbsp;&nbsp;&nbsp; Na atividade de Spark era necessário contar as palavras do readme presente no git atravéz de comandos Spark. Isso devia ser realizado em um container, cuja a imagem foi disponibilizada. <p>
&nbsp;&nbsp;&nbsp; Assim após um pull da imagem jupyter/all-spark-notebook, executei um container docker com o modo interativo e iniciando o shell do container (infelizmente esqueci de tirar print). Com o terminal iniciado, baixei o arquivo README.md do meu git com o comando wget e inicializei o pyspark.<p>
&nbsp;&nbsp;&nbsp; No terminal spark realizei as importações e o inicio da sessão. Assim comecei uma aplicação e fiz os [comandos necessários para contar as palavras](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/spark_comandos.txt) do README.md e salvei o resultado gerado pelos comando na minha máquina. Resultando no arquivo [contagem_palavras](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/spark_contagem_palavras_readme).

### AWS Glue:
&nbsp;&nbsp;&nbsp; Na atividade de AWS Glue foram seguidos os passos disponibilizados, sendo inicialmente criado um usuário com as permissões no Glue. Após foi criado uma regra do IAM, que dá acesso ao S3, para ser agregada nos jobs do Glue. Então foi configurado permissões do AWS Lake Formation para facilitar a criação e gerenciamento de data lakes. Por fim foi criado um job no glue, esse job tinha como dados de entrada o bucket S3 com os dados nomes.csv e como saida o bucket de destino do S3. <p>
&nbsp;&nbsp;&nbsp; Com o job criado era necessário fazer algumas execuções, sendo elas:
* Ler o arquivo nomes.csv no S3([codigo 1](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/1codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_leitura_arquivo_nomes.csv)).
* Imprimir o schema do dataframe gerado no passo anterior ([codigo 2](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/2codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_schema_dataframe.json)).
* Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO, e levar o resultado para o S3, com formato json e particionamento por ano e sexo.([codigo 3](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/3codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_nome_maiusculo)).
* Imprimir a contagem de linhas presentes no dataframe ( [codigo 4](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/4codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_total_linhas.json)).
* Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe ([codigo 5](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/5codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_contagem_nome_por_ano)).
* Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu ([código 6](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/6codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_nome_feminino_mais_usado)).
* Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu ([código 7](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/7codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_nome_masculino_mais_usado)).
* Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe ([código](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/8codigoglue.py), [resultado](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/codigoglue_total_registro_por_ano_e_genero)).

&nbsp;&nbsp;&nbsp; Após realizar esses jobs no AWS Glue era preciso criar um novo Crawler que criou automaticamente uma tabela chamada
frequencia_registro_nomes_eua com os nomes maiúsculos. Com a execução for bem sucedida era possível ver a nova tabela
frequencia_registro_nomes_eua por meio do Athena. Para consulta-la era preciso conceder privilégios de DESCRIBE e SELECT no LakeFormation. Após conceder esses privilégios realizei as seguintes consultas com linguagem SQL no AWS Athena:
* [Ano e gênero com maior quantidade de nomes diferentes registrados.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_ano_genero_com_maior_quant_registros_diferentes.csv)
* [Ano e gênero com maior quantidade de registros.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_ano_genero_maior_quant_registros.csv)
* [Top 5 anos com maior quantidade de nomes diferentes registrados.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_ano_maior_quant_nome_diferentes_registrados.csv)
* [Top 5 anos com maior quantidade de registros.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_ano_maior_quant_registros.csv)
* [Quantidade de nomes diferentes registrados.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_contagem_nomes.csv)
* [Top 10 nomes femininos mais registrados em 2002.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_fem_mais_registrados_2002.csv)
* [Top 10 nomes masculinos mais registrados em 2002.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_masc_mais_registrados_2002.csv)
* [Quantidade, por gênero, de nomes diferentes registrados.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_quant_nome_diferente_por_genero_regsitrado.csv)
* [Quantidade total de registros femininos e masculinos.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_quant_total_registros_fem_masc.csv)
* [Total, por gênero, de nomes diferentes registrados em 2002.](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint07/Evid%C3%AAncias/athena_total_nomes_diferentes_registrados_em_2002.csv)

