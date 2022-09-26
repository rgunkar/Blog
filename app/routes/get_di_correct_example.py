from flask import render_template

from app import app

@app.route('/get_correct_di_aapi2')
def get_correct_di_aapi2():
    return render_template('correct_di_aapi2.html', title='Solid Principle')