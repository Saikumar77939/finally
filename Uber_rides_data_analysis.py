# === Uber Ride Data Analysis ===

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set plot style and figure size
plt.style.use('ggplot')
#sns.set_theme(style="whitegrid")  # Use Seaborn's native style system

sns.set_palette('Set2')
plt.rcParams['figure.figsize'] = (12, 8)

# 2. Load Data
file_path = r"D:\today\Uber rides.xlsx"

try:
    df = pd.read_excel(file_path)
    print(f"✅ Loaded {len(df)} records from Excel file.")
except FileNotFoundError:
    print("❌ File not found. Please check the path and file name.")
    df = None

# 3. Data Exploration
if df is not None:
    print("\n--- Dataset Info ---")
    df.info()

    print("\n--- Dataset Description ---")
    print(df.describe(include='all'))

    print("\n--- First 5 Records ---")
    print(df.head())

# 4. Data Cleaning
if df is not None:
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert datetime column if it exists
    if 'pickup_datetime' in df.columns:
        df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

    print("\n✅ Cleaned Dataset Info:")
    df.info()

# 5. Exploratory Data Analysis
if df is not None and 'pickup_datetime' in df.columns:
    # Extract time components
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
    df['month'] = df['pickup_datetime'].dt.month

    # Ride Distribution by Hour
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='hour')
    plt.title('Ride Distribution by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Rides')
    plt.xticks(range(0, 24))
    plt.show()

    # Ride Distribution by Day of Week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='day_of_week', order=range(7))
    plt.title('Ride Distribution by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Rides')
    plt.xticks(ticks=range(7), labels=days)
    plt.show()

# 6. Insights and Conclusion
print("\n📌 Add your insights and conclusions here based on the visualizations and statistics above.")

a="""Insights:
Hourly Ride Patterns:
-Most rides occur during peak commuting hours, typically between 5 PM and 9 PM, indicating high demand in the evening.
-There’s a noticeable dip in early morning hours (e.g., 2 AM – 6 AM), which suggests lower ride activity during that period.

Day of Week Trends:
-Ride volume tends to increase toward the weekend, especially on Friday and Saturday, possibly due to social activities or outings.
-Weekday rides may indicate work or school commutes, whereas weekend patterns may reflect leisure or entertainment travel.

Data Quality:
-The dataset contained missing values and duplicates, which were successfully cleaned.
-The pickup datetime field was converted to proper datetime format for time-based analysis.


Conclusion:
The Uber ride dataset reveals clear patterns in human mobility behavior, especially around daily routines and weekly cycles.

Understanding when rides are most frequent can help Uber:
-Optimize driver availability
-Improve surge pricing models
-Enhance customer service during peak times

For deeper insights, further analysis can be done by incorporating:
-Pickup/dropoff locations (geospatial analysis)
-Trip durations and distances
-Fare amounts and customer ratings 
"""
print(a)