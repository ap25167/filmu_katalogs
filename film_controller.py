# -*- coding: utf-8 -*-
# Autors: Adams Pastars ap25167
# KONTROLIERIS (Controller) - savieno modeli un skatu.
# Šeit tiek apstrādāti lietotāja pieprasījumi (maršruti) un izsauktas modeļa funkcijas.

from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.film_model import FilmModel

# Blueprint apvieno visus filmu maršrutus
film_bp = Blueprint("film", __name__)


# Sākumlapa - parāda visu filmu sarakstu un meklēšanu
@film_bp.route("/")
def saraksts():
    meklet = request.args.get("meklet", "")
    filmas = FilmModel.visas(meklet)
    return render_template("saraksts.html", filmas=filmas, meklet=meklet)


# Forma jaunas filmas pievienošanai
@film_bp.route("/pievienot", methods=["GET", "POST"])
def pievienot():
    if request.method == "POST":
        FilmModel.pievienot(
            request.form["nosaukums"],
            request.form["zanrs"],
            request.form["gads"],
            request.form["vertejums"],
            request.form["attels"]
        )
        flash("Filma veiksmīgi pievienota!")
        return redirect(url_for("film.saraksts"))
    return render_template("forma.html", film=None)


# Forma esošas filmas labošanai
@film_bp.route("/labot/<int:film_id>", methods=["GET", "POST"])
def labot(film_id):
    film = FilmModel.viena(film_id)
    if request.method == "POST":
        FilmModel.labot(
            film_id,
            request.form["nosaukums"],
            request.form["zanrs"],
            request.form["gads"],
            request.form["vertejums"],
            request.form["attels"]
        )
        flash("Filma veiksmīgi labota!")
        return redirect(url_for("film.saraksts"))
    return render_template("forma.html", film=film)


# Filmas dzēšana
@film_bp.route("/dzest/<int:film_id>")
def dzest(film_id):
    FilmModel.dzest(film_id)
    flash("Filma izdzēsta.")
    return redirect(url_for("film.saraksts"))
