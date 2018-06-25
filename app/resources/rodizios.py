from flask_restful import Resource, reqparse
from app.models import Rodizio
from flask import flash, redirect, url_for
from app import db


parser = reqparse.RequestParser()
parser.add_argument('tipo', type=str, required=True)
parser.add_argument('stock', type=str, required=True)


class Rodizios(Resource):

    def get(self):
        rodizio_browser = []
        rodizios = Rodizio.query.all()

        if rodizios:
            for rodizio in rodizios:
                rodizio_browser.append(
                    {"id": rodizio.id,
                     "tipo": rodizio.tipo,
                     "stock": int(rodizio.stock),
                      }
                )

        return rodizio_browser

    def post(self):
        args = parser.parse_args()
        print(args)

        # Procurar se ja existe rodizio com mesmo tipo
        rodizio = Rodizio.query.filter_by(tipo=args["tipo"]).first()

        if rodizio:
            # Adicionar mais stock se ja existir rodizio
            rodizio.stock = rodizio.stock + int(args["stock"])
        else:
            # Cria rodizio se nao existir na base de dados comm mesmo tipo
            novo_rodizio = Rodizio(tipo=args["tipo"], stock=args["stock"])
            db.session.add(novo_rodizio)

        db.session.commit()

        flash('Stock alterado com sucesso!')
        return redirect(url_for('inventario_rodizios'))

        return True