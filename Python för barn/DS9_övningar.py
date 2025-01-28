'''
# Extract: Läs in försäljningsdata och kunddata
import pandas as pd
sales_data = pd.read_csv("sales_2025.csv")
customer_data = pd.read_csv("customers.csv")

merged_data = pd.merge(sales_data, customer_data, on="CustomerID", how="inner")
print(merged_data)

#Transform: Hantera saknade värdenoch skapa en ny kolumn "Total_Sales"
merged_data["Total_Sales"] = merged_data["Price"] * merged_data["Quantity"]
print(merged_data)

#Load: Skapa en final CSV filen
merged_data.to_csv("merged_data.csv")
'''




from textblob import TextBlob

svTexts = [
   "Den här produkten är fantastisk!",
   "Jag är missnöjd med servicen.",
   "Helt okej upplevelse, inte mer."
]

enTexts = [
    "This product is amazing!",
    "I am dissatisfied with the service.",
    "Okay experience, nothing more."
]

texts = enTexts

for text in texts:
   analysis = TextBlob(text)
   print(f"Text: {text}")
   print(f"Polarity: {analysis.sentiment.polarity}")
   print(f"Subjectivity: {analysis.sentiment.subjectivity}\n")


