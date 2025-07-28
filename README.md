# Verifica Formale e Analisi Stocastica di un Sistema di Emergenza Ospedaliero

## 📌 Descrizione del progetto

Questo progetto affronta la modellazione, la verifica e l'analisi prestazionale di un sistema critico per la gestione di pazienti in un'unità di terapia intensiva. L'obiettivo è analizzare il comportamento del sistema in situazioni di allarme e valutare l'efficacia delle risorse disponibili (medici, infermieri, letti) tramite tecniche formali e strumenti di simulazione.

Il progetto è suddiviso in due approcci principali:

- 📈 **Analisi prestazionale** con GSPN (Generalized Stochastic Petri Nets)
- 🔍 **Verifica formale** con SMV (CTL e LTL)  

---

## 🔁 Analisi Prestazionale (GSPN)

La rete stocastica è modellata in **PIPE2** e analizzata in diverse configurazioni di risorse (letti, medici, infermieri). L'obiettivo è misurare:

- ✅ Probabilità di evento critico 
- 🛏️ Tasso di occupazione medio dei letti
- 👩‍⚕️ Probabilità che il trattamento sia eseguito da un medico
- 📤 Throughput complessivo del sistema

I dati sono ottenuti da simulazione e analisi stazionaria, con supporto di script Python per estrazioni personalizzate.

---

## 🧮 Verifica Formale (SMV)

Sono stati sviluppati due modelli:

- `Centralizzato.smv`: modello centralizzato a singolo processo
- `Multiprocesso.smv`: modello multiprocesso, con pazienti modellati individualmente

Entrambi i modelli sono stati verificati usando specifiche CTL e LTL per garantire proprietà di sicurezza e corretto intervento in caso di allarme.
---

## 📂 Struttura del progetto
```
Gestione-di-pazienti-in-terapia-intensiva-ICU/
├── GSPN/
│   ├── Script_e_test/
│   │   ├── analisi_hazard/
│   │   │   ├── Hazard1.csv
│   │   │   ├── Hazard2.csv
│   │   │   ├── Hazard3.csv
│   │   │   └── conteggio_hazard_stazionario.py
│   │   ├── Test_1.html
│   │   ├── Test_2.html
│   │   ├── Test_3.html
│   │   └── Valori.txt
│   └── Terapia_Intensiva.xml
├── Model_Checking/
│   ├── Centralizzato.smv
│   └── Multiprocesso.smv
├── Documentazione.pdf
└── README.md

```
---
## 🛠️ Requisiti

- NuSMV per la verifica CTL/LTL
- PIPE2 per la modellazione GSPN
- Python 3.x con `pandas` per analisi automatizzate

---
## 👥 Contributors

- [@Vincenzo D'Angelo](https://github.com/vincenzodan)
- [@Giorgio Di Costanzo](https://github.com/GiorgioDiCostanzo)

