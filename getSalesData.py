import pandas as pandas
import matplotlib.pyplot as plt


#Graphs the status according to last contact
##df = pandas.read_sql("SELECT count(*)status, lastcontact FROM leads WHERE status = 'closed' AND lastcontact ='')
##df.plot(kind="bar", x="lastcontact" y="status")
plt.show()