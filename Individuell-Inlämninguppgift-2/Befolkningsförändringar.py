import pandas as pd

#Öppnar och läser in csv filen med pandas. Obs! Data är åtskilda med ";" istället för ",".
df = pd.read_csv(r"C:\Users\johan\Documents\newproject\Individuell-Inlämninguppgift-2\befolkningsfoeraendringar-helar(original).csv", sep=";")
print(df.head(10))

#Controllerar om det finns "null" data i filen.
print(df.isnull().sum())

#Skapar och beräknar kolumnen "tillväxttakt".
df["tillväxttakt"] = df["folkökning"] / df["folkmängd"] * 100
print(df["tillväxttakt"].head(10))

#Filtrerar de senaste 10 åren (från 2013-2023).
df_filtered = df[df["år"] >= 2013]
print(df_filtered.head(10))

#Använd groupby() och agg() för att summera och analysera nyckeltal. 
grouped_df = df_filtered.groupby("år").agg({
    "folkmängd": "sum",
    "folkökning": "sum",
    "födelseöverskott": "sum",
    "invandringar": "sum"
})
print(grouped_df)

#Skapar en sökväg till platsen där filen ska sparas. Och exporterar filen med .to_excel().
processed_file_path = r"C:\Users\johan\Documents\newproject\Individuell-Inlämninguppgift-2\processed_data_befolkningsförändringar.xlsx"
df_filtered.to_excel(processed_file_path, index=False)
print(f"Data have been saved at: {processed_file_path}")

import matplotlib.pyplot as plt
import seaborn as sns

#Läser in data från den nyligen exporterade excel filen.
df_filtered = pd.read_excel(r"C:\Users\johan\Documents\newproject\Individuell-Inlämninguppgift-2\processed_data_befolkningsförändringar.xlsx")

#Visualiserar data om "folkökning" med ett histogram.
plt.figure(figsize=(8, 6))
sns.histplot(df_filtered["folkökning"], kde=True, color="skyblue")
plt.title("Distribution of Population Growth (2013-2023)", fontsize=14)
plt.xlabel("Population Growth", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(True)
plt.show()

#Visualiserar "Averagre Growth Rate Over Time (2013-2023)" med ett line chart. 
plt.figure(figsize=(8, 6))
avg_growth_rate = df_filtered.groupby("år")["tillväxttakt"].mean()
avg_growth_rate.plot(kind="line", color="orange", marker="o")
years = avg_growth_rate.index
plt.xticks(ticks=years, labels=years, rotation=45)
plt.title("Average Growth Rate Over Time (2013-2023)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Growth Rate (%)", fontsize=12)
plt.grid(True)
plt.show()

#Visualiserar "Birth Surplus & Immigration vs Population Growth (2013-2023)" med ett scatter plot.
plt.figure(figsize=(10, 6))
#Plot födelseöverskott vs folkökning
sns.scatterplot(x="födelseöverskott", y="folkökning", data=df_filtered, color="blue", label="Birth Surplus", s=100)
#Plot invandringar vs folkökning
sns.scatterplot(x="invandringar", y="folkökning", data=df_filtered, color="orange", label="Immigration", s=100)
plt.title("Birth Surplus & Immigration vs Population Growth (2013-2023)", fontsize=14)
plt.xlabel("Birth Surplus and Immigration", fontsize=12)
plt.ylabel("Population Growth", fontsize=12)
plt.grid(True)
plt.show()

