import pandas as pd 
import matplotlib.pyplot as plt

df = pd.DataFrame({'Employee': ['Robert', 'Derek', 'Marcus'],
                    'Sales': ['5', '10', '50']})

print(df)



##df.plot(x = 'Employee', y='Sales', kind = 'bar')
plt.bar(df['Employee'],rwidth=0.9,alpha=0.3,color='blue',bins=15,edgecolor='red') 
plt.show()
#Sort the leaderboard

##df = df.sort(['Employee', 'Sales'], ascending=[1,0])
##print(df)