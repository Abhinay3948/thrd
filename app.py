from flask import Flask, request, send_file, render_template
import os
import backend

app = Flask(__name__)

# Store the output file path globally for download
output_file_path = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_files():
    global output_file_path
    try:
        products_file = request.files['products']
        sales_file = request.files['sales']

        products_path = 'temp_products.csv'
        sales_path = 'temp_sales.csv'
        products_file.save(products_path)
        sales_file.save(sales_path)

        output_file_path = 'updated_prices.csv'
        backend.process_csv_files(products_path, sales_path, output_file_path)

        # Clean up temporary input files
        for file_path in [products_path, sales_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

        return '', 200
    except Exception as e:
        return str(e), 500

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/download')
def download_file():
    global output_file_path
    if output_file_path and os.path.exists(output_file_path):
        return send_file(output_file_path, as_attachment=True, download_name='updated_prices.csv')
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)