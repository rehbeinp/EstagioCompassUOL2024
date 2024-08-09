# Sprint 04
## Desafios: 
&nbsp;&nbsp;&nbsp;O desafio sobre Docker foi dividido em três etapas, sendo a primeira e a terceira sobre criar uma imagem no docker e rodar um *container* a partir dela, e a segunda sobre reutilização de container.
### [Etapa 01](https://github.com/rehbeinp/EstagioC_UOL/tree/main/Sprint04/Evid%C3%AAncias):
&nbsp;&nbsp;&nbsp;Na primeira etapa foi disponibilizado um Script Python, chamado *[carguru.py](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint04/Evid%C3%AAncias/etapa1_carguru.py)* para a criação de uma imagem. Era necessário assim criar um documento *[Dockerfile](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint04/Evid%C3%AAncias/etapa1_Dockerfile)*, fazer o **build** da imagem e rodar um *container*. Ao rodá-lo era imprimido uma frase no console do tipo "Você deve dirigir um 'carro-tal-tal' ", onde carro-tal-tal mudava a cada execução. A baixo está o print do **build** da imagem nomeada *carguru* nas primeiras linhas, e o **run** de um container chamado *carros* com essa imagem *carguru* logo depois.

<img src= ..\..\Sprint04\Evidências\etapa1_build_carguru.png width=500>
<p>
&nbsp;&nbsp;&nbsp;O documento *Dockerfile* e o Script *carguru.py* utilizados nessa etapa estão no diretório "Evidências."

### Etapa 02:
&nbsp;&nbsp;&nbsp; Na segunda etapa era necessário responder se esse container chamado *carros* criado com a imagem *carguru* poderia ser reutilizado, e apresentar o comando para que isso fosse possível. <p>
&nbsp;&nbsp;&nbsp; Sim, *carros*, criado a partir de *carguru* pode ser reutilizado, mas para isso, por ser um *container interativo* ele precisa de um comando expecífico, sendo *docker start **-i** carros*, como mostra a imagem a baixo.

<img src= ..\..\Sprint04\Evidências\etapa2_reutilizar_container.png width=500>
<p>

### [Etapa 03](https://github.com/rehbeinp/EstagioC_UOL/tree/main/Sprint04/Evid%C3%AAncias/etapa03):
&nbsp;&nbsp;&nbsp; Na terceira etapa era necessário criar um Script Python que recebia uma *string* e devolvia um código *hash* por meio do algoritmo SHA-1, em uma impressão na tela por meio do *hexdigest*. Assim, criei um script chamado *[doc.py](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint04/Evid%C3%AAncias/etapa3_doc.py)* e um *[Dockerfile](https://github.com/rehbeinp/EstagioC_UOL/blob/main/Sprint04/Evid%C3%AAncias/etapa3_Dockerfile)* e gerei uma imagem, chamada *mascarar-dados* a partir de um **build**. E com *mascarar-dados* rodei o container *cripto* que gerou então o hash a partir da string fornecida. Execução na imagem a baixo. 

<img src= ..\..\Sprint04\Evidências\etapa03_mascarar_dados.png width=500>
<p>

&nbsp;&nbsp;&nbsp; Mais algumas execuções:

<img src= ..\..\Sprint04\Evidências\etapa03_mais_execucoes.png width=500>

&nbsp;&nbsp;&nbsp;O documento *Dockerfile* e o Script *doc.py* utilizados nessa etapa estão no diretório "Evidências."
