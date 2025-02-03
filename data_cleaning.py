import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Data Exploration and Cleaning
smart_alarm_df = pd.read_csv('smart_alarm_management_exploration_sample.csv')
print(smart_alarm_df.shape)
print(smart_alarm_df.columns)

# Display the first few rows of the DataFrame
print(smart_alarm_df.head())

# Summary Statistics of the dataset
print(smart_alarm_df.describe())

# Check percentage of missing values in each column
missing_percentage = smart_alarm_df.isnull().mean() * 100
print(missing_percentage)

# Check for duplicate rows
duplicate_rows = smart_alarm_df.duplicated()
print(f"Number of duplicate rows: {duplicate_rows.sum()}")

# Check for duplicate columns
duplicate_cols = smart_alarm_df.columns.duplicated()
print(f"Number of duplicate columns: {duplicate_cols.sum()}")

# Print the duplicate column names
if duplicate_cols.any():
    print("\nDuplicate columns:")
    print(smart_alarm_df.columns[duplicate_cols])
else:
    print("No duplicate columns found.")


# 2. Text Processing on AlarmLabel and AlarmMessage
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(smart_alarm_df['AlarmMessage'])
feature_names = tfidf.get_feature_names_out()
