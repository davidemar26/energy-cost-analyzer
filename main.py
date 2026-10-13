import csv

mesi = []
consumi = []
prezzi = []
costi = []

numero_mesi = int(input("Quanti mesi vuoi analizzare? "))

if numero_mesi <= 0:
    print("Errore: inserisci almeno un mese.")
else:
    dati_validi = True

    for i in range(numero_mesi):
        print(f"\nMese {i + 1}")

        nome_mese = input("Nome del mese: ")
        consumo_kwh = float(input("Consumo in kWh: "))
        prezzo_kwh = float(input("Prezzo per kWh in euro: "))

        if consumo_kwh < 0 or prezzo_kwh < 0:
            print("Errore: consumo e prezzo non possono essere negativi.")
            dati_validi = False
            break

        costo_totale = consumo_kwh * prezzo_kwh

        mesi.append(nome_mese)
        consumi.append(consumo_kwh)
        prezzi.append(prezzo_kwh)
        costi.append(costo_totale)

    if dati_validi:
        print("\n--- Riepilogo costi energetici ---")

        for i in range(numero_mesi):
            print(f"{mesi[i]}: {costi[i]:.2f} euro")

        print(f"\nCosto complessivo: {sum(costi):.2f} euro")

        indice_massimo = costi.index(max(costi))
        print(f"Mese più costoso: {mesi[indice_massimo]}")

        with open(
            "risultati_energia.csv",
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            scrittore = csv.writer(file, delimiter=";")

            scrittore.writerow([
                "Mese",
                "Consumo_kWh",
                "Prezzo_euro_kWh",
                "Costo_euro"
            ])

            for i in range(numero_mesi):
                scrittore.writerow([
                    mesi[i],
                    consumi[i],
                    prezzi[i],
                    round(costi[i], 2)
                ])

        print("\nDati salvati in risultati_energia.csv")
