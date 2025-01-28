import pandas as pd
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import streamlit as st

# تعداد روزهایی که داده میخواهیم تولید کنیم (یک ماه)
num_days = 30  # یک ماه

# تاریخ شروع
start_date = datetime(2025, 1, 1)

# پارامترهایی که می‌خواهیم داده تولید کنیم
params = ['Date', 'Humidity (%)', 'Temperature (°C)', 'pH', 'Nitrogen (ppm)', 'Phosphorus (ppm)', 'Potassium (ppm)']

# تابع برای تولید داده‌های فرضی
def generate_data(num_days):
    data = []
    for i in range(num_days):
        date = start_date + timedelta(days=i)
        humidity = round(random.uniform(20, 80), 2)  # رطوبت بین 20% و 80%
        temperature = round(random.uniform(5, 40), 2)  # دما بین 5 تا 40 درجه
        ph = round(random.uniform(5.5, 8), 2)  # pH بین 5.5 تا 8
        nitrogen = round(random.uniform(10, 100), 2)  # نیتروژن بین 10 تا 100 ppm
        phosphorus = round(random.uniform(5, 50), 2)  # فسفر بین 5 تا 50 ppm
        potassium = round(random.uniform(10, 200), 2)  # پتاسیم بین 10 تا 200 ppm
        data.append([date, humidity, temperature, ph, nitrogen, phosphorus, potassium])
    return data

# تولید داده‌ها
data = generate_data(num_days)

# تبدیل به DataFrame
df = pd.DataFrame(data, columns=params)

# ذخیره داده‌ها در فایل Excel
df.to_excel("soil_data_30_days.xlsx", index=False)

# بارگذاری داده‌ها از فایل اکسل
df = pd.read_excel("soil_data_30_days.xlsx")

# نمایش پنج ردیف اول داده‌ها
print(df.head())

# تحلیل داده‌ها - محاسبه میانگین، حداقل و حداکثر برای هر پارامتر
summary = df.describe()
print("Summary Statistics:\n", summary)

# ساخت داشبورد
st.title('پلتفرم تحلیل وضعیت خاک')

# نمایش داده‌ها به صورت جدول
st.subheader('جدول داده‌ها:')
st.write(df)

# انتخاب بازه زمانی توسط کاربر
st.sidebar.header("انتخاب بازه زمانی")
start_date_input = st.sidebar.date_input("تاریخ شروع", df['Date'].min())
end_date_input = st.sidebar.date_input("تاریخ پایان", df['Date'].max())

# فیلتر کردن داده‌ها بر اساس بازه زمانی
filtered_data = df[(df['Date'] >= pd.to_datetime(start_date_input)) & (df['Date'] <= pd.to_datetime(end_date_input))]

# نمودار تغییرات دما و رطوبت
st.subheader('نمودار تغییرات دما و رطوبت در بازه‌ی انتخابی شما:')
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data['Date'], filtered_data['Temperature (°C)'], label='Temperature (°C)', color='red')
ax.plot(filtered_data['Date'], filtered_data['Humidity (%)'], label='Humidity (%)', color='blue')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Temperature and Humidity Over Time')
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# پیش‌بینی وضعیت دما برای روزهای آینده
st.subheader('پیش‌بینی وضعیت دما برای روزهای آینده:')
predicted_temperatures = filtered_data['Temperature (°C)'].rolling(window=7).mean()  # پیش‌بینی ساده با میانگین متحرک
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data['Date'], predicted_temperatures, label='Predicted Temperature (°C)', color='orange')
ax.set_xlabel('Date')
ax.set_ylabel('Predicted Temperature (°C)')
ax.set_title('Predicted Temperature for Upcoming Days')
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# پیش‌بینی رطوبت و pH با استفاده از میانگین متحرک
filtered_data['Predicted Humidity (%)'] = filtered_data['Humidity (%)'].rolling(window=7).mean()
filtered_data['Predicted pH'] = filtered_data['pH'].rolling(window=7).mean()

# نمودار پیش‌بینی رطوبت
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data['Date'], filtered_data['Predicted Humidity (%)'], label='Predicted Humidity (%)', color='blue')
ax.set_xlabel('Date')
ax.set_ylabel('Predicted Humidity (%)')
ax.set_title('Predicted Humidity for Upcoming Days')
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# نمودار پیش‌بینی pH
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data['Date'], filtered_data['Predicted pH'], label='Predicted pH', color='green')
ax.set_xlabel('Date')
ax.set_ylabel('Predicted pH')
ax.set_title('Predicted pH for Upcoming Days')
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# نمودار پراکندگی برای رابطه بین دما و رطوبت
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(filtered_data['Temperature (°C)'], filtered_data['Humidity (%)'], color='purple')
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Humidity (%)')
ax.set_title('Relationship Between Temperature and Humidity')
st.pyplot(fig)
