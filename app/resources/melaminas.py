from flask_restful import Resource, reqparse
from app.models import Melamina
from flask import flash, redirect, url_for
from app import db

parser = reqparse.RequestParser()
parser.add_argument('cor', type=str, required=True)
parser.add_argument('espessura', type=str, required=True)
parser.add_argument('stock', type=str, required=True)


class Melaminas(Resource):

    def get(self):
        melamina_browser = []
        melaminas = Melamina.query.all()

        if melaminas:
            for melamina in melaminas:
                melamina_browser.append(
                    {"id": melamina.id,
                     "espessura": melamina.espessura,
                     "cor": melamina.cor,
                     "stock": int(melamina.stock)
                      }
                )

        return melamina_browser

    def post(self):
        args = parser.parse_args()
        print(args)

        # Procurar se ja existe melamina com mesma cor e espessura
        melamina = Melamina.query.filter_by(cor=args["cor"], espessura=args["espessura"]).first()

        if melamina:
            # Adicionar mais stock se ja existir melamina
            melamina.stock = melamina.stock + int(args["stock"])
        else:
            # Cria melamina se nao existir na base de dados comm mesma cor e espessura
            nova_melamina = Melamina(cor=args["cor"], espessura=args["espessura"], stock=args["stock"])
            db.session.add(nova_melamina)

        db.session.commit()

        flash('Stock alterado com sucesso!')
        return redirect(url_for('inventario_melaminas'))

        return True
