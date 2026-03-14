import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
   
    ordered_ids = orders['customerId']
    no_order_df = customers[~customers['id'].isin(ordered_ids)]
    result = no_order_df[['name']].rename(columns={'name': 'Customers'})
    return result