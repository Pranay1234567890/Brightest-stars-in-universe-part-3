
## START OF CODE ##
import pandas as pd
import csv

df=pd.read_csv("Brightest_stars.csv")

print(df.columns)

df.drop(['Unnamed:0','Unnamed:6','Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1', 'Luminosity'],axis=1,inplace=True)
final_data=df.dropna()

final_data.reset_index(drop=True,inplace=True)

final_data.to_csv('final_data.csv')
final_data.info()
final_data.describe()
final_data.head(5)
final_data.dtypes
## END OF CODE ##

## ERRORS AND INFO ##

## No. OF ERRORS: 2
## RAN CODE: 3 Times
## ERRORS ON RUN: 2, 3

## ERROR NO.1 and 2

# y
# Index(['Unnamed: 0', 'Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity',
#        'Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'],
#       dtype='object')
# Traceback (most recent call last):
#   File "c:\Users\-\Desktop\P130\main.py", line 10, in <module>
#     df.drop(['Unnamed:0','Unnamed:6','Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1', 'Luminosity'],axis=1,inplace=True)
#   File "C:\Users\-\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper    
#     return func(*args, **kwargs)
#   File "C:\Users\-\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\frame.py", line 4901, in drop
#     return super().drop(
#   File "C:\Users\-\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\generic.py", line 4150, in drop
#    obj = obj._drop_axis(labels, axis, level=level, errors=errors)
#  File "C:\Users\-\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\generic.py", line 4185, in _drop_axis    
#     new_axis = axis.drop(labels, errors=errors)
#   File "C:\Users\-\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\indexes\base.py", line 6018, in drop     
#     raise KeyError(f"{labels[mask]} not found in axis")
# KeyError: "['Unnamed:0' 'Unnamed:6'] not found in axis"