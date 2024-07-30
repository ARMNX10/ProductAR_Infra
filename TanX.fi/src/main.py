import pandas as pd
from data_processing import (
    read_data, 
    compute_revenue_by_month, 
    compute_revenue_by_product, 
    compute_revenue_by_customer, 
    top_10_customers_by_revenue
)

def main():
    file_path = 'orders.csv'
    df = read_data(file_path)
    revenue_by_month = compute_revenue_by_month(df)
    print("Total Revenue by Month:")
    print(revenue_by_month)
    print("\n")
    revenue_by_product = compute_revenue_by_product(df)
    print("Total Revenue by Product:")
    print(revenue_by_product)
    print("\n")
    revenue_by_customer = compute_revenue_by_customer(df)
    print("Total Revenue by Customer:")
    print(revenue_by_customer)
    print("\n")
    top_customers = top_10_customers_by_revenue(df)
    print("Top 10 Customers by Revenue:")
    print(top_customers)
if __name__ == "__main__":
    main()
