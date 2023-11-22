
import pandas as pd

#df = data file
contacts_df = pd.read_csv('./contacts_LEC06.csv')

print(contacts_df.head())

for index, contact in contacts_df.iterrows():
    print(index, contact['Name'], contact['E-mail'])

