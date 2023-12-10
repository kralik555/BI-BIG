import pandas as pd

happy = pd.read_csv('data/happy.csv')
freedom = pd.read_csv('data/freedom.csv')
suicide = pd.read_csv('data/suicide.csv')

merged_df = pd.merge(happy, freedom, on=['Country', 'Year'], how='inner')
merged_df = pd.merge(happy, freedom, on=['Country', 'Year'], how='inner')

merged_df.to_csv('logstash/datasets/data.csv', index=False)
