from flask import render_template

from app import app


@app.route('/get_incorrect_lsp_aapi1')
def get_incorrect_lsp_aapi1():
    return render_template('incorrect_lsp_aapi1.html', title='Solid Principle')
