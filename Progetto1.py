#parte 1

titolo = "Il Signore degli anelli" 
n_copie = 3
prezzo_medio = 18.5
disponibilità = True
if n_copie > 0:
    disponibilità = True
else: disponibilita = False
    

print (f"Titolo: {titolo}, Copie: {n_copie}, Prezzo medio: {prezzo_medio}, Disponibilità: Disponibile" if disponibilità == True else "Non disponibile")

#parte 2
titoli = ["Il Signore degli Anelli", "Il ritratto di Dorian Gray", "Cecità", "Harry Potter", "Zanna Bianca"]
libro =  {titolo: "Il Ritratto di Dorian Gray", n_copie : 3, prezzo_medio: 15.5, disponibilità: True}
utenti = {"Matteo Silvestri", "Luca Lari", "Simone Poleschi", "Matteo Fagni", "Luca Bonelli", "Giacomo Bonvicini", "Guglielmo Pacini"}

#parte 3
class LibroNonDisponibileError(Exception):
    pass


class Libro:
    def __init__(self, titolo, autore, anno, n_copie):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.n_copie = n_copie

    def info(self):
        print(f"Titolo: {titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie Disponibili: {n_copie}") 

class Utente:
    def __init__(self, nome, età, id_utente):
        self.nome = nome
        self.età = età
        self.id_utente = id_utente

    def scheda(self):
        print(f"Nome: {self.nome}, Età: {self.età}, ID Utente: {self.id_utente}")

class Prestito:
    def __init__ (self, giorni, utente, libro):
        self.giorni = giorni
        self.utente = utente
        self.libro = libro
       

    def dettagli(self):
        print (f"Dati Utente: {self.utente.nome, self.utente.età, self.utente.id_utente}, Dati Libro: {self.libro.titolo, self.libro.autore, self.libro.anno, self.libro.n_copie}, Durata: {self.giorni} giorni.")

#parte 4


    def presta_libro(self):

         nuovo_prestito = Prestito(self.giorni, self.utente, self.libro)
         nuovo_prestito.dettagli()

         if self.libro.n_copie >= 1:
            self.libro.n_copie -= 1
           
           
         else:


          raise LibroNonDisponibileError ("Libro non disponibile")    

utente1 = Utente("Luca Bonelli", 26, 6969)
utente2 = Utente("Matteo Fagni", 26, 6868)
utente3 = Utente("Giacomo Bonvicini", 26, 6767)
libro1 = Libro("Il Signore degli Anelli", "Tolkien", 1954, 3)
libro2 = Libro("Cecità","Saramago", 1998, 2)
libro3 = Libro("Harry Potter", "Rawling", 1999, 1)

prestito1 = Prestito(30, utente1, libro1)
prestito1.presta_libro()

prestito2 = Prestito(30, utente2, libro2)
prestito2.presta_libro()

prestito3 = Prestito(30, utente3, libro3)
prestito3.presta_libro()

lista_aggiornata = f"""
      Titolo: {libro1.titolo}, Copie Disponibili: {libro1.n_copie}
      Titolo: {libro2.titolo}, Copie Disponibili: {libro2.n_copie}
      Titolo: {libro3.titolo}, Copie Disponibili: {libro3.n_copie}
      """


print (lista_aggiornata)