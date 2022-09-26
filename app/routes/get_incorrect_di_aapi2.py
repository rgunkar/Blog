from flask import render_template

from app import app


@app.route('/get_incorrect_di_aapi2')
def get_incorrect_di_aapi2():
    return render_template('incorrect_di_aapi2.html', title='Solid Principle')
