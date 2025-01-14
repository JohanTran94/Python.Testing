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

import pandas as pd
print(pd.__version__)

data = {
    "Name": ["Anna", "Björn", "Cecilia"], 
    "Age": [25, 30, 27],
    "City": ["Stockholm", "Göteborg", "Malmö"]
}
df = pd.DataFrame(data)
print(df)

file = open("Inlämning_uppgift_1_Chi Cuong Tran.txt", "r")  # Mở tệp đọc
content = file.read()  # Đọc nội dung tệp
file.close()  # Đóng tệp




print ("hello, world!")
#Öppna en fil med context manager
with open ("data.csv", "w") as file:
    file.write("Name,Age,City\n")

with open ("data.csv", "a") as file:
    file.write("Anna,25,Stockholm\n")

with open ("data.csv", "a") as file:
    file.write("Björn,30,Göteborg\n")

with open ("data.csv", "a") as file:
    file.write("Cecelia,27,Stockholm")

with open ("data.csv") as file:
    print(file.read())

with open ("data.csv") as file:
    for line in file:
        print (line.strip())
'''

import pandas as pd

print (pd.__version__)

data = {
    "Name": ["Anna", "Björn", "Cecilia"], 
    "Age": [25, 30, 27],
    "City": ["Stockholm", "Göteborg", "Malmö"]
}
df = pd.DataFrame(data)
print(df)
print(df.info())

print("Gör något med kolumnen Ages:")
ages = df["Age"]
print(ages)

print("Alla ädre än 25: ")
filtered_Data = df[df["Age"] > 25]
print(filtered_Data)

print("Alla yngreän eller exakt 25 år: ")
filtered_Data = df[df["Age"] <= 25]
print(filtered_Data)

print("Antal element:")
len(ages)