import pandas as pd

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:password@localhost/company_data')

for file in 'files':                                   
    
    print('processing:',file) 
    
    df = pd.read_excel(file)   
    
    df.to_sql('company_data_cleaned',engine,if_exists='append',index=False) 

    del df
    
    print('connected successfully') 
