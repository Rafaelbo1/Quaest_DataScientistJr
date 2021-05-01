import pandas as pd
from collections import Counter

# Função para automatizar a construção de tabelas de contingência
def contingency_tables(df):
    columns_names = df.columns.tolist()
    # input para a esolha das variáveis a serem analizadas
    try:
        x, y = input('\n''Variáveis:{}''\n'
                 '\n''DIGITE O NOME DE DUAS VARIÁVEIS OU ENTER PARA DEFAULT(sexo, voto1)'
                 '\n''(não digite aspas e use apenas espaço para separar as variáveis desejadas)'
                 '\n''R: ' .format(columns_names)).split()
    except ValueError:
        x = 'sexo'
        y = 'voto1'
    # x,y = 'sexo', 'voto1'

    # usando pandas crosstab
    data_crosstab = pd.crosstab(df[x], df[y], margins=False)

    # usando usando pandas groupby, size() e unstack()
    # Até 3 vezes mais rápido que o pandas
    # crosstab
    dg = df.groupby([x, y]).size().unstack().fillna(0)
    #ordenar a tabela pelo nome do candidato
    data_groupby = dg.reindex(sorted(dg.columns,key=lambda x: x[-2:]), axis=1)

    # Usa collections.Counter() e zip()
    # Cerca de 9 vezes mais rápido que o pandas groupby
    data_counter = Counter(zip(df[x], df[y]))

    # retorna uma tabela ou um contador  de contingência
    return data_groupby, x, y



# Driver Function(teste da função) e print da tablela de contingência
if __name__ == "__main__":
    # Careegando os dados em um data frame
    df = pd.read_excel('bd_surveyquaest.xlsx', sheet_name='Sheet 1')
    # Analizando as váriáveis da tabela
    print(df.head(10))
    df.describe()
    df.info()

    table,_,_ = contingency_tables(df)
    print(table)