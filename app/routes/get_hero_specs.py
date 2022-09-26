from flask import render_template
from app import app


# SRP
class HasHealth:
    def damage_take(self):
        return "Health - 50"

    def is_alive(self):
        return True

    def is_dead(self):
        return False


class CanAttack:
    def damage_make(self):
        return "100"


# We can create all new class for new specs

class Hero:
    def __init__(self, name):
        self.name = name


# It will have only single reason to change now, that is for returning another spec
class ReturnHeroSpec(Hero, CanAttack):

    def __repr__(self):
        return self.name + "has Attack Power:" + self.damage_make()


@app.route('/get_hero_spec')
def get_hero_specs():
    hero_specs = ReturnHeroSpec(name="Superman")
    return render_template('hero.html', hero_specs=hero_specs, title='Solid Principle')
