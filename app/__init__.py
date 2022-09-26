from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import index
from app.routes import get_hero_specs
from app.routes import get_hero_address
from app.routes import get_animal_properties
from app.routes import get_incorrect_di_aapi2, get_di_correct_example
