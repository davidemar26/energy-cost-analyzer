
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Energy Cost Analyzer",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Energy Cost Analyzer")
st.write("Dashboard per l'analisi dei costi energetici.")

# Legge il CSV
dati = pd.read_csv("risultati_energia.csv", sep=";")

# Filtro per selezionare i mesi
mesi_disponibili = dati["Mese"].tolist()

mesi_selezionati = st.multiselect(
    "Seleziona i mesi da analizzare",
    options=mesi_disponibili,
    default=mesi_disponibili
)

# Filtra le righe in base alla selezione
dati_filtrati = dati[dati["Mese"].isin(mesi_selezionati)]

# Se non sono stati selezionati mesi, mostra un messaggio
if dati_filtrati.empty:
    st.info("Seleziona almeno un mese per visualizzare le statistiche.")
else:
    # Calcola le statistiche sui dati filtrati
    costo_totale = dati_filtrati["Costo_euro"].sum()
    consumo_medio = dati_filtrati["Consumo_kWh"].mean()
    numero_mesi = len(dati_filtrati)

    # Mostra le metriche
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Costo totale", f"{costo_totale:.2f} €")

    with col2:
        st.metric("Consumo medio", f"{consumo_medio:.2f} kWh")

    with col3:
        st.metric("Mesi analizzati", numero_mesi)

    
    # Individua il mese più costoso tra quelli selezionati
    indice_massimo = dati_filtrati["Costo_euro"].idxmax()
    riga_massima = dati_filtrati.loc[indice_massimo]

    st.metric(
        "Mese più costoso",
        riga_massima["Mese"],
        f'{riga_massima["Costo_euro"]:.2f} €'
    )


    st.divider()

    # Grafico dei costi mensili
    st.subheader("Costi energetici mensili")

    grafico_costi = dati_filtrati.set_index("Mese")[["Costo_euro"]]

    st.bar_chart(
        grafico_costi,
        y_label="Costo (€)",
        x_label="Mese"
    )

    # Tabella dei dati filtrati
    st.subheader("Dati mensili")
    st.dataframe(dati_filtrati, use_container_width=True)

    # Prepara il CSV filtrato per il download
    csv_filtrato = dati_filtrati.to_csv(
        index=False,
        sep=";"
    ).encode("utf-8")

    st.download_button(
        label="Scarica i dati selezionati",
        data=csv_filtrato,
        file_name="risultati_energia_filtrati.csv",
        mime="text/csv"
    )


