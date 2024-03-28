from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel('data.xlsx')  # Replace 'data.xlsx' with the name of your Excel file

    # Convert the DataFrame to an HTML table
    html_table = df.to_html(classes='table table-striped', index=False)  # Add CSS classes to style the table

    return render_template('index.html', html_table=html_table)

if __name__ == '__main__':
    app.run(debug=True)
