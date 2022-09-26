from flask import render_template
from app import app


# ------------------------------------------------------------------------
# Open Closed Principles
class BlockAddress:
    def return_builing_number(self):
        return "B-28"


class FullAddress(BlockAddress):
    def __repr__(self):
        return "City:- Surat" + "block: " + self.return_builing_number()


# ----------------------------------------------------------------------------------
@app.route('/get_hero_address')
def get_hero_address():
    hero_address = FullAddress()
    return render_template('hero_address.html', hero_address=hero_address, title='Solid Principle')
