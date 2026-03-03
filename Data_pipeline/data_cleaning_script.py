import pandas as pd

df = pd.read_excel

df.dropna(subset=['title'],inplace=True)  

df.fillna('None',inplace=True)                  

df.drop_duplicates(inplace=True)  

df['date'] = pd.to_datetime(df['date'],errors='coerce')

df['gross_appreciation_multiplier'] = df['gross_appreciation_multiplier'].astype(str).str.replace('x','') 

df['gross_appreciation_period'] = df['gross_appreciation_period'].str.extract('(\d+)')

df['has_image'] = df['has_image'].astype(bool)                                                                                     