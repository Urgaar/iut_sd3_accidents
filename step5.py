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


victime = victime.drop(columns = nans)
victime = victime.dropna()
victime = pd.read_csv("step2/missing_values_deleted.csv", sep=",")

victime = victime.drop(columns=['an'])

hrmn=pd.cut(victime['hrmn'],24,labels=[str(i) for i in range(0,24)])

victime['hrmn']=hrmn.values

victime.to_csv("step3/time_encoding.csv")

from sklearn.cluster import KMeans

df = pd.read_csv("step3/time_encoding.csv", sep=",")

# On extrait du tableau la latitude et la longitude

X_lat = df['lat']
X_long = df['long']

# On définit tous nos points à classifier

X_cluster = np.array((list(zip(X_lat, X_long))))

# Kmeans nous donne pour chaque point la catégorie associée

clustering = KMeans(n_clusters=15, random_state=0)
clustering.fit(X_cluster)

# Enfin on ajoute les catégories dans la base d'entraînement

geo = pd.Series(clustering.labels_)
df['geo'] = geo

df.to_csv("step4/gps_encoding.csv")
df = pd.read_csv("gps_encoding.csv", sep=",")

y = df['grav']

features = ['catu','sexe','trajet','secu',
            'catv','an_nais','mois',
            'occutc','obs','obsm','choc','manv',
            'lum','agg','int','atm','col','gps',
            'catr','circ','vosp','prof','plan',
            'surf','infra','situ','hrmn','geo']

X_train_data = pd.get_dummies(df[features].astype(str))

X_train_data.to_csv("step5/train.csv")
