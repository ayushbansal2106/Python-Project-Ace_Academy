# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# file_path = "Sales Data.csv" 
# sales_data = pd.read_csv(file_path, encoding='ISO-8859-1')
# print("First 5 rows of the dataset:")
# print(sales_data.head())
# print("\nMissing Values in Columns:")
# print(sales_data.isnull().sum())
# sales_data.fillna(sales_data.median(numeric_only=True), inplace=True)
# sales_data.dropna(inplace=True)
# print("\nDataset after cleaning:")
# print(sales_data.head())
# print("\nRemaining missing values (should be zero):")
# print(sales_data.isnull().sum())
# print("\nSummary Statistics:")
# print(sales_data.describe())
# if 'SALES' in sales_data.columns and 'QUANTITYORDERED' in sales_data.columns:
#     print(f"\nMean of Sales: {sales_data['SALES'].mean():.2f}")
#     print(f"Median of Sales: {sales_data['SALES'].median():.2f}")
#     print(f"Standard Deviation of Sales: {sales_data['SALES'].std():.2f}")
#     print(f"Mode of Sales: {sales_data['SALES'].mode()[0]:.2f}")
#     print(f"\nMean of Quantity Ordered: {sales_data['QUANTITYORDERED'].mean():.2f}")
#     print(f"Median of Quantity Ordered: {sales_data['QUANTITYORDERED'].median():.2f}")
#     print(f"Standard Deviation of Quantity Ordered: {sales_data['QUANTITYORDERED'].std():.2f}")
#     print(f"Mode of Quantity Ordered: {sales_data['QUANTITYORDERED'].mode()[0]:.2f}")
# sales_data['ORDERDATE'] = pd.to_datetime(sales_data['ORDERDATE'], errors='coerce')
# sales_data.dropna(subset=['ORDERDATE'], inplace=True)  # Drop invalid dates
# sales_data['YearMonth'] = sales_data['ORDERDATE'].dt.to_period('M')
# sales_trends = sales_data.groupby('YearMonth')['SALES'].sum()
# plt.figure(figsize=(12, 6))
# sales_trends.plot(marker='o', color='b')
# plt.title("Sales Trend Over Time", fontsize=16)
# plt.xlabel("Year-Month")
# plt.ylabel("Total Sales")
# plt.grid()
# plt.show()
# sales_data['Month'] = sales_data['ORDERDATE'].dt.month
# monthly_sales = sales_data.groupby('Month')['SALES'].sum()
# plt.figure(figsize=(10, 6))
# sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette='viridis')
# plt.title("Seasonal Sales Patterns (Monthly Sales)", fontsize=16)
# plt.xlabel("Month")
# plt.ylabel("Total Sales")
# plt.show()
# if 'PRODUCTCODE' in sales_data.columns:
#     top_products = sales_data.groupby('PRODUCTCODE')['SALES'].sum().sort_values(ascending=False).head(10)
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x=top_products.values, y=top_products.index, palette='coolwarm')
#     plt.title("Top 10 Performing Products", fontsize=16)
#     plt.xlabel("Total Sales")
#     plt.ylabel("Product Code")
#     plt.show()

# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_clean_data(file_path):
    """
    Load the dataset and handle missing values.
    Returns a cleaned DataFrame.
    """
    print("Loading dataset...")
    sales_data = pd.read_csv(file_path, encoding="ISO-8859-1")
    print("\nFirst 5 rows of the dataset:")
    print(sales_data.head())

    print("\nMissing Values in Columns:")
    print(sales_data.isnull().sum())

    # Handle missing values
    sales_data.fillna(sales_data.median(numeric_only=True), inplace=True)
    sales_data.dropna(inplace=True)

    print("\nDataset after cleaning:")
    print(sales_data.head())

    return sales_data


def compute_statistics(data, target_columns):
    """
    Compute various statistics for the provided target columns (like 'SALES').
    Returns a dictionary of statistics.
    """
    stats = {}
    for column in target_columns:
        if column in data.columns:
            stats[column] = {
                "Mean": np.round(data[column].mean(), 2),
                "Median": np.round(data[column].median(), 2),
                "Std. Dev": np.round(data[column].std(), 2),
                "Mode": np.round(data[column].mode()[0], 2),
            }
    return stats


def plot_sales_trends(data):
    """
    Plot sales trends over time (YearMonth) using a line chart.
    """
    if "ORDERDATE" in data.columns:
        data["ORDERDATE"] = pd.to_datetime(data["ORDERDATE"], errors="coerce")
        data.dropna(subset=["ORDERDATE"], inplace=True)
        data["YearMonth"] = data["ORDERDATE"].dt.to_period("M")

        sales_trends = data.groupby("YearMonth")["SALES"].sum()
        plt.figure(figsize=(12, 6))
        sales_trends.plot(marker="o", color="b")
        plt.title("Sales Trend Over Time", fontsize=16)
        plt.xlabel("Year-Month")
        plt.ylabel("Total Sales")
        plt.grid()
        plt.show()


def plot_monthly_sales(data):
    """
    Visualize seasonal sales patterns by month using a bar plot.
    """
    if "ORDERDATE" in data.columns:
        data["Month"] = data["ORDERDATE"].dt.month
        monthly_sales = data.groupby("Month")["SALES"].sum()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette="viridis")
        plt.title("Seasonal Sales Patterns (Monthly Sales)", fontsize=16)
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.show()


def plot_top_products(data):
    """
    Visualize the top 10 products based on sales using a horizontal bar plot.
    """
    if "PRODUCTCODE" in data.columns:
        top_products = (
            data.groupby("PRODUCTCODE")["SALES"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_products.values, y=top_products.index, palette="coolwarm")
        plt.title("Top 10 Performing Products", fontsize=16)
        plt.xlabel("Total Sales")
        plt.ylabel("Product Code")
        plt.show()


def main():
    # File path
    file_path = "Sales Data.csv"

    # 1. Load and Clean the Data
    sales_data = load_and_clean_data(file_path)

    # 2. Compute Summary Statistics
    target_columns = ["SALES", "QUANTITYORDERED"]
    stats = compute_statistics(sales_data, target_columns)
    print("\nSummary Statistics:")
    for column, column_stats in stats.items():
        print(f"\nStatistics for {column}:")
        for stat_name, value in column_stats.items():
            print(f"{stat_name}: {value}")

    # 3. Visualizations
    plot_sales_trends(sales_data)
    plot_monthly_sales(sales_data)
    plot_top_products(sales_data)


# Entry point of the script
if __name__ == "__main__":
    main()
