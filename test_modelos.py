# 15913 de 16132 (219)

from criptoexchange.modelos  import todoCoinApiIo
from config import apikey

def test_todocoin():
    todas = todoCoinApiIo()
    assert isinstance(todas, todoCoinApiIo)#hace que vea si todas es del tipo todocoinapiio
    todas.trae(apikey)
    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos)== 219

