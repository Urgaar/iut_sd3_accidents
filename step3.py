import pandas as pd
df=pd.read_csv("merged_data.csv")
victime=df
print(victime.columns)
hrmn=pd.cut(victime['hrmn'],24,labels=[str(i) for i in range(0,24)])
victime['hrmn']=hrmn.values

