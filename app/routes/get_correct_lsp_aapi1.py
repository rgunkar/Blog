from flask import render_template

from app import app


@app.route('/get_correct_lsp_aapi1')
def get_correct_lsp_aapi1():
    return render_template('correct_lsp_aapi1.html', title='Solid Principle')
