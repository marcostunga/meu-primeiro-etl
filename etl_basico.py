# Meu Primeiro ETL - Data Engineer Júnior
# Marcos - 12/08/2026

import pandas as pd

print("Olá, meu pipeline está funcionando!")

# 1. EXTRACT - Extrair dados
dados = {
    'produto': ['Mouse', 'Teclado', 'Monitor'],
    'vendas': [50, 30, 10],
    'preco': [100, 200, 1200]
}

df = pd.DataFrame(dados)
print("\nDados Extraídos:")
print(df)

# 2. TRANSFORM - Transformar dados
df['faturamento'] = df['vendas'] * df['preco']
print("\nDados Transformados:")
print(df)

# 3. LOAD - Carregar dados
df.to_csv('vendas_processadas.csv', index=False)
print("\nArquivo 'vendas_processadas.csv' criado com sucesso!")
