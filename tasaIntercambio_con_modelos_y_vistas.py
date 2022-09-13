from criptoexchange.modelos import Cambio, todoCoinApiIo, ModelError
from criptoexchange.vistas import pideCripto, mostrarTipoCambio, mostrarError
from config import apikey

class Exchanger:
    def ejecuta():
        todas= todoCoinApiIo()
        todas.trae(apikey)
        cripto = pideCripto()

        while cripto != "":
            if cripto in todas.criptos:
                tipoCambio = Cambio(cripto)
                try:
                    tipoCambio.actualiza(apikey)
                    mostrarTipoCambio(tipoCambio.tasa)
                except ModelError as variables:
                    mostrarError(variables)
            
            cripto = pideCripto()