from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():

    df = pd.read_csv('data/Relatorio_operadoras.csv',encoding='latin-1', on_bad_lines='skip')

    return df.to_html()



if(__name__ == '__main__'):
    app.run(debug=True)
