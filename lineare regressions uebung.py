import pandas as pd
df = pd.read_csv("C:\Users\marck\OneDrive - OST\OST RJ\WING\WING - 4 Semester\MOSIM\Python Systemanalyse\Übung 4_2")

#X = df.iloc[0:len(df),0] #Erste Spalte
#Y = df.iloc[0:len(df),1] #Zweite Spale

print(df.iloc[0,2])