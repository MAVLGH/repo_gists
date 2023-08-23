from flask import Flask, send_file

app = Flask(__name__)

@app.route('/download-pdf')
def download_pdf():
    path_to_pdf = 'path/to/yourfile.pdf'
    return send_file(
        path_to_pdf,
        as_attachment=True,
        attachment_filename='yourfile.pdf',
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run()
