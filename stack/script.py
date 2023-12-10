import pandas as pd
import numpy as np

happy = pd.read_csv('data/happy.csv')
freedom = pd.read_csv('data/freedom.csv')
suicides = pd.read_csv('data/suicide.csv')

happy = happy.dropna()
happy = happy.drop(columns=['Regional Indicator', 'Log GDP Per Capita', 'Healthy Life Expectancy At Birth', 'Generosity'])

freedom = freedom.drop(columns=[col for col in freedom.columns if len(col) == 2 or len(col) == 1])
freedom = freedom.drop(columns=["Add Q", "Add A", 'C/T', 'Status', 'Region'])

suicides = suicides.drop(columns=['country-year', 'HDI for year'])
suicides = suicides.drop(columns=[col for col in suicides.columns if "gdp" in col])

merged_df = pd.merge(happy, freedom, on=['Country', 'Year'], how='inner')
merged_df = pd.merge(merged_df, suicides, on=['Country', 'Year'], how='inner')

merged_df = merged_df.rename(columns={'Total': 'Total freedom'})

df = merged_df.copy()
df['weighted_suicides'] = df['suicides/100k pop'] * df['population']
    
grouped = df.groupby(['Country', 'Year'])
aggregated_data = grouped.agg({
    'population': 'sum',
    'suicides_no': 'sum',
    'Life Ladder': 'first',  # Assuming these values are constant for each group
    'Social Support': 'first',
    'Freedom To Make Life Choices': 'first',
    'Perceptions Of Corruption': 'first',
    'Positive Affect': 'first',
    'Negative Affect': 'first',
    'Confidence In National Government': 'first',
    'PR rating': 'first',
    'CL rating': 'first',
    'Total freedom': 'first',
    'weighted_suicides': 'sum'
})
aggregated_data['suicides/100k pop'] = aggregated_data['weighted_suicides'] / aggregated_data['population']
aggregated_data.drop('weighted_suicides', axis=1, inplace=True)
aggregated_data.reset_index(inplace=True)

# Add the constant columns
aggregated_data['generation'] = 'All'
aggregated_data['sex'] = 'Both'
aggregated_data['age'] = 'All'
sum_data = aggregated_data

grouped = df.groupby(['Country', 'Year', 'sex'])
aggregated_data = grouped.agg({
    'population': 'sum',
    'suicides_no': 'sum',
    'Life Ladder': 'first',  # Assuming these values are constant for each group
    'Social Support': 'first',
    'Freedom To Make Life Choices': 'first',
    'Perceptions Of Corruption': 'first',
    'Positive Affect': 'first',
    'Negative Affect': 'first',
    'Confidence In National Government': 'first',
    'PR rating': 'first',
    'CL rating': 'first',
    'Total freedom': 'first',
    'weighted_suicides': 'sum'
})
aggregated_data['suicides/100k pop'] = aggregated_data['weighted_suicides'] / aggregated_data['population']
aggregated_data.drop('weighted_suicides', axis=1, inplace=True)
aggregated_data.reset_index(inplace=True)

aggregated_data['generation'] = 'All'
aggregated_data['age'] = 'All'

new_df = pd.concat([merged_df, sum_data])
final_df = pd.concat([new_df, aggregated_data])
final_df.reset_index(inplace=True)
final_df = final_df.drop(columns=["index"])
final_df = final_df.rename(columns={"suicides/100k pop": "suicides_per_100k"})
print(final_df.columns)

print("Save the dataset!")
final_df.to_csv("data.csv", index=False)
