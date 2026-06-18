[README.md](https://github.com/user-attachments/files/29104214/README.md)
# Filmu katalogs (MVC)

Autors: **Adams Pastars ap25167**

Vienkārša tīmekļa lietotne filmu pārvaldīšanai, izveidota ar Python (Flask)
pēc **MVC (Model-View-Controller)** dizaina šablona.

## Ko lietotne dara
- Parāda visu filmu sarakstu (sakārtotu pēc vērtējuma)
- Pievieno jaunu filmu
- Labo esošu filmu
- Dzēš filmu
- Meklē filmu pēc nosaukuma

## MVC struktūra
- **Model** (`models/film_model.py`) - darbs ar datu bāzi (SQLite)
- **View** (`templates/`) - HTML lapas, ko redz lietotājs
- **Controller** (`controllers/film_controller.py`) - apstrādā pieprasījumus, savieno modeli un skatu

## Kā palaist

1. Instalē Flask:
```
pip install flask
```

2. Palaid lietotni:
```
python app.py
```

3. Atver pārlūkā:
```
http://127.0.0.1:5000
```

Datu bāze (`filmas.db`) tiek izveidota automātiski pirmajā palaišanā.
