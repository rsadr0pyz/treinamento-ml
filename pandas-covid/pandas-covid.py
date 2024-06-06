import pandas as pd


covid_data = pd.read_csv("covid.csv",sep=',', encoding="latin-1")

# Filter by number of cases
cities_data = covid_data.groupby("Municipios").sum(numeric_only=True)

print(cities_data.loc[['VITORIA', 'VENDA NOVA DO IMIGRANTE']])