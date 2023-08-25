import os
import dash
from dash import html
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib
from flask import send_file
from io import BytesIO

matplotlib.use('Agg')

app = dash.Dash(__name__)
server = app.server

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


@app.callback(
    Output('download-link', 'href'),
    Output('download-link', 'style'),
    [Input('generate-button', 'n_clicks')],
    prevent_initial_call=True
)
def update_link(n_clicks):
    file_name = 'my_file_from_dash.pdf'
    _path = f'./data/{file_name}'
    save_pdf(10, 1000, _path)
    return f'/download/{file_name}', {'display': 'block'}


app.layout = html.Div([
     html.Button("Generate PDF", id="generate-button"),
     html.A("Download PDF", id='download-link', href='', style={'display': 'none'})
 
])

@server.route('/download/<path:path>')
def serve_static(path):
    return send_file(f'./data/{path}', as_attachment=True, download_name=path, mimetype='application/pdf')

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
