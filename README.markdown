#live webservice
this is the live website link where you can check the results for your new data 
-- https://thrd-9has.onrender.com --


# Price Update Script README

## What is this?

This is a Python script that helps update product prices based on how much stock we have and how well items are selling. It takes two files (products.csv and sales.csv), does some calculations, and creates a new file (updated_prices.csv) with the old and new prices for each product.

## How it works

1. **Reads Data**: The script loads two files:
   - `products.csv` (has product details like stock and current price)
   - `sales.csv` (has sales info like how many were sold)

2. **Combines Data**: It matches products from both files using a unique code called "sku".

3. **Applies Pricing Rules**:
   - **Rule 1: Low Stock, High Demand** – If we’re low on stock (less than 20) but selling a lot (more than 30), the price goes up by 15%.
   - **Rule 2: Dead Stock** – If we have too much stock (more than 200) and nothing’s selling (0 sold), the price drops by 30%.
   - **Rule 3: Overstocked** – If we have a lot of stock (more than 100) but low sales (less than 20), the price drops by 10%.
   - **Rule 4: Minimum Profit** – Ensures the new price is never too low (at least 20% above the cost price).

4. **Final Touches**:
   - Rounds prices to two decimal places (like $19.99).
   - Adds a "$" to prices for clarity.
   - Saves the results to `updated_prices.csv` with just the product code (sku), old price, and new price.

## What you need

- **Python**: Make sure you have Python installed.
- **Pandas Library**: This script uses a tool called "pandas" to handle data. You can install it by typing `pip install pandas` in your command line.
- **Input Files**:
  - `products.csv` (with columns: sku, stock, current_price, cost_price)
  - `sales.csv` (with columns: sku, quantity_sold)

## How to run it

1. Save the script as something like `price_update.py`.
2. Put your `products.csv` and `sales.csv` files in the same folder as the script.
3. Open a terminal or command prompt, go to the folder, and type:
   ```
   python price_update.py
   ```
4. Check the folder for a new file called `updated_prices.csv`.

## What you get

A file (`updated_prices.csv`) with three columns:
- **sku**: The product code.
- **old_price**: The original price (with a "$").
- **new_price**: The updated price (with a "$").

## Notes

- The script only updates prices for products that appear in both input files.
- If something doesn’t match the rules, the price might stay the same (but it’ll still be checked for the minimum profit rule).
- Make sure your input files are correct, or the script might not work as expected.

If you have questions or run into issues, let me know!
