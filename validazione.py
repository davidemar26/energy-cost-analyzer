
def valida_mese(nome_mese, mesi_visti):
    mesi_ordine = {
        "gennaio": 1,
        "febbraio": 2,
        "marzo": 3,
        "aprile": 4,
        "maggio": 5,
        "giugno": 6,
        "luglio": 7,
        "agosto": 8,
        "settembre": 9,
        "ottobre": 10,
        "novembre": 11,
        "dicembre": 12
    }

    nome_normalizzato = nome_mese.strip().lower()

    if nome_normalizzato not in mesi_ordine:
        raise ValueError(f"Mese non riconosciuto: {nome_mese}")

    if nome_normalizzato in mesi_visti:
        raise ValueError(f"Mese duplicato: {nome_mese}")

    return nome_normalizzato


def valida_valori(consumo, prezzo):
    if consumo < 0 or prezzo < 0:
        raise ValueError(
            "Consumo e prezzo non possono essere negativi."
        )
