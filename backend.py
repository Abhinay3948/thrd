import pandas as pd

def process_csv_files(products_path, sales_path, output_path):
    # Read the csv files
    df1 = pd.read_csv(products_path)
    df2 = pd.read_csv(sales_path)
    
    # Set the sku as primary key to merge the rows based on the key value
    df1.set_index('sku', inplace=True)
    df2.set_index('sku', inplace=True)
    
    result = pd.concat([df1, df2], axis=1, join='inner')
    
    # Rule 1 – Low Stock, High Demand (Highest Priority)
    rule1 = (result['stock'] < 20) & (result['quantity_sold'] > 30)
    result.loc[rule1, 'new_price'] = result.loc[rule1, 'current_price'] * 1.15
    
    # Rule 2 – Dead Stock (Second Priority)
    rule2 = (result['stock'] > 200) & (result['quantity_sold'] == 0)
    rule2 = rule2 & ~rule1
    result.loc[rule2, 'new_price'] = result.loc[rule2, 'current_price'] * 0.7
    
    # Rule 3 – Overstocked Inventory (Third Priority)
    rule3 = (result['stock'] > 100) & (result['quantity_sold'] < 20)
    rule3 = rule3 & ~rule1 & ~rule2
    result.loc[rule3, 'new_price'] = result.loc[rule3, 'current_price'] * 0.9
    
    # Rule 4 – Minimum Profit Constraint (Always Applied Last)
    min_pr = result['cost_price'] * 1.2
    below_min_pr = result['new_price'] < min_pr
    result.loc[below_min_pr, 'new_price'] = min_pr[below_min_pr]
    
    # Apply Final Rounding
    result['new_price'] = result['new_price'].round(2)
    
    # Rename the column name
    result.rename(columns={"current_price": "old_price"}, inplace=True)
    
    # Reset the index to turn 'sku' back into a column
    result.reset_index(inplace=True)
    
    # Select only the required columns for the final report
    final_report = result[['sku', 'old_price', 'new_price']]
    
    # Format the price columns to include dollar sign
    final_report['old_price'] = '$' + final_report['old_price'].astype(str)
    final_report['new_price'] = '$' + final_report['new_price'].astype(str)
    
    # Save the final report
    final_report.to_csv(output_path, index=False)