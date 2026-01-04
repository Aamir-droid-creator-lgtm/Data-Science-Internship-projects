import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure output folder exists
os.makedirs("visualizations", exist_ok=True)

# Load dataset
try:
    df = pd.read_csv("data/sales_data.csv")
except FileNotFoundError:
    print("Error: sales_data.csv not found in data folder")
    exit()

# Data cleaning
df.dropna(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])

# If Total_Sales not reliable, recalculate
df["Calculated_Sales"] = df["Quantity"] * df["Price"]

# ---------------- ANALYSIS ---------------- #

# 1. Sales by Product
product_sales = df.groupby("Product")["Calculated_Sales"].sum()

# 2. Monthly Sales Trend
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Calculated_Sales"].sum()

# 3. Revenue by Region
region_sales = df.groupby("Region")["Calculated_Sales"].sum()

# ---------------- VISUALIZATIONS ---------------- #

# Bar Chart: Product vs Sales
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.close()

# Line Chart: Monthly Sales Trend
plt.figure(figsize=(8, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("visualizations/monthly_sales_trend.png")
plt.close()

# Pie Chart: Revenue Distribution by Region
plt.figure(figsize=(7, 7))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/regional_revenue_distribution.png")
plt.close()

# ---------------- SUMMARY OUTPUT ---------------- #

print("📊 E-COMMERCE SALES SUMMARY")
print("Total Revenue:", df["Calculated_Sales"].sum())
print("Top Product:", product_sales.idxmax())
print("Best Sales Month:", monthly_sales.idxmax())
print("Top Revenue Region:", region_sales.idxmax())
