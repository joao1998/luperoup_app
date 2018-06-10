from flask_restful import Resource
from app.models import Vidro


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
                     "stock": str(vidro.stock)
                     }
                )

        return vidro_browser