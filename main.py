
import csv

nome_file = "risultati_energia.csv"

mesi = []
consumi = []
prezzi = []
costi = []

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
                nome_mese = riga["Mese"]
                consumo_kwh = float(riga["Consumo_kWh"])
                prezzo_kwh = float(riga["Prezzo_euro_kWh"])

                if consumo_kwh < 0 or prezzo_kwh < 0:
                    raise ValueError(
                        "Consumo e prezzo non possono essere negativi."
                    )

            except (ValueError, KeyError) as errore:
                raise ValueError(
                    f"Errore alla riga {numero_riga}: {errore}"
                )

            costo_totale = consumo_kwh * prezzo_kwh

            mesi.append(nome_mese)
            consumi.append(consumo_kwh)
            prezzi.append(prezzo_kwh)
            costi.append(costo_totale)

    if not costi:
        print("Il file non contiene dati da analizzare.")

    else:
        print("\n--- Riepilogo costi energetici ---")

        for i in range(len(mesi)):
            print(
                f"{mesi[i]}: {consumi[i]:.2f} kWh -> "
                f"{costi[i]:.2f} euro"
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

        indice_massimo = costi.index(max(costi))
        print(f"Mese più costoso: {mesi[indice_massimo]}")

except FileNotFoundError:
    print(f"Errore: il file '{nome_file}' non esiste.")

except (ValueError, KeyError) as errore:
    print(f"Errore nei dati del CSV: {errore}")

