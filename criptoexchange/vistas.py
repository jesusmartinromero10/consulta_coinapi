def pideCripto():
    cripto = input("Introduzca una cripto conocida: ").upper()
    return cripto

def mostrarTipoCambio(tasa):
    print("{:.2f} € ".format(tasa))

def mostrarError(error):
    print("se ha producido el error {}".format(error))

