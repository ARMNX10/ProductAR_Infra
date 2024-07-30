import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def compute_revenue_by_month(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year_month'] = df['order_date'].dt.to_period('M')
    revenue_by_month = df.groupby('year_month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
    return revenue_by_month

def compute_revenue_by_product(df):
    df['revenue'] = df['product_price'] * df['quantity']
    revenue_by_product = df.groupby('product_name')['revenue'].sum()
    return revenue_by_product

def compute_revenue_by_customer(df):
    df['revenue'] = df['product_price'] * df['quantity']
    revenue_by_customer = df.groupby('customer_id')['revenue'].sum()
    return revenue_by_customer

def top_10_customers_by_revenue(df):
    revenue_by_customer = compute_revenue_by_customer(df)
    top_10_customers = revenue_by_customer.nlargest(10)
    return top_10_customers
