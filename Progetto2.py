nome1 = "Marco"
cognome1 = "Bianchi"
codice_fiscale1 = "BNCMRC88A21G452Y"
età1 = 45
peso1 = 88.5
analisi1 = ["emocromo, colesterolo, urine"]


nome2 = "Edoardo"
cognome2 = "Balli"
codice_fiscale2 = "BLLEDD98A17G653W"
età2 = 35
peso2 = 77.3
analisi2 = ["feci", "urine", "colesterolo"]


nome3 = "Franco"
cognome3 = "Lurti"
codice_fiscalE3= "LRTFRC76A12G345Z"
età3 = 29
peso3 = 82.5
analisi3 = ["emocromo", "ferro", "urine"]





class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, età, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.età = età
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = risultati_analisi

    def scheda_personale(self):
            print(f"Dati principali: {self.nome}, {self.cognome}, {self.codice_fiscale}, {self.età} anni, {self.peso} kg, {self.analisi_effettuate}")
            
class Medico:
     def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

     def visita_paziente(self, paziente):
        self.paziente = paziente
        print (f"Il dottor {self.cognome} sta visitando {self.paziente.nome} {self.paziente.cognome}")

 

class Analisi:
     def __init__(self, tipo_analisi, risultato):
        self.tipo_analisi = tipo_analisi
        self.risultato = risultato
                        
        def valuta(self, max, min):
             if self.risulato >= min and self.risultato <= max:
                print ("Il valore è nella norma")
             else: print ("Il valore è fuori dai parametri!")



import numpy as np

valori = np.array([100.05, 99.5, 87.4, 69.69, 88.00, 100.00, 78.6, 82.00, 89.99, 95.5])
media = np.mean([valori])
massimo = np.max([valori])
minimo = np.min([valori])
deviazione_std = np.std([valori])

analisi1 = Analisi("emocromo", 110)
analisi2 = Analisi("urine", 120)
analisi3 = Analisi("colesterolo", 240)
risultati_analisi = np.array([analisi1.risultato, analisi2.risultato, analisi3.risultato])
Paziente.risultati_analisi = risultati_analisi

def statistiche_analisi(self, risultati_analisi):

    stampa = f"""
                               {self.nome} {self.cognome}
           Tipo di analisi effettuate: {self.analisi_effettuate[0]}                    
           Media: {np.mean(risultati_analisi)}
           Massimo: {np.max(risultati_analisi)} 
           Minimo: {np.min(risultati_analisi)}
           Deviazione Standard: {np.std(risultati_analisi)}
           """
    print(stampa)

Paziente.statistiche_analisi = statistiche_analisi


def main():

    medico1 = Medico("Luca", "Brasi", "Gastroenterologia")
    medico2 = Medico("Michael", "Corleone", "Neurologia")
    medico3 = Medico("Frank", "Lucas", "Cardiologia")

    paziente1 = Paziente("Mattia", "Lorenzi", "LRZMTT99A23G456W", 27, 88.5, ["colesterolo, emocromo, ferro"], [113, 113, 98.3])
    paziente2 = Paziente("Leonardo", "Lucci", "LCCLND88A24G466X", 34, 99.2, ["emocromo","ferro", "piastrine"], [110, 115, 97.5])
    paziente3 = Paziente("Giorgio", "Tesi", "TSIGRG77A25G476Y", 41, 79.8, ["colesterolo", "emocromo", "urine"], [120, 130, 105.6])
    paziente4 = Paziente("Simone", "Poleschi", "PLSSMN85A26G486Z", 30, 85.3, ["colesterolo", "ferro", "urine"], [140, 125, 110.2])
    paziente5 = Paziente("Luca", "Lari", "LRILCU92A27G496W", 29, 90.1, ["emocromo", "ferro", "piastrine"], [115, 120, 99.9])

    paziente1.scheda_personale()
    paziente2.scheda_personale()
    paziente3.scheda_personale()
    paziente4.scheda_personale()
    paziente5.scheda_personale()

    medico1.visita_paziente(paziente1)
    medico2.visita_paziente(paziente2)
    medico3.visita_paziente(paziente3)

    paziente1.statistiche_analisi(paziente1.risultati_analisi)
    paziente2.statistiche_analisi(paziente2.risultati_analisi)
    paziente3.statistiche_analisi(paziente3.risultati_analisi)
    paziente4.statistiche_analisi(paziente4.risultati_analisi)
    paziente5.statistiche_analisi(paziente5.risultati_analisi)

if __name__ == "__main__":
    main()

                
