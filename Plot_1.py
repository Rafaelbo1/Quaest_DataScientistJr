import pandas as pd
import matplotlib.pyplot as plt

# Careegando os dados em um data frame
df = pd.read_excel('bd_surveyquaest.xlsx', sheet_name='Sheet 1')
# Analizando as váriáveis da tabela
print(df.head(10))
df.describe()
df.info()

#Plot da da variável intenção de voto
plt.subplots_adjust(left=0.3, bottom=0.3)
votos = df.groupby('voto1').size().sort_values(ascending=False)
votos.plot(kind='bar')

#Identiifcando as barras com a quantidade de votos
for i in range(len(votos)):
    plt.text(i, votos.iloc[i], votos.iloc[i], ha='center', va='bottom')

#plot
plt.ylabel('Quant. voto1')
plt.title('Intenção de Voto por Candidato')
plt.show()


