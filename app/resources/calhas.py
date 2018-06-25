from flask_restful import Resource, reqparse
from app.models import Calha
from flask import flash, redirect, url_for
from app import db


# Define argumentos que sao necessario no post
parser = reqparse.RequestParser()
parser.add_argument('tipo')
parser.add_argument('cor')
parser.add_argument('referencia')
parser.add_argument('stock')


class Calhas(Resource):

    def get(self):
        calhas_browser = []
        calhas = Calha.query.all()

        if calhas:
            for calha in calhas:
                calhas_browser.append(
                    {"id": calha.id,
                     "tipo": calha.tipo,
                     "cor": calha.cor,
                     "referencia": calha.referencia,
                     "stock": int(calha.stock)
                     }
                )

        return calhas_browser

    def post(self):
        args = parser.parse_args()
        print(args)

        # Procurar se ja existe melamina com mesma cor e espessura
        calha = Calha.query.filter_by(cor=args["cor"], tipo=args["tipo"], referencia=args["referencia"]).first()

        if calha:
            # Adicionar mais stock se ja existir melamina
            calha.stock = calha.stock + int(args["stock"])
        else:
            # Cria melamina se nao existir na base de dados comm mesma cor e espessura
            nova_calha = Calha(cor=args["cor"], tipo=args["tipo"], referencia=args["referencia"], stock=args["stock"])
            db.session.add(nova_calha)

        db.session.commit()

        flash('Stock alterado com sucesso!')
        return redirect(url_for('inventario_calhas'))

        return True

