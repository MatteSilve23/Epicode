# Parte 1


import numpy as np                                                                                              # Importazione Librerie
import pandas as pd
import matplotlib.pyplot as plt

class ErroreCreazioneArray(Exception):                                                                          #Errore personalizzato, verrà utilizzato dopo
    pass


df = pd.read_csv(r"C:\Users\User\Desktop\Epicode\vendite.csv", sep = ";", encoding = "utf-8")



# Parte 2

print(df.head())                                                                                                # Primi 5 Prodotti
print(df.shape)                                                                                                 # L'output atteso è "(30, 5)", dove 30 sono le righe e 5 le colonne
print(df.info())                                                                                                # Informazioni sul dataframe


# Parte 3 

df["Incasso"] = df["Quantità"]*df["Prezzo_unitario"]                                                            # Aggiunta della colonna "Incasso"

incasso_Totale = df["Incasso"].sum()                                                                            # Incasso totale
print(f"L'Incasso Totale è: {incasso_Totale}")

incasso_Medio = df.groupby("Negozio")["Incasso"].mean()                                                         # Incasso medio per negozio
print(f"Incasso Medio per negozio \n{incasso_Medio}")


prodotti = (
     df.groupby("Prodotto")["Quantità"]
      .sum()
      .reset_index()
      .sort_values(by = "Quantità", ascending = False)

)

top_tre_prodotti = prodotti.head(3)                                                                             # Top 3 Prodotti
print(f"Tre Prodotti più venduti \n{top_tre_prodotti}")

dati = (
    df.groupby(["Negozio", "Prodotto"], as_index = False)["Incasso"]
    .mean()
    .rename(columns ={"Incasso":"Incasso Medio"})
)

print(f"Incasso medio dei prodotti \n{dati}")                                                                              # Incasso medio per prodotto (in relazione al negozio)



# Parte 4 

quantità = df["Quantità"].to_numpy()                                                                           # Utilizzo di NumPy a fini statistici

media = np.mean(quantità)
massimo = np.max(quantità)
minimo = np.min(quantità)
deviazione_Standard = np.std(quantità)
sopra_Media = quantità > media
percentuale = np.sum(sopra_Media)/quantità.size*100

print(f"La percentuale di vendite sopra la media è: {percentuale}%")                                       

array = np.array(df[["Quantità", "Prezzo_unitario"]])
incasso = array[:, 0]*array[:, 1]

if (incasso == df["Incasso"].values).all():                                                                    # Contollo dell'errore personalizzato                     
    print("Verifica eseguita! L'array bidimensionale è stato creato correttamente e funziona.")
else: raise ErroreCreazioneArray("L'array è stato creato erroneamente")



# Parte 5

df.groupby("Negozio")["Incasso"].sum().plot(kind = "bar")                                                      # Creazione dei grafici
plt.ylabel("(€)", rotation = 90)

plt.title("Incasso Totale per negozio")
plt.show()

incasso_per_prodotto = df.groupby("Prodotto")["Incasso"].sum()
plt.pie(incasso_per_prodotto, labels = incasso_per_prodotto.index, autopct = "%1.1f%%")
plt.title("Percentuale di Incasso di ciascun prodotto")
plt.show()


df["Data"] = pd.to_datetime(df["Data"])
incasso_giornaliero = df.groupby("Data")["Incasso"].sum().sort_index()

plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker ="o")
plt.title("Incasso Totale Giornaliero")
plt.ylabel("(€)", rotation = 90)
plt.tight_layout()
plt.show()


# Parte 6 
collega = {                                                                                                     # Analisi Avanzata           
    "Cuffie": "Audio",
    "TV": "Informatica e TV",
    "PC": "Informatica e TV",
    "Smartphone": "Smartphone e Tablet",
    "Monitor": "Informatica e Tablet",
    "Lavatrice": "Elettrodomestici",
    "Lavastoviglie": "Elettrodomestici"
}

df["Categoria"] = df["Prodotto"].map(collega)

incasso_Totale_Categoria = df.groupby("Categoria")["Incasso"].sum()
print(f"Incasso totale per categoria \n{incasso_Totale_Categoria}")

quantità_Media = df["Quantità"].mean()
print(f"La quantità media venduta è: \n{quantità_Media}")

df.to_csv("vendite_analizzate.csv", index = False)


# Parte 7

incasso_per_categoria =df.groupby("Categoria")["Incasso"].sum().sort_values(ascending = False)                # Grafico combinato e funzione (facoltativo)
media_giornaliera = df.groupby("Data")["Quantità"].mean()
df["Categoria"] = df["Categoria"].astype(str)
df["Data"] = pd.to_datetime(df["Data"])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (6,4))

ax1.bar(incasso_per_categoria.index, incasso_per_categoria.values, color = "Yellow", label = "Incasso (€)")
ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso(€)")

ax2.plot(media_giornaliera.index, media_giornaliera.values, color = "skyblue", marker = "o" )
ax2.set_xlabel("Data")
ax2.set_ylabel("Quantità")

plt.title ("Quantità media giornaliera")
ax1.legend(loc = "upper right")
plt.tight_layout()
plt.show()



def top_n_prodotti(df):
    incasso_totale_prodotto = df.groupby("Prodotto")["Incasso"].sum().sort_values(ascending = False)
    print("Top 5 prodotti per Incasso(€)")
    print(incasso_totale_prodotto.head(5))
    

    
top_n_prodotti(df)



