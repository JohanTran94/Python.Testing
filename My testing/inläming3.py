import pandas as pd
#Öppnar och läser in csv filen med pandas. Data är åtskilda med ";".
df = pd.read_csv(r"C:\Users\johan\Documents\newproject\Inlämninguppgift-3\inlupp-3-processed_data_befolkningsförändringar.csv")
print(df.head(10))
#Sorterar kolumnen "år" i rätt ordning 2013 till 2023.
df.sort_values(by='år', ascending=True, inplace=True)
print(df['år'].head(11))
#Beräknar "Födelsetal (%)".
df['Födelsetal (%)'] = (df['födda'] / df['folkmängd']) * 100
#Beräknar "Dödstal (%)".
df['Dödstal (%)'] = (df['döda'] / df['folkmängd']) * 100
#Beräknar "Naturlig befolkningstillväxt (%)".
df['Naturlig befolkningstillväxt (%)'] = (df['födelseöverskott'] / df['folkmängd']) * 100
print(df[['år', 'Födelsetal (%)', 'Dödstal (%)', 'Naturlig befolkningstillväxt (%)']].head(10))

#Visualiserar relationen mellan "Inflyttningar" och "Utflyttningar" med en grouped bar chart.
import matplotlib.pyplot as plt
import numpy as np

width= 0.35
x= np.arange(len(df['år']))
plt.figure(figsize=(10,6))
plt.bar(x - width/2, df['samtliga inflyttningar'], width, label='Samtliga Inflyttningar', color='orange')
plt.bar(x + width/2, df['samtliga utflyttningar'], width, label='Samtliga Utflyttningar', color='green')
plt.xlabel('År')
plt.ylabel('Antal personer')
plt.title('Utflyttningar vs Inflyttningar')
plt.xticks(x, df['år'], rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#Visualiserar "Befolkningstillväxt: Födelsetal, Dödstal & Naturlig Tillväxt" med en grouped bar chart.
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.25
index = np.arange(len(df))
ax.bar(index - bar_width, df['Födelsetal (%)'], bar_width, label='Födelsetal (%)', color='lightblue')
ax.bar(index, df['Dödstal (%)'], bar_width, label='Dödstal (%)', color='salmon')
ax.bar(index + bar_width, df['Naturlig befolkningstillväxt (%)'], bar_width, label='Naturlig befolkningstillväxt (%)', color='lightgreen')
ax.set_xticks(index)
ax.set_xticklabels(df['år'])
ax.set_xlabel('År')
ax.set_ylabel('Procent (%)')
ax.set_title('Befolkningstillväxt: Födelsetal, Dödstal & Naturlig Tillväxt')
ax.legend()
plt.xticks(rotation=45)
plt.show()
from sklearn.linear_model import LinearRegression

#Förbered data för regression
X = df[['år']]  # Oberoende variabel
y = df['tillväxttakt']  # Beroende variabel
#Skapa och träna modellen
model = LinearRegression()
model.fit(X, y)
#Generera framtida år.
future_years = pd.DataFrame({'år': range(df['år'].max() + 1, df['år'].max() + 11)})
#Gör förutsägelser för framtida tillväxt.
future_predictions = model.predict(future_years)
#Visualiserar historiska och förutsagda värden med en line chart.
plt.figure(figsize=(10, 6))
plt.plot(df['år'], df['tillväxttakt'], color='blue', marker="o", label='Historiska data')
plt.plot(df['år'], model.predict(X), color='green', label='Trend')
plt.plot(future_years, future_predictions, color='red', linestyle='--', label='Förutsägelser')
plt.xlabel('År', fontsize=12)
plt.ylabel('Tillväxttakt (%)', fontsize=12)
plt.title('Förutsägelse av Befolkningstillväxt', fontsize=16)
plt.xticks(range(df['år'].min(), future_years['år'].max() + 1), rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
'''
'''