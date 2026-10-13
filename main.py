
import csv

def calcola_media(valori):
    if len(valori) == 0:
        return 0

    return sum(valori) / len(valori)


def calcola_statistiche(consumi, costi):
    consumo_totale = sum(consumi)
    consumo_medio = calcola_media(consumi)
    costo_medio = calcola_media(costi)

    return consumo_totale, consumo_medio, costo_medio


def numero_mese(nome_mese):
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

    nome_mese = nome_mese.strip().lower()

    if nome_mese not in mesi_ordine:
        raise ValueError(f"Mese non riconosciuto: {nome_mese}")

    return mesi_ordine[nome_mese]


nome_file = "risultati_energia.csv"
dati_mensili = []

try:
    with open(
        nome_file,
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        lettore = csv.DictReader(file, delimiter=";")

        for numero_riga, riga in enumerate(lettore, start=2):
            try:
                nome_mese = riga["Mese"].strip()
                consumo_kwh = float(riga["Consumo_kWh"])
                prezzo_kwh = float(riga["Prezzo_euro_kWh"])

                if consumo_kwh < 0 or prezzo_kwh < 0:
                    raise ValueError(
                        "Consumo e prezzo non possono essere negativi."
                    )

                numero_mese(nome_mese)

            except (ValueError, KeyError, AttributeError) as errore:
                raise ValueError(
                    f"Errore alla riga {numero_riga}: {errore}"
                )

            costo_totale = consumo_kwh * prezzo_kwh

            dati_mensili.append({
                "mese": nome_mese,
                "consumo": consumo_kwh,
                "prezzo": prezzo_kwh,
                "costo": costo_totale
            })

    if not dati_mensili:
        print("Il file non contiene dati da analizzare.")

    else:
        dati_mensili = sorted(
            dati_mensili,
            key=lambda dato: numero_mese(dato["mese"])
        )

        mesi = [dato["mese"] for dato in dati_mensili]
        consumi = [dato["consumo"] for dato in dati_mensili]
        costi = [dato["costo"] for dato in dati_mensili]

        print("\n--- Riepilogo costi energetici ---")

        for i, dato in enumerate(dati_mensili):
            print(
                f"{dato['mese']}: {dato['consumo']:.2f} kWh -> "
                f"{dato['costo']:.2f} euro"
            )

            if i > 0:
                costo_precedente = costi[i - 1]

                if costo_precedente > 0:
                    variazione = (
                        (costi[i] - costo_precedente)
                        / costo_precedente
                    ) * 100

                    if variazione > 0:
                        print(f"  Aumento: +{variazione:.1f}%")
                    elif variazione < 0:
                        print(f"  Diminuzione: {variazione:.1f}%")
                    else:
                        print("  Variazione: 0.0%")
                else:
                    print("  Variazione: N/D (costo precedente zero)")

        print(f"\nCosto complessivo: {sum(costi):.2f} euro")

        totale_kwh, media_kwh, media_euro = calcola_statistiche(
            consumi, costi
        )

        print(f"Consumo totale: {totale_kwh:.2f} kWh")
        print(f"Consumo medio mensile: {media_kwh:.2f} kWh")
        print(f"Costo medio mensile: {media_euro:.2f} euro")

        indice_massimo = costi.index(max(costi))
        print(f"Mese più costoso: {mesi[indice_massimo]}")

except FileNotFoundError:
    print(f"Errore: il file '{nome_file}' non esiste.")

except (ValueError, KeyError) as errore:
    print(f"Errore nei dati del CSV: {errore}")

