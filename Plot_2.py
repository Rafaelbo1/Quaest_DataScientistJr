import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabela import contingency_tables as ct

# Careegando os dados em um data frame
df = pd.read_excel('bd_surveyquaest.xlsx', sheet_name='Sheet 1')
table, x, y = ct(df)
table = table.T
#Ordenar pela soma
table['sum'] = table.sum(axis=1)
data = table.sort_values(by= 'sum', ascending=False)

#Agrupar candidatos com menos votos e ordenar pelo índice
data_table = data.iloc[:8]
data_table.loc['Demais Candidatos 111'] = data[8:].sum()
table_data = data_table.reindex(sorted(data_table.index,key=lambda x: x[-2:]), axis=0).iloc[:,:-1]

#Nome das colunas e dos índices para o plot
categ = table_data .index.tolist()
rows = table_data .columns.tolist()

# Cores para as barras e dimensões das barras e tabelas
colors = plt.cm.Set3(np.linspace(0, 0.75, len(categ)))
n_rows = len(table_data)
index = np.arange(len(rows)) + 0.3
bar_width = 0.90

# Configuração das barras
but = np.zeros(len(rows))
#Texto de numeros em % para a tabela de contigência
cell_text =[]
#Plot do gráfico de barras
sum_total = table_data.sum()
h = np.zeros(len(rows))
for row in range(n_rows):
    bars = plt.bar(rows, table_data.iloc[row],  bar_width, bottom=but, color=colors[row])
    but += table_data.iloc[row]
    cell_str = table_data.iloc[row] * 100 /sum_total
    cell_text.append(["{0:.2f}%".format(x) for x in cell_str])

#Plot do topo da barra
for r, rect in enumerate(bars):
    plt.text(rect.get_x() + rect.get_width() / 2.0, sum_total.iloc[r],
             '%d votos' % (sum_total.iloc[r]), ha='center', va='bottom')

# Plot das tabelas
the_table = plt.table(cellText=cell_text,
                      rowLabels=categ,
                      rowColours=colors,
                      colLabels=rows,
                      loc='bottom')

# Tamanho das letras da tabela
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)

# Plot
plt.subplots_adjust(left=0.3, bottom=0.3)
plt.ylabel('Quant. {}'.format(y))
plt.xticks([])
plt.title('Relação entre {} e {}'.format(x,y))
plt.show()
