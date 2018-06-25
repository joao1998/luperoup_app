from flask_restful import Resource, reqparse
from app.models import Perfil
from flask import flash, redirect, url_for
from app import db

parser = reqparse.RequestParser()
parser.add_argument('cor', type=str, required=True)
parser.add_argument('tipo', type=str, required=True)
parser.add_argument('referencia', type=str, required=True)
parser.add_argument('stock', type=str, required=True)


class Perfis(Resource):
    def get(self):
        perfil_browser = []
        perfis = Perfil.query.all()

        if perfis:
            for perfil in perfis:
                perfil_browser.append(
                    {"id": perfil.id,
                     "referencia": perfil.referencia,
                     "tipo": perfil.tipo,
                     "cor": perfil.cor,
                     "stock": int(perfil.stock)
                      }
                )

        return perfil_browser

    def post(self):
        args = parser.parse_args()
        print(args)

        # Procurar se ja existe rodizio com mesmo tipo
        perfil = Perfil.query.filter_by(cor=args["cor"],tipo=args["tipo"], referencia=args["referencia"]).first()

        if perfil:
            # Adicionar mais stock se ja existir rodizio
            perfil.stock = perfil.stock + int(args["stock"])
        else:
            # Cria rodizio se nao existir na base de dados comm mesmo tipo
            novo_perfil = Perfil(cor=args["cor"], referencia=args["referencia"], tipo=args["tipo"],stock=args["stock"]);
            db.session.add(novo_perfil);

        db.session.commit()

        flash('Stock alterado com sucesso!')
        return redirect(url_for('inventario_perfis'))

        return True