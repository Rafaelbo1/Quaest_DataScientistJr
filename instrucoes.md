# Avaliação técnica — Quaest, Data Scientist Jr. 

A base de dados foi tratada com os nomes originais com as seguintes variáveis e suas respectivas categorias.
 - sbjnum: id do respondente
 - sexo: sexo do respondente
 - idade: idade (numérica) do respondente
 - rendaf: renda familiar do respondente
 - esc: escolaridade do respondente
 - aval_gov: avaliação do governo
 - voto1: intenção de voto do respondente.

A partir da base de dados, foram desenvolvidas as atividades com a descrição do "passo a passo" nos scripts dos códigos de cada demanda. 
- Para o carregamento da base de dados no formato enviado, foi usada função do pandas read_excel() junto com xlrd na versão 1.2.0 - única adequada à leitura do tipo de arquivo .xlsx

 1. Crie uma função em alguma linguagem de programação, preferencialmente em R ou Python,  que automatize a construção de tabelas de contingência. O objetivo é identificar se há uma diferença sociodemográfica na intenção de voto. Em outras palavras, por ex.: As mulheres e os homens estão votando no mesmo candidato ? 
	
	- Para esta atividade, disponibilizei um conjunto de bibliotecas/funções naturais de Python que fazem o que foi solicitado - criar uma função que automatize a construção de tabelas de contingência.
	- A função criada contém em seu início linhas para input das variáveis que o usuário desejar ver na tabela de contigência (uma lista com os nomes das variáveis é disponibilizada). O script pode "rodar" em modo defalut com as variáveis 'sexo' e 'voto1', basta que o usuário pressione enter quando for solicitado preencher a resposta requerida na execução do código tabela.

	- Assim temos uma função que pode contruir uma tabela com pandas crosstab(), pandas groupby com size() e unstack() ou collections.Counter() e zip(). Como descrito no script, esta última foi a que contruiu a tabela, mais rápido e com menos processamento, porém, optei em usar o pandas groupby com size() e unstack() para cumprir o prazo de entrega.
	
	- O teste da função é feito dentro do próprio script com a base de dados disponiblizada - Basta executar tabela.py e será visto um print da tabela de contigência criada.

 2. Ainda com essa base de dados, construa dois gráficos.
 3. 
 4. 2.1. O primeiro gráfico será da variável intenção de voto.
 		- O script desta atividade é o plot_1.py
 		- Basta executar para plotar o gráfico da variável intenção de voto e suas categorias.
 		- Pra este gráfico foi usada uma função simples da biblioteca pandas e matplotlib.
    2.2. Já o segundo, plot um gráfico que represente o cruzamento entre as variáveis intenção de voto e avaliação do governo. Quem avalia o governo de forma
           positiva, vota em qual candidato ? E quem avalia de forma negativa ?
		- O script desta atividade é o plot_2.py
		- Este script, pelo nível da demanda, foi usada em conjunto com função contingency_tables() do script tabela.py - pelo import: "from tabela import: 				contingency_tables as ct"
		- Novamente as variáveis desejadas para o cruzamento podem ser selecionadas(lembrando que o default são as variáveis 'sexo' e 'voto1')
		- Temos, então, as configurações descritas no código para o plot de um gráfico de barras juntamente com uma tabela de contingência complementado a informação
		- 
		- Se as variáveis aval_gov e voto1 forem selecionadas, temos:
			* Barras com o total de votos por categoria de aval_gov
			* Cada barra está dividida em cores que representam a quantidade de votos que cada candidato tem para cada categoria de aval_gov.
			* Na tabela, temos a percentagem de votos que cada candiato tem para cada categoria. Assim é possível identificar, por exemplo: A maioria dos que dão uma avaliação BOA para o governo votam no CANDITADO 2 - 67,72%.
		-
		-
		- No mesmo script, para as variáveis sexo e voto1 temos:
			* Barras com o total de votos por categoria de sexo
			* Cada barra está dividida em cores que representam a quantidade de votos que cada candidato tem para cada categoria de sexo.
			* Na tabela, tem-se a percentagem de votos que cada candiato tem para cada categoria. Assim é possível identificar, por exemplo: A maioria do eleitorado do sexo FEMININO votam no CANDITADO 2 - 54,13%.




Obs: Os códigos foram inscritos usando bibliotecas instaladas em um ambiente virtual, como recomendam as melhores práticas.
     Segue, o requirements.txt. Caso o usuário queira utlizar para instalação de todas as bibliotecas usada, basta executar na linha de comando: pip install -r requirements.txt



