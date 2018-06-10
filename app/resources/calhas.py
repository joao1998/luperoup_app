from flask_restful import Resource
from app.models import Calha


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