# -*- coding: utf-8 -*-
# Autors: Adams Pastars ap25167
# MODELIS (Model) - atbild par datiem un datu bāzi.
# Šeit notiek visas darbības ar datu bāzi: pievienošana, lasīšana, labošana, dzēšana.

import sqlite3

# Datu bāzes faila nosaukums
DB_NOSAUKUMS = "filmas.db"


class FilmModel:

    # Izveido savienojumu ar datu bāzi
    @staticmethod
    def savienojums():
        savieno = sqlite3.connect(DB_NOSAUKUMS)
        savieno.row_factory = sqlite3.Row  # ļauj piekļūt kolonnām pēc nosaukuma
        return savieno

    # Izveido tabulu, ja tās vēl nav, un pievieno dažas filmas kā piemēru
    @staticmethod
    def init_db():
        savieno = FilmModel.savienojums()
        savieno.execute("""
            CREATE TABLE IF NOT EXISTS filmas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nosaukums TEXT NOT NULL,
                zanrs TEXT NOT NULL,
                gads INTEGER NOT NULL,
                vertejums REAL NOT NULL,
                attels TEXT NOT NULL DEFAULT ''
            )
        """)
        savieno.commit()

        # Ja tabula ir tukša, pievienojam dažas piemēra filmas
        # (attēli ir brīvi pieejami no Wikimedia Commons - saites darbojas)
        skaits = savieno.execute("SELECT COUNT(*) FROM filmas").fetchone()[0]
        if skaits == 0:
            piemeri = [
                ("Better Call Saul", "Krimināldrāma", 2015, 10,
                 "https://i.imgur.com/2Br3y2q.jpeg"),
                ("Breaking Bad", "Krimināldrāma", 2008, 8,
                 "https://i.imgur.com/aAEq8UC.jpeg"),
                ("No Country for Old Men", "Trilleris", 2007, 7,
                 "https://i.imgur.com/i2cY7XV.jpeg"),
                ("Inglourious Basterds", "Kara filma", 2009, 9,
                 "https://i.imgur.com/Ro4hbX1.jpeg"),
            ]
            savieno.executemany(
                "INSERT INTO filmas (nosaukums, zanrs, gads, vertejums, attels) VALUES (?, ?, ?, ?, ?)",
                piemeri
            )
            savieno.commit()
        savieno.close()

    # Atgriež visas filmas (ar iespēju meklēt pēc nosaukuma)
    @staticmethod
    def visas(meklet=""):
        savieno = FilmModel.savienojums()
        if meklet:
            rezultats = savieno.execute(
                "SELECT * FROM filmas WHERE nosaukums LIKE ? ORDER BY vertejums DESC",
                ("%" + meklet + "%",)
            ).fetchall()
        else:
            rezultats = savieno.execute(
                "SELECT * FROM filmas ORDER BY vertejums DESC"
            ).fetchall()
        savieno.close()
        return rezultats

    # Atgriež vienu filmu pēc tās ID
    @staticmethod
    def viena(film_id):
        savieno = FilmModel.savienojums()
        rezultats = savieno.execute(
            "SELECT * FROM filmas WHERE id = ?", (film_id,)
        ).fetchone()
        savieno.close()
        return rezultats

    # Pievieno jaunu filmu
    @staticmethod
    def pievienot(nosaukums, zanrs, gads, vertejums, attels):
        savieno = FilmModel.savienojums()
        savieno.execute(
            "INSERT INTO filmas (nosaukums, zanrs, gads, vertejums, attels) VALUES (?, ?, ?, ?, ?)",
            (nosaukums, zanrs, gads, vertejums, attels)
        )
        savieno.commit()
        savieno.close()

    # Labo esošu filmu
    @staticmethod
    def labot(film_id, nosaukums, zanrs, gads, vertejums, attels):
        savieno = FilmModel.savienojums()
        savieno.execute(
            "UPDATE filmas SET nosaukums=?, zanrs=?, gads=?, vertejums=?, attels=? WHERE id=?",
            (nosaukums, zanrs, gads, vertejums, attels, film_id)
        )
        savieno.commit()
        savieno.close()

    # Dzēš filmu
    @staticmethod
    def dzest(film_id):
        savieno = FilmModel.savienojums()
        savieno.execute("DELETE FROM filmas WHERE id = ?", (film_id,))
        savieno.commit()
        savieno.close()
