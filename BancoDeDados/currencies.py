import pandas as pd

# Função para obter os dados (substitua pela sua fonte de dados)
def obter_dados(arquivo_csv):
    df = pd.read_csv(arquivo_csv, index_col='Data', parse_dates=True)
    return df

# Carrega os dados (substitua pelo caminho do seu arquivo CSV)
df = obter_dados('taxas_de_cambio.csv')

# Seleciona o período desejado
df = df['2016-01-01':'2021-02-20']

# Calcula a média de cada moeda
media_moedas = df.mean()

# Imprime os resultados
print(media_moedas)