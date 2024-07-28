import pytest
import pandas as pd
from data_processing import (
    compute_revenue_by_month,
    compute_revenue_by_product,
    compute_revenue_by_customer,
    top_10_customers_by_revenue
)

@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'customer_id': [1001, 1002, 1001, 1003, 1004, 1005, 1002, 1001, 1003, 1005],
        'order_date': [
            '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-02-01',
            '2023-02-01', '2023-02-15', '2023-02-20', '2023-03-01', '2023-03-02'
        ],
        'product_id': [2001, 2002, 2001, 2003, 2004, 2002, 2001, 2003, 2004, 2002],
        'product_name': [
            'Product A', 'Product B', 'Product A', 'Product C', 'Product D',
            'Product B', 'Product A', 'Product C', 'Product D', 'Product B'
        ],
        'product_price': [20.5, 15.0, 20.5, 25.0, 30.0, 15.0, 20.5, 25.0, 30.0, 15.0],
        'quantity': [2, 1, 3, 1, 2, 2, 1, 4, 3, 1]
    }
    df = pd.DataFrame(data)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year_month'] = df['order_date'].dt.to_period('M')
    df['revenue'] = df['product_price'] * df['quantity']
    return df

def test_compute_revenue_by_month(sample_data):
    result = compute_revenue_by_month(sample_data)
    expected = pd.Series([142.5, 210.5, 105.0], index=pd.period_range(start='2023-01', periods=3, freq='M'), name='revenue')
    assert result.equals(expected), "Test failed for compute_revenue_by_month"
    print("Test passed for compute_revenue_by_month")

def test_compute_revenue_by_product(sample_data):
    result = compute_revenue_by_product(sample_data)
    expected = pd.Series(
        [123.0, 60.0, 125.0, 150.0],
        index=['Product A', 'Product B', 'Product C', 'Product D'],
        name='revenue'
    )
    assert result.equals(expected), "Test failed for compute_revenue_by_product"
    print("Test passed for compute_revenue_by_product")

def test_compute_revenue_by_customer(sample_data):
    result = compute_revenue_by_customer(sample_data)
    expected = pd.Series(
        [202.5, 35.5, 115.0, 60.0, 45.0],
        index=[1001, 1002, 1003, 1004, 1005],
        name='revenue'
    )
    assert result.equals(expected), "Test failed for compute_revenue_by_customer"
    print("Test passed for compute_revenue_by_customer")

def test_top_10_customers_by_revenue(sample_data):
    result = top_10_customers_by_revenue(sample_data)
    expected = pd.Series(
        [202.5, 115.0, 60.0, 45.0, 35.5],
        index=[1001, 1003, 1004, 1005, 1002],
        name='revenue'
    )
    assert result.equals(expected), "Test failed for top_10_customers_by_revenue"
    print("Test passed for top_10_customers_by_revenue")

if __name__ == "__main__":
    pytest.main([__file__])
