# Informações do Teste - Quaest, Data Scientist Jr. 

A base de dados foi tratada com os nomes das variáveis e das categorias originais. As variáveis são:
 - sbjnum: id do respondente
 - sexo: sexo do respondente
 - idade: idade (numérica) do respondente
 - rendaf: renda familiar do respondente
 - esc: escolaridade do respondente
 - aval_gov: avaliação do governo
 - voto1: intenção de voto do respondente.

A partir da base de dados, foram desenvolvidas as atividades com a descrição do "passo a passo" nos scripts dos códigos de cada demanda. 
- Para o carregamento da base de dados no formato enviado (bd_surveyquaest.xlsx), foi usada uma função do pandas read_excel() junto com a biblioteca xlrd --versão 1.2.0 - única adequada à leitura do tipo de arquivo .xlsx (poderia converter para .csv, mas optei por seguir com o formato original)

 1. Crie uma função em alguma linguagem de programação, preferencialmente em R ou Python,  que automatize a construção de tabelas de contingência. O objetivo é identificar se há uma diferença sociodemográfica na intenção de voto. Em outras palavras, por ex.: As mulheres e os homens estão votando no mesmo candidato ? 
	
	- Para esta atividade, disponibilizei um conjunto de bibliotecas/funções naturais de Python que contribuem para o desenvolvimento do que foi solicitado -
	  criar uma função que automatize a construção de tabelas de contingência.
	  
	- A função criada contém, em seu início, linhas para input das variáveis que o usuário desejar ver na tabela de contigência
	  (uma lista com os nomes das variáveis é apresentada ao executar o script). O script pode se executado em modo defalut com as variáveis 'sexo' e 'voto1',
	  basta que o usuário pressione enter quando for solicitado preencher a resposta requerida na execução do código.
	  
	- Assim, temos uma função onde é possível construir uma tabela com as bibliotecas pandas crosstab(), pandas groupby com size() e unstack() ou
	  collections.Counter() e zip(). Como descrito no script, esta última foi a que construiu a tabela mais rápido e com menos processamento, porém,
	  optei em usar o pandas groupby com size() e unstack() para cumprir o prazo de entrega (ver o return da função no script).
	  
	- O teste da função é feito dentro do próprio script com a base de dados carregada - Basta executar tabela.py e será visto um print da tabela de contigência criada.
	
	TABELA DE CONTIGÊNCIA - PRINT
	
	![Test Image 1](https://github.com/Rafaelbo1/Quaest_DataScientistJr/blob/master/image/Tabela%20de%20contingencia.png)


	TABELA DE CONTIGÊNCIA - DEBUG
	![Test Image 2](https://github.com/Rafaelbo1/Quaest_DataScientistJr/blob/master/image/Tabela%20de%20contingencia-debug.png)

2. Ainda com essa base de dados, construa dois gráficos. 

      2.1) O primeiro gráfico será da variável intenção de voto.
      
 	- O script desta atividade é o plot_1.py
 	
 	- Basta executar para visualizar o plot do gráfico da variável intenção de voto e suas categorias.
 	
 	- Pra este gráfico foi usada uma função simples da biblioteca pandas e matplotlib.

	![Test Image 3](https://github.com/Rafaelbo1/Quaest_DataScientistJr/blob/master/image/Variavel%20voto1.png)
 
      2.2) Já o segundo, plot um gráfico que represente o cruzamento entre as variáveis intenção de voto e avaliação do governo. Quem avalia o governo de forma
 	   positiva, vota em qual candidato ? E quem avalia de forma negativa ?

	- O script desta atividade é o plot_2.py
	
	- Este script foi usado em conjunto com função contingency_tables() do script tabela.py (pelo import: "from tabela import: 				contingency_tables as ct")
	
	- Novamente as variáveis desejadas para o cruzamento podem ser selecionadas(lembrando que o default são as variáveis 'sexo' e 'voto1')
	
	- Temos, descritas no código, as configurações para o plot do gráfico de barras juntamente com uma tabela de contingência para melhor visualização da informação
	
	- Se as variáveis aval_gov e voto1 forem selecionadas, temos:
		* Barras com o total de votos por categoria de aval_gov
		* Cada barra está dividida em cores que representam a quantidade de votos que cada candidato tem para cada categoria de aval_gov.
		* Foi feito um agrupamento dos candidatos com quantidade de votos muito baixa. Esse dado foi adicionada em uma nova variável chamada de Demais Candidatos 111.
		* Houve dúvida quanto às categorias Regular Positivo e Regualar Negativo, é possível agrupar em uma única coluna (Regular),
		  porém como não conheço em detalhe essa informação optei por manter ambas.
		* Na tabela, temos a percentagem de votos que cada candiato tem para cada categoria. Assim é possível identificar, por exemplo:
		  A maioria dos que dão uma avaliação BOA para o governo votam no CANDITADO 2 - 67,72%.
		
		
	![Test Image 4](https://github.com/Rafaelbo1/Quaest_DataScientistJr/blob/master/image/Variaveis%20aval_gov%20e%20voto1.png)
	
	
	- No mesmo script, para a seleção das variáveis sexo e voto1 temos:
		* Barras com o total de votos por categoria de sexo
		* Cada barra está dividida em cores que representam a quantidade de votos que cada candidato tem para cada categoria de sexo.
		* Foi feito um agrupamento dos candidatos com quantidade de votos muito baixa. Esse dado foi adicionada em uma nova variável chamada de Demais Candidatos 111.
		* Na tabela, tem-se a percentagem de votos que cada candiato tem para cada categoria. Assim é possível identificar, por exemplo:
		* A maioria do eleitorado do sexo FEMININO votam no CANDITADO 2 - 54,13%.


	![Test Image 5](https://github.com/Rafaelbo1/Quaest_DataScientistJr/blob/master/image/Variaveis%20sexo%20e%20voto1.png)


Obs: Os códigos foram desenvolvidos usando bibliotecas instaladas em um ambiente virtual, como recomendam as melhores práticas.
     Segue, o requirements.txt. Caso o usuário queira utlizar para instalação de todas as bibliotecas usada. Basta executar na linha de comando:
     pip install -r requirements.txt



