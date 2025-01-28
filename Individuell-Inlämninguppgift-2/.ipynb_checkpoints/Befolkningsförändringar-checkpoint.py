import pandas as pd

df = pd.read_csv(r"C:\Users\johan\Documents\newproject\befolkningsfoeraendringar-helar.csv", sep=";")
print(df.head())

print(df.isnull().sum())

df['tillväxttakt'] = df['folkökning'] / df['folkmängd'] * 100
print(df["tillväxttakt"].head())

df_filtered = df[df['år'] >= 2013] #lọc dữ liệu trong vòng 10 năm gần đây
print(df_filtered.head())

grouped_df = df.groupby('år').agg({
    'folkmängd': 'sum',
    'folkökning': 'sum',
    'födelseöverskott': 'sum',
    'invandringar': 'sum'
})
print(grouped_df.head())

processed_file_path = r"C:\Users\johan\Desktop\DM-TUC-24\Data Science\Inlämninguppgift 2\processed_data_befolkningsförändringar.xlsx"
df_filtered.to_excel(processed_file_path, index=False)
print(f"Data have been saved at: {processed_file_path}")

import matplotlib.pyplot as plt
import seaborn as sns

# Đọc lại dữ liệu từ file Excel vừa xuất
df_filtered = pd.read_excel(r"C:\Users\johan\Desktop\DM-TUC-24\Data Science\Inlämninguppgift 2\processed_data_befolkningsförändringar.xlsx")

# a. Biểu đồ Histogram
plt.figure(figsize=(8, 6))
sns.histplot(df_filtered['folkökning'], kde=True, color='skyblue')
plt.title('Distribution of Population Growth (2013-2023)', fontsize=14)
plt.xlabel('Population Growth', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True)
plt.show()

# b. Biểu đồ Line Chart
# Biểu đồ Line Chart với tốc độ tăng trưởng dân số qua các năm
plt.figure(figsize=(8, 6))
df_filtered.groupby('år')['tillväxttakt'].mean().plot(kind='line', color='orange', marker='o')
plt.title('Average Growth Rate Over Time (2013-2023)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Growth Rate (%)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.show()


# c. Biểu đồ Scatter Plot
# Tạo một scatter plot với màu sắc dựa trên giá trị của một biến khác (ví dụ: 'folkökning' - tăng trưởng dân số)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='födelseöverskott', y='invandringar', data=df_filtered, hue='folkökning', palette='viridis', s=100)
plt.title('Birth Surplus vs Immigration (2013-2023)', fontsize=14)
plt.xlabel('Birth Surplus', fontsize=12)
plt.ylabel('Immigration', fontsize=12)
plt.grid(True)
plt.legend(title='Population Growth', fontsize=10)
plt.show()


