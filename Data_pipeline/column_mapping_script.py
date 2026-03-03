import pandas as pd

df = pd.read_excel('file',nrows=0)

column_map = {'Date' : 'date',
              'ARTIST' : 'artist',                     
              'SALE_PRC' : 'sale_price',           
              'DESCRIPTION' : 'description' ,
              'dscptn' : 'description',
              'gross_appreciation_multiplier' : 'gross_appreciation_multiplier', 
              'gross_appreciation_period' : 'gross_appreciation_period', 
              'has_image' : 'has_image',
              'image_url' : 'image_url', 
              'purchase_price' : 'purchase_price', 
              'tiTLE' : 'title', 
              'Urrl' : 'url'}     
df.rename(columns=column_map,inplace=True) 

master_cols = ['date',
               'title',
               'artist',                              
               'description',
               'purchase_price',
               'sale_price', 
               'gross_appreciation_multiplier', 
               'gross_appreciation_period', 
               'url',
               'image_url', 
               'has_image'
] 
df = df[master_cols]                                                                                                                  