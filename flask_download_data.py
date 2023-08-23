
import os
import matplotlib
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from io import BytesIO
from flask import Flask, send_file
from matplotlib.backends.backend_pdf import PdfPages


app = Flask(__name__)

def generate_data(n_cols, n_rows) -> pd.DataFrame:
    data = np.random.normal(0, 1, (n_cols, n_rows))
    cols = [f"C{i+1:03d}" for i in range(n_cols)]
    return pd.DataFrame(data=data.T, columns=cols)
        
def generate_binary(n_cols, n_rows):
    df = generate_data(n_cols, n_rows)
    buffer = BytesIO()
    with PdfPages(buffer) as pdf_pages:
        ax = df.plot()
        pdf_pages.savefig(ax.get_figure())
        plt.close(ax.get_figure())
    return buffer

def save_pdf(n_cols, n_rows, path):
    buffer = generate_binary(n_cols, n_rows)
    binary = buffer.getvalue()

    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'wb') as file:
        file.write(binary)

@app.route('/')
def root():
    return """<a href="/download-pdf"><button>Download PDF</button></a>"""

@app.route('/download-pdf')
def download_pdf():
    print('download_pdf')
    try:
        file_name = 'my_file.pdf'
        _path = f'./data/{file_name}'
        save_pdf(10, 1000, _path)
        r = send_file(
            path_or_file=_path,
            as_attachment=True,
            download_name=file_name,
            mimetype='application/pdf'
        )
    except Exception as e:
        print(e)
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0')
