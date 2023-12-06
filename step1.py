#import des librairies
import pandas as pd
carac = pd.read_csv("carac.csv",sep=';')
lieux = pd.read_csv("lieux.csv",sep=';')
veh = pd.read_csv("veh.csv",sep=';')
vict = pd.read_csv("vict.csv",sep=';')
victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')
victime = victime.merge(accident,on='Num_Acc')

