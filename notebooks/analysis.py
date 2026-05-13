import pandas as pd

# Load dataset
df = pd.read_csv("../data/sales.csv", encoding="latin1")

# Show first 5 rows
print(df.head())

# Dataset shape
print("Shape:", df.shape)

# Column names
print(df.columns)

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create month column
df["Month"] = df["Order Date"].dt.month_name()

# Total sales by category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales By Category:")
print(category_sales)

# Top 5 cities by sales
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)

print("\nTop Cities:")
print(city_sales.head())

# Save cleaned dataset
df.to_csv("../data/cleaned_sales.csv", index=False)

print("\nCleaned dataset saved successfully!")