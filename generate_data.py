# Generate synthetic retail sales data

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_sales_data(num_records=1500):
    np.random.seed(42)
    random.seed(42)
    
    categories = {
        'Electronics': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Camera'],
        'Clothing': ['T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes'],
        'Home': ['Chair', 'Table', 'Lamp', 'Pillow', 'Curtains'],
        'Books': ['Fiction Book', 'Textbook', 'Magazine', 'Comic', 'Manual'],
        'Sports': ['Basketball', 'Tennis Racket', 'Yoga Mat', 'Dumbbells', 'Running Shoes']
    }
    
    price_ranges = {
        'Electronics': (50, 1200),
        'Clothing': (15, 150),
        'Home': (20, 300),
        'Books': (5, 80),
        'Sports': (10, 200)
    }
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    data = []
    
    for i in range(num_records):
        order_id = f"ORD{str(i+1).zfill(6)}"
        random_days = random.randint(0, 365)
        order_date = start_date + timedelta(days=random_days)
        customer_id = f"CUST{random.randint(1, 500):04d}"
        
        category = random.choice(list(categories.keys()))
        product = random.choice(categories[category])
        quantity = np.random.choice([1, 2, 3, 4, 5], p=[0.5, 0.25, 0.15, 0.07, 0.03])
        
        min_price, max_price = price_ranges[category]
        price = round(random.uniform(min_price, max_price), 2)
        
        record = {
            'order_id': order_id,
            'order_date': order_date.strftime('%Y-%m-%d'),
            'customer_id': customer_id,
            'product': product,
            'category': category,
            'quantity': quantity,
            'price': price
        }
        
        data.append(record)
    
    df = pd.DataFrame(data)
    df = df.sort_values('order_date').reset_index(drop=True)
    
    return df

def main():
    print("Generating synthetic sales data...")
    
    sales_df = generate_sales_data(1500)
    
    output_path = 'sales.csv'
    sales_df.to_csv(output_path, index=False)
    
    print(f"Generated {len(sales_df)} sales records")
    print(f"Saved to: {output_path}")
    print(f"Date range: {sales_df['order_date'].min()} to {sales_df['order_date'].max()}")
    print(f"Categories: {', '.join(sales_df['category'].unique())}")
    print(f"Price range: ${sales_df['price'].min():.2f} - ${sales_df['price'].max():.2f}")

if __name__ == "__main__":
    main()