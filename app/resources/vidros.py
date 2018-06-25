from flask_restful import Resource, reqparse
from app.models import Vidro
from flask import flash, redirect, url_for
from app import db

parser = reqparse.RequestParser()
parser.add_argument('cor', type=str, required=True)
parser.add_argument('tipo', type=str, required=True)
parser.add_argument('stock', type=str, required=True)



class Vidros(Resource):

    def get(self):
        vidro_browser = []
        vidros = Vidro.query.all()

        if vidros:
            for vidro in vidros:
                vidro_browser.append(
                    {"id": vidro.id,
                     "tipo": vidro.tipo,
                     "cor": vidro.cor,
                     "stock": int(vidro.stock)
                     }
                )

        return vidro_browser

    def post(self):
        args = parser.parse_args()
        print(args)

        # Procurar se ja existe vidro com mesmo tipo e cor
        vidro = Vidro.query.filter_by(cor=args["cor"], tipo=args["tipo"]).first()

        if vidro:
            # Adicionar mais stock se ja existir vidro
            vidro.stock = vidro.stock + int(args["stock"])
        else:
            # Cria vidro se nao existir na base de dados comm mesma cor e espessura
            novo_vidro = Vidro(cor=args["cor"], tipo=args["tipo"], stock=args["stock"])
            db.session.add(novo_vidro)

        db.session.commit()

        flash('Stock alterado com sucesso!')
        return redirect(url_for('inventario_vidros'))

        return True