'''
import csv
data = [
 {"Name": "Anna", "Age": 25, "City": "Stockholm"},
 {"Name": "Björn", "Age": 30, "City": "Göteborg"}
]
with open("output.csv", "w", newline="") as file:
 writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
 writer.writeheader()
 writer.writerows(data)
'''
import pandas as pd
print(pd.__version__)

data = {
    "Name": ["Anna", "Björn", "Cecilia"], 
    "Age": [25, 30, 27],
    "City": ["Stockholm", "Göteborg", "Malmö"]
}
df = pd.DataFrame(data)
print(df)
