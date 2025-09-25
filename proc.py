import pandas as pd

df_base = pd.read_csv('Status/Baseex (2).csv', encoding='cp1252', sep=',', index_col=False)

df_stats = pd.read_csv('Status/COD STATUS.csv', encoding='cp1252', sep=',', index_col=False)

Desc = dict(zip(df_stats['Código '], df_stats['Descrição do Ultimo Status']))

df_base['Descrição do status'] = df_base['Cód. do Status da encomenda'].map(Desc)

df_base['Data do Último Status'] = pd.to_datetime(df_base['Data do Último Status'], dayfirst=True)

df_base['Data'] = df_base['Data do Último Status'].dt.date

df_base['Hora'] = df_base['Data do Último Status'].dt.time

df_base = df_base.drop(df_base.columns[5], axis=1)

df_base['Rota'] = df_base['Rota'].str.split('-').str[1]

df_base['Número do SEDEX'] = df_base['Número do SEDEX'].fillna('-').apply(lambda x: "Correios" if x != '-' else x)

df_base.rename(columns={'Cód. do Status da encomenda': 'Código'}, inplace=True)

df_base = df_base.sort_values('Nome Fantasia do Cliente').reset_index(drop=True)

df_base.to_csv('Base tratada!.csv', encoding='cp1252', sep=',', index=False)


print(df_base.head(50))