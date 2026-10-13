mesi = []
costi = []

numero_mesi = int(input("Quanti mesi vuoi analizzare? "))

for i in range(numero_mesi):
    print(f"\nMese {i + 1}")

    nome_mese = input("Nome del mese: ")
    consumo_kwh = float(input("Consumo in kWh: "))
    prezzo_kwh = float(input("Prezzo per kWh in euro: "))

    if consumo_kwh < 0 or prezzo_kwh < 0:
        print("Errore: consumo e prezzo non possono essere negativi.")
        break

    costo_totale = consumo_kwh * prezzo_kwh

    mesi.append(nome_mese)
    costi.append(costo_totale)

if len(costi) == numero_mesi and numero_mesi > 0:
    print("\n--- Riepilogo costi energetici ---")

    for i in range(numero_mesi):
        print(f"{mesi[i]}: {costi[i]:.2f} euro")

    print(f"\nCosto complessivo: {sum(costi):.2f} euro")

    indice_massimo = costi.index(max(costi))
    print(f"Mese più costoso: {mesi[indice_massimo]}")