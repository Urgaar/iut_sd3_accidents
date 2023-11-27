#import des librairies
import pandas as pd
df7=pd.read_csv("C:/Users/sgranier/iut_sd3_accidents/carac.csv",on_bad_lines='skip')
df2=pd.read_csv("C:/Users/sgranier/iut_sd3_accidents/lieux.csv",on_bad_lines='skip')
df3=pd.read_csv("C:/Users/sgranier/iut_sd3_accidents/veh.csv",on_bad_lines='skip')
df4=pd.read_csv("C:/Users/sgranier/iut_sd3_accidents/vict.csv",on_bad_lines='skip')
import pandas as pd
all_files = ["vict.csv","veh.csv","lieux.csv"]

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)
li.append(df7)

frame = pd.concat(li, axis=0, ignore_index=True)
print(frame)
# set files path
frame.to_csv("merged_data.csv")
