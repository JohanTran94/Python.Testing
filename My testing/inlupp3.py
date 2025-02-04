import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Tạo dữ liệu mẫu
data = {
    'födda': [1000, 1050, 1100, 1200, 1250, 1300, 1350, 1400, 1450, 1500],
    'döda': [500, 520, 530, 550, 580, 600, 620, 630, 650, 680],
    'folkmängd': [10000, 10100, 10200, 10300, 10450, 10550, 10700, 10850, 11000, 11100],
    'samtliga inflyttningar': [200, 220, 250, 300, 320, 350, 380, 400, 420, 450],
    'samtliga utflyttningar': [150, 160, 180, 200, 220, 240, 250, 260, 270, 290],
    'invandringar': [100, 110, 120, 130, 140, 150, 160, 170, 180, 200],
    'utvandringar': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
}

# Chuyển dữ liệu sang DataFrame
df = pd.DataFrame(data)

# Tạo các cột mới dựa trên dữ liệu hiện có
df['Befolkningstillväxt (%)'] = (df['folkmängd'].pct_change() * 100).fillna(0)
df['Födelsetal (%)'] = (df['födda'] / df['folkmängd']) * 1000
df['Dödstal (%)'] = (df['döda'] / df['folkmängd']) * 1000
df['Nettoinflyttning (%)'] = ((df['samtliga inflyttningar'] - df['samtliga utflyttningar']) / df['folkmängd']) * 1000
df['Naturlig befolkningstillväxt (%)'] = (df['födda'] - df['döda']) / df['folkmängd'] * 1000
df['Invandringstal (%)'] = (df['invandringar'] / df['folkmängd']) * 1000
df['Utvandringstal (%)'] = (df['utvandringar'] / df['folkmängd']) * 1000

# Chọn các cột đặc trưng (features) và cột mục tiêu (target)
X = df[['Födelsetal (%)', 'Dödstal (%)', 'Nettoinflyttning (%)', 'Naturlig befolkningstillväxt (%)', 
        'Invandringstal (%)', 'Utvandringstal (%)']]
y = df['Befolkningstillväxt (%)']

# Tiền xử lý: Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Chia dữ liệu thành bộ huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Khởi tạo mô hình hồi quy tuyến tính
model = LinearRegression()

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán trên bộ kiểm tra
y_pred = model.predict(X_test)

# Đánh giá mô hình
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# In kết quả
print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R^2 Score: {r2}')

# Trực quan hóa sự phân tán giữa giá trị thực tế và giá trị dự đoán
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Giá trị thực tế')
plt.ylabel('Giá trị dự đoán')
plt.title('So sánh giá trị thực tế và giá trị dự đoán')
plt.show()

# Trực quan hóa residuals (sai số)
residuals = y_test - y_pred
sns.histplot(residuals, kde=True)
plt.title('Phân phối của residuals')
plt.show()
