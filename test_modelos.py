# 15913 de 16132 (219)

from criptoexchange.modelos  import todoCoinApiIo, Cambio
from config import apikey

def test_todocoin():
    todas = todoCoinApiIo()
    assert isinstance(todas, todoCoinApiIo)#hace que vea si todas es del tipo todocoinapiio
    todas.trae(apikey)
    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos)== 219

def test_cambio_OK():
    btceur = Cambio("BTC")
    assert btceur.tasa is None
    assert btceur.horefecha is None
    btceur.actualiza(apikey)
    assert btceur.tasa > 0
    assert isinstance(btceur.horefecha, str)

def test_cambio_no_Ok():
    noOk = Cambio("kakatua")
    assert noOk.tasa is None
    assert noOk.horefecha is None

    #noOk.actualiza(apikey)
    
