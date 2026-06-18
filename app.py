# -*- coding: utf-8 -*-
# Autors: Adams Pastars ap25167
# Filmu katalogs - MVC tīmekļa lietotne (Flask)
# Šis ir galvenais fails, kas palaiž lietotni un savieno visus kontrolierus.

from flask import Flask
from models.film_model import FilmModel
from controllers.film_controller import film_bp

# Izveidojam Flask lietotni
app = Flask(__name__)
app.secret_key = "ap25167"

# Sagatavojam datu bāzi (izveido tabulu, ja tās vēl nav)
FilmModel.init_db()

# Reģistrējam kontrolieri (maršrutus)
app.register_blueprint(film_bp)

# Palaižam serveri
if __name__ == "__main__":
    app.run(debug=True)
