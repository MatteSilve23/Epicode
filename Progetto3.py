nome = "Mario Rossi"
età = 25
saldo = 1252,54
VIP = True

destinazioni = ["Parigi", "Londra", "Tokyo", "New York", "Barcellona"]
prezzi_medi = {"Parigi": 670, "Londra": 1250, "Milano": 789, "Praga": 1120, "Barcellona": 912}

class Cliente:
    def __init__(self, nome, età, VIP):
        self.nome = nome
        self.età = età
        self.VIP = VIP
        if self.VIP == True:
            self.VIP = "Sì"

        else: self.VIP = "No"

    def scheda_cliente(self):
            print (f"""
                   Nome: {self.nome}
                   Età: {self.età}
                   VIP: {self.VIP}  
               """)
            
class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata


class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio
        

        

        if cliente.VIP == "Sì":
            sconto = viaggio.prezzo * 0.10  

        else: sconto = 0

        self.importo_finale = viaggio.prezzo - sconto


    def dettagli (self):
        print("Dettagli Prenotazione:")
        self.cliente.scheda_cliente()
        print (f"""
                  Destinazione: {self.viaggio.destinazione}
                  Importo Finale: {self.importo_finale}
                  Durata: {self.viaggio.durata} giorni
               """)   

#Esempio di funzionamento delle classi
        
c1 = Cliente("Luca Brasi", 44, VIP = True)
v1 = Viaggio("Helsinky", 2200, 10)

prenotazione1 = Prenotazione(c1, v1)
prenotazione1.dettagli()


       
import numpy as np

prezzi_prenotazioni = np.random.randint(200, 2000, size = 100)
prezzo_medio = np.mean(prezzi_prenotazioni)
prezzo_massimo = np.max(prezzi_prenotazioni)
prezzo_minimo = np.min(prezzi_prenotazioni)
deviazione_std = np.std(prezzi_prenotazioni)
perc_sopra_media = np.sum(prezzi_prenotazioni > prezzo_medio) / len(prezzi_prenotazioni)*100

print (f"""
           Prezzo Medio: {prezzo_medio} €
           Prezzo Massimo: {prezzo_massimo} €
           Prezzo Minimo: {prezzo_minimo} €
           Deviazione Standard: {deviazione_std}
           Percentuale dei prezzi sopra la media: {perc_sopra_media} %
        """)
                          

import pandas as pd
dati = {
    "Cliente": ["Luca Brasi", "John Meckennie", "Lucas Lerman", "Mario Rossi", "Marco Verdi"],
    "Destinazione": ["Londra", "Tokyo", "Parigi", "New York", "Barcellona"],
    "Prezzo": [220, 350, 999, 870, 2000],
    "Giorno di Partenza": ["1-2-26", "3-15-26", "12-6-26", "22-9-26", "9-11-26"],
    "Durata": [10, 5, 3, 3, 6],
    "Incasso": [1100, 200, 320, 120, 600]

}
df = pd.DataFrame(dati)

incasso_totale = df["Incasso"].sum()
print("Incasso Totale:")
print(f"{incasso_totale} €")

incasso_medio_per_destinazione = df.groupby("Destinazione")["Incasso"].mean()
print("Incasso Medio (€)")
print(incasso_medio_per_destinazione)

ordinato = incasso_medio_per_destinazione.sort_values(ascending = False)
top_tre_destinazioni = ordinato.head(3)
print("Le Tre mete più redditizie (€)")
print(top_tre_destinazioni)

import matplotlib.pyplot as plt

plt.bar(df["Destinazione"], df["Incasso"], color = "skyblue", width = 0.6)
plt.title("Incasso per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("€")
plt.show()

date = pd.date_range("2025-01-01", periods = len(df), freq = "W")
plt.plot(date, df["Incasso"], color = "skyblue")
plt.title("Incasso Per Giorno ")
plt.ylabel("€")
plt.tight_layout()
plt.show()

plt.pie(df["Incasso"], labels = df["Destinazione"], autopct = "%1.1f%%")
plt.title("Percentuale di Vendite Per Destinazione")
plt.show()

ordina_continenti = {
    "Londra": "Europa",
    "Parigi": "Europa",
    "Tokyo": "Asia",
    "New York": "America",
    "Barcellona": "Europa"
}

df["Continente"] = df["Destinazione"].map(ordina_continenti)
print("Dati aggiornati")
print(df)

incasso_continente = df.groupby("Continente")["Incasso"].sum()
print("Incasso Totale (€)")
print(incasso_continente)

durata_media = df.groupby("Continente")["Durata"].mean()
print("Durata Media (giorni)")
print(durata_media)

df.to_csv("prenotazioni_analizzate.csv", index = False)


def best_customers(df, n=4): 
 contatore = df["Cliente"].value_counts().head(n)
 print("Clienti con Più prenotazioni:")
 print(contatore)

fig, ax1 = plt.subplots(figsize = (6,4))

ax1.bar(df["Continente"], df["Incasso"], color = "Yellow", label = "Incasso (€)")
ax1.set_xlabel("Continente")
ax1.set_ylabel("Incasso(€)")

ax2 = ax1.twinx()
ax2.plot(df["Continente"], df["Durata"], marker = "o", label = "Durata Media (giorni)")
ax2.set_ylabel("Durata Media (giorni)")

plt.title ("Incasso e Durata media per Continente")
ax1.legend()
ax2.legend()

plt.show()






