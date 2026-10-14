
import pandas as pd
import matplotlib.pyplot as plt

dati = pd.read_csv("risultati_energia.csv", sep=";")

mesi = dati["Mese"]
costi = dati["Costo_euro"]

# Calcola il costo medio
costo_medio = costi.mean()

# Crea il grafico
plt.bar(mesi, costi, label="Costo mensile")

# Aggiunge la linea della media
plt.axhline(
    y=costo_medio,
    linestyle="--",
    label=f"Costo medio: {costo_medio:.2f} €"
)

plt.title("Costi energetici mensili")
plt.xlabel("Mese")
plt.ylabel("Costo (€)")
plt.xticks(rotation=45)

plt.legend()
plt.tight_layout()
plt.show()

