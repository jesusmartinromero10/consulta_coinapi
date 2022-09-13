
from criptoexchange.modelos import Cambio, ModelError, todoCoinApiIo
from config import apikey

todas = todoCoinApiIo()
todas.trae(apikey)

print("{} de {}".format(len(todas.criptos), len(todas.criptos) + len(todas.no_criptos)))

cripto = input("introduzca una cripto conocida: ").upper()
while cripto != "" :
    if cripto in todas.criptos:
        tipoCambio = Cambio(cripto)
        try:
            tipoCambio.actualiza(apikey)

            print("{:.2f} €" .format(tipoCambio.tasa))

        except ModelError as mensaje:
            print("Se a producido el error {}".format(mensaje))
    
    cripto = input("introduzca una cripto conocida; ").upper()

