'''
import csv

data_testing_1 = [
    ["Product", "Price", "Stock"],
    ["Apples", 5, 100],
    ["Bananas", 3, 150],
    ["Oranges", 4, 200]
]

with open("products.csv", "w", newline="") as file:
    my_writer = csv.writer(file)
    my_writer.writerows(data_testing_1)

with open("products.csv", "r") as file:
    my_reader = csv.reader(file)
    for row in my_reader:
        print(row)

        

import csv

data_testing_2 = [
    {"Product": "Apples", "Price": 5, "Stock": 100},
    {"Product": "Bananas", "Price": 3, "Stock": 150},
    {"Product": "Oranges", "Price": 4, "Stock": 200}
]

with open ("dict_products.csv", "w", newline="") as file:
    my_writer = csv.DictWriter(file, fieldnames=["Product", "Price", "Stock"])
    my_writer.writeheader()
    my_writer.writerows(data_testing_2)

with open ("dict_products.csv", "r") as file:
    my_reader = csv.DictReader(file)
    for row in my_reader:
        print(row)

        



import matplotlib.pyplot as plt

# Dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Vẽ biểu đồ đường
plt.plot(x, y, marker="o")
plt.title("Exempel på linjediagram")
plt.xlabel("X-axeln")
plt.ylabel("Y-axeln")
plt.grid(True)
plt.show()
'''

import seaborn as sns
import matplotlib.pyplot as plt

# Dữ liệu mẫu
data = [12, 15, 17, 14, 19, 24, 29, 30, 32, 35]

# Biểu đồ phân phối dữ liệu
sns.histplot(data, bins=5, kde=True)
plt.title("Exempel på histogram")
plt.show()
