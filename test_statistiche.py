from statistiche import calcola_media, calcola_statistiche

def test_calcola_media():
    assert calcola_media([120, 150, 100]) == 370 / 3

def calcola_media_lista_vuota():
    assert calcola_media([]) == 0

def test_calcola_statistiche():
    totale, media, costo_medio = calcola_statistiche(
        [120, 150, 100],
        [30, 37.5, 25]
    )

    assert totale == 370
    assert abs(media - 123.3333333333) < 0.0001
    assert abs(costo_medio - 30.8333333333) < 0.0001 


def test_calcola_media_lista_vuota():
    assert calcola_media([]) == 0