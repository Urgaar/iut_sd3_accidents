import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
carac = pd.read_csv("carac.csv",sep=';')
lieux = pd.read_csv("lieux.csv",sep=';')
veh = pd.read_csv("veh.csv",sep=';')
vict = pd.read_csv("vict.csv",sep=';')
victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')
victime = victime.merge(accident,on='Num_Acc')

nan_values = victime.isna().sum()

nan_values = nan_values.sort_values(ascending=True)*100/len(victime.axes[0])

ax = nan_values.plot(kind='barh', 
                     figsize=(8, 10), 
                     color='#AF7AC5',
                     zorder=2,
                     width=0.85)

ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.tick_params(axis="both", 
               which="both", 
               bottom="off", 
               top="off", 
               labelbottom="on", 
               left="off", 
               right="off", 
               labelleft="on")

vals = ax.get_xticks()

for tick in vals:
  ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)
victime.to_csv("step2/missing_values_deleted.csv")
plt.savefig("step2/missing_value_graph.png")

nans = ['v1','v2','lartpc',
       'larrout','locp','etatp',
       'actp','voie','pr1',
       'pr','place']

df = victime.drop(columns = nans)
df = df.dropna()

