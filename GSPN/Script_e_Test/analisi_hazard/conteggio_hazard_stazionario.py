import pandas as pd

# Caricamento del CSV con separatore corretto
df = pd.read_csv("Hazard3.csv", sep=';')

# Pulizia intestazioni e conversione numeri
df.columns = df.columns.str.strip()
df['Value'] = df['Value'].str.replace(',', '.').astype(float)

# Filtro hazard: nessun infermiere, nessun medico, ma allarme attivo
hazard_df = df[
    (df['P_InfermieriDisponibili'] == 0) &
    (df['P_MediciDisponibili'] == 0) &
    (df['P_AllarmeGenerato'] > 0)
]

# Somma delle probabilità
hazard_prob = hazard_df['Value'].sum()

# Stampa
print(f"Probabilità totale in stato di hazard: {hazard_prob:.6f}")
