import csv
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import pickle
import psycopg2

conn = psycopg2.connect(database="body-performance",host="db", user="admin", password="admin", port="5432")

#query to extract database
cur = conn.cursor()
cur.execute("SELECT * FROM body_performance")

# Recupero dei dati e scrittura in un file CSV
with open('bodyPerformance.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cur.description])  # Scrittura della riga di intestazione
    writer.writerows(cur)

# Chiusura del cursore e della connessione
cur.close()
conn.close()

#Dataset loading
df = pd.read_csv('bodyPerformance.csv')

###complete eda on notebook###

#Feature engineering

#Rename columns
df = df.rename(columns={"body fat_%":"body_fat", "height_cm":"height", "weight_kg":"weight", "sit and bend forward_cm":"bend_forward", "gripForce":"grip_force","sit-ups counts":"sit_ups", "broad jump_cm":"broad_jump"})
df.sample(10)

#one hot encode of gender variable
sex = df[['gender']]
oneHot = OneHotEncoder(sparse=False)
sex = pd.DataFrame(oneHot.fit_transform(sex), columns=oneHot.get_feature_names_out())
df.drop(columns=['gender'], axis=1, inplace=True)
df = pd.concat([sex, df], axis=1)
df = df.rename(columns={'x0_F': 'F'})
df = df.rename(columns={'x0_M': 'M'})

#conversion in meters
df['height_m'] = df.height/100
#creation of a new feature
df['BMI'] = df.weight /df.height_m**2
df.drop('height',axis = 1,inplace = True)
df.drop('height_m',axis = 1,inplace = True)
df.drop('weight',axis = 1,inplace = True)

#Label conversion
classes = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
df['class'] = df['class'].replace(classes)

#Label
y = df[['class']]
x = df.drop(['class'],axis = 1)
x.head()

#Exploratory Data Analysis
print(df.head())
print(df.shape)
print(df.describe())
print(df.info())

#Standardization
sc = StandardScaler()
sc.fit(x)
x_train = sc.transform(x)

#Training
classifier = XGBClassifier()
classifier.fit(x_train,y)

#Model and scaler export
with open('./data/model.pickle', 'wb') as file:
    pickle.dump(classifier, file)
with open('./data/scaler.pickle','wb') as file:
    pickle.dump(sc, file)
