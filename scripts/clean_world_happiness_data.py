import pandas as pd

data = pd.read_excel('./data/raw/world_happiness_report.xlsx')

data_cleaned = data[data['Year'] >= 2019]

data_cleaned.to_csv('./data/processed/world_happiness_report_cleaned.csv', index=False)


print(data_cleaned.shape)
print(data_cleaned.duplicated(['Year', 'Country name']).sum())
print(data_cleaned.isna().sum())
