def calcola_media(valori):
    if len(valori) == 0:
        return 0

    return sum(valori) / len(valori)


def calcola_statistiche(consumi, costi):
    consumo_totale = sum(consumi)
    consumo_medio = calcola_media(consumi)
    costo_medio = calcola_media(costi)

    return consumo_totale, consumo_medio, costo_medio