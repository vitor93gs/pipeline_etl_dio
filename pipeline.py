import pandas as pd

df = pd.read_csv('data.csv')
print(df)
def update_transformer(id,entry,updated_entry):
    df.loc[df['ID'] == id, entry] = updated_entry
    df.to_csv('data.csv', index=False)

update_transformer(1,"Abilities","['Leadership','Mega Punch','Eye Beam']")
updated_df = pd.read_csv('data.csv')
print(updated_df)
