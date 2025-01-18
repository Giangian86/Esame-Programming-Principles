import json
import os

class MovieLibrary:

    """
    Classe che gestisce una collezione di film contenuta in un file JSON,
    con operazioni di aggiunta, rimozione e aggiornamento.

    Attributi d'istanza:
        json_file = percorso assoluto del file JSON
        movies = lista dei film inizializzata come vuota
    """

    # Metodo costruttore che inizializza la classe

    def __init__(self, json_file = r"C:\Users\glbac\OneDrive\Desktop\Programming Principles - Traccia (1)\movies.json"):
        self.json_file = json_file
        self.movies = []
        

    # Verifica l'esistenza del file e se confermata, leggendo il file JSON si ha accesso 
    # al secondo attributo di istanza della classe, la lista dei film

        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding='utf-8') as file:
                self.movies = json.load(file)

    # Esercizio 17 - Modifica al metodo costruttore inserendo che venga sollevata l'eccezione FileNotFoundError
    # se il file nel percorso assoluto non viene trovato 
    
        if not os.path.exists(self.json_file):
              raise FileNotFoundError(f"File not found: " r"C:\Users\glbac\OneDrive\Desktop\Programming Principles - Traccia (1)\movies.json")
    
    # Esercizio 18 - Implementazione eccezione personalizzata MovieNotFoundError

    class MovieNotFoundError(Exception):
        pass

    """ 
    Definizione della classe di eccezione MovieNotFoundError,
    che eredita le funzionalità dalla classe Exception.
    """

    def __update_json_file(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "w", encoding="utf-8") as file:
                json.dump(self.movies, file, indent=4)

    """
    Metodo privato che aggiorna il file movies.json ogni volta che l'attributo movies subisce modifiche.
    Il metodo verifica l'esistenza del percorso e apre il file in modalità scrittura, poi salva 
    le modifiche effettuate.
    """

    # Esercizio 1
    
    def get_movies(self):
        return self.movies
    
    """
    Restituisce la lista completa dei film presenti nella collezione.
    """
    
    # Esercizio 2

    def add_movie(self, title = str, director = str, year = int, genres = list[str]):
        movie_to_add = {
            "title" : title,
            "director" : director,
            "year" : year,
            "genres" : genres
        }
        self.movies.append(movie_to_add)
        self.__update_json_file()
        return movie_to_add
    
    """
    Aggiunge un nuovo film alla collezione in formato dizionario.

    Richiede l'inserimento dei parametri title (str), director(str), year (int) e genres (str) come argomenti.

    """

    # Esercizio 3

    def remove_movie(self, title = str):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                self.__update_json_file()
                return movie
        
        raise self.MovieNotFoundError("Movie was not found")
    
    """
    Rimuove un film dalla collezione cercandolo per titolo.

    Usa un ciclo for per iterare nella lista ogni film presente e
    tramite la condizione if ricerca il titolo inserito (rispettando il non case-sensitive) 
    per rimuoverlo dalla collezione.
    Se il titolo inserito non viene trovato, viene sollevata l'eccezione MovieNotFoundError.
    """
            
    # Esercizio 4

    def update_movie(self, title, director = None, year = None, genres = None):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                if director is not None:
                    movie["director"] = director
                if year is not None:
                    movie["year"] = year
                if genres is not None:
                    movie["genres"] = genres
                self.__update_json_file()
                return movie
            
        raise self.MovieNotFoundError("Movie was not found")
    
    """
    Aggiorna i dettagli di un film nella collezione.

    Usa il ciclo for per iterare nella lista ogni film presente e
    tramite la condizione if, rispettando il non case-sensitive, ricerca il film per titolo. 
    Se passati come None, i parametri del metodo sono opzionali, e verranno aggiornati nella lista solo
    se diversi da quelli da già presenti.
    Se il titolo inserito non viene trovato, viene sollevata l'eccezione MovieNotFoundError.
    """
            
    # Esercizio 5

    def get_movie_titles(self):
        titles = []
        for movie in self.movies:
            titles.append(movie["title"])
        return titles
    
    """
    Restituisce una lista contenente solo i titoli dei film presenti nella collezione.

    Crea una lista vuota, attraverso il ciclo for itera nella lista dei film 
    estrapolando il titolo di ognuno dei film presenti e salvandolo nella lista creata.
    """
    
    # Esercizio 6

    def count_movies(self):
        return len(self.movies)
    
    """
    Restituisce il numero totale dei film presenti nella collezione.

    Richiama la funzione len() che se applicata a una lista restituisce 
    il numero totale degli elementi al suo interno.
    """

    # Esercizio 7

    def get_movie_by_title(self, title):
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie

    """
    Restituisce il film corrispondente al titolo passato come argomento (non case-sensitive).
    """

    # Esercizio 8

    def get_movie_by_title_substring(self, substring):
        matched_by_substring = []
        for movie in self.movies:
            if substring.lower() in movie["title"].lower():
                matched_by_substring.append(movie)
        return matched_by_substring
    
    """
    Restituisce una lista di film ricercati attraverso una substring.

    Crea una lista vuota, attraverso il ciclo for itera nella lista dei film 
    ed estrapola solo quelli che rispettano la condizione if di contenere la sottostringa, 
    salvandoli nella lista creata.
    """

    # Esercizio 9

    def get_movies_by_year(self, year = int):
        listed_by_year = []
        for movie in self.movies:
            if movie["year"] == year:
                listed_by_year.append(movie)
        return listed_by_year
    
    """
    Restituisce una lista di film ricercati attraverso l'anno di produzione.

    Crea una lista vuota, attraverso il ciclo for itera nella lista dei film 
    ed estrapola solo quelli che rispettano la condizione if dell'anno di produzione selezionato,
    salvandoli nella lista creata.
    """

    # Esercizio 10

    def count_movies_by_director(self, director = str):
        count_movies = 0
        for movie in self.movies:
            if movie["director"].lower() == director.lower():
                count_movies += 1
        return count_movies
    
    """
    Conta e restituisce il numero totale di film presenti nella lista del regista (director) selezionato.

    Utilizza un ciclo for e un contatore, itera nella lista e ogni volta che trova una corrispondenza 
    con il nome del regista selezionato (non case-sensitive) incrementa di 1 il contatore, 
    restituendo poi il numero totale.
    """

    # Esercizio 11

    def get_movies_by_genre(self, genre = str):
        listed_by_genre = []
        for movie in self.movies:
            if any(gnr.lower() == genre.lower() for gnr in movie["genres"]):
                listed_by_genre.append(movie)
        return listed_by_genre
    
    """
    Restituisce una lista di film ricercati per il genere selezionato.

    Crea una lista vuota, itera nella lista di film ed estrapola i film che contengono il genere selezionato
    rispettando la condizione if di non case-sensitive, inserendoli nella lista creata.
    Nella condizione if viene usata la funzione any() che verifica se nell'iterazione è presente almeno un
    valore True. 
    """
    
    # Esercizio 12 

    def get_oldest_movie_title(self):
        oldest_movie = min(self.movies, key = lambda movie: movie["year"])
        return oldest_movie["title"]

    """
    Restituisce il titolo del film più vecchio.

    Utilizza la funzione key lambda per analizzare ogni dizionario nella lista dei film 
    e restituire il valore della chiave year. 
    Sfrutta la funzione min per cercare tra gli elementi della lista dei film quello con 
    il valore della chiave year più piccolo e restituirlo.
    """

    # Esercizio 13

    def get_average_release_year(self):
        years_sum = 0
        for movie in self.movies:
            years_sum += movie["year"]
        media = years_sum / len(self.movies)
        return media
    
    """
    Restituisce la media aritmetica degli anni di pubblicazione dei film nella collezione.

    Crea un contatore che si aggiorna ad ogni iterazione del ciclo for sulla lista dei film 
    catturando l'anno di rilascio, viene poi calcolata la media matematica tra la somma degli anni di rilascio 
    e il numero totale degli elementi nella lista di film.
    """
    
    # Esercizio 14

    def get_longest_title(self):
        longest_movie_title = max(self.movies, key = lambda movie: len(movie["title"]))
        return longest_movie_title["title"]


    """
    Restituisce il titolo più lungo tra i film della collezione.

    Utilizza la funzione key lambda per analizzare il dizionario e restituire il valore della chiave title. 
    Sfrutta la funzione min per cercare tra gli elementi della lista dei film quello con 
    il valore della chiave title più lungo e restituirlo.
    """

    # Esercizio 15 

    def get_titles_between_years(self, start_year = int, end_year = int):
        titles_between_years = []
        for movie in self.movies:
            if start_year <= movie["year"] <= end_year:
                titles_between_years.append(movie["title"])
        return titles_between_years
    
    """
    Restituisce una lista dei titoli dei film che sono compresi tra i due parametri start_year e end_year.

    Crea una lista, itera nella lista di film e se la condizione if per cui il valore year è compreso tra i parametri impostati
    (estremi compresi) è rispettata, aggiunge il titolo del film corrispondente alla lista creata.
    """

    # Esercizio 16 - Il metodo get_most_common_year()

    def get_most_common_year(self):
        pass


 

json_path = r"C:\Users\glbac\OneDrive\Desktop\Programming Principles - Traccia (1)\movies.json"

collection = MovieLibrary(r"C:\Users\glbac\OneDrive\Desktop\Programming Principles - Traccia (1)\movies.json")



# test_zone

"""

# Esercizio 1 - Metodo get_movies

print(f"All the movies in the library are : {collection.get_movies()}")

# Esercizio 2 - Metodo add_movie

added_movie = collection.add_movie("The Karate Kid", "John G. Avildsen", 1984, ["Action", "Drama", "Sport"])
print(f"The movie {added_movie["title"]} has been added in your collection!")

# Esercizio 3 - Metodo remove_movie

removed_movie = collection.remove_movie("The Karate Kid")
print(f"{removed_movie["title"]} has been deleted from the collection!")


# Esercizio 4 - Metodo update_movie

updated_movie = collection.update_movie("fight club", None, None, ["Drama", "Thriller"])
print(f"The movie {updated_movie["title"]} has been updated!")

# Esercizio 5 - Metodo get_movie_titles

print(collection.get_movie_titles())

# Esercizio 6 - Metodo count_movies

stored_movies = collection.count_movies()
print(f"You have {stored_movies} movies stored in your collection!")

# Esercizio 7 - Metodo get_movies_by_title

movie_by_title = collection.get_movie_by_title("the dark knight")
print(f"You have {movie_by_title["title"]} in your collection with that title!")

# Esercizio 8 - Metodo get_movies_by_title_substring

movie_by_substring = collection.get_movie_by_title_substring("the")
print(f"The movies matching with this substring in the title are: {movie_by_substring}")
print(len(movie_by_substring))

# Esercizio 9 - Metodo get_movies_by_year

movies_by_year = collection.get_movies_by_year(1994)
print(f"The movies from the selected year are: {movies_by_year}")

# Esercizio 10 - Metodo count_movies_by_director()

movies_by_director = collection.count_movies_by_director("Christopher Nolan")
print(f"The movies by the selected director in your collection are {movies_by_director}")

# Esercizio 11 - Metodo get_movies_by_genre()

movies_by_genre = collection.get_movies_by_genre("action")
print(f"The movies by the selected genre in your collection are: {movies_by_genre}")

# Esercizio 12 - Metodo get_oldest_movie_title()

oldest_movie_title = collection.get_oldest_movie_title()
print(f"The oldest movie in your collection is : {oldest_movie_title}")

# Esercizio 13 - Metodo get_average_release_year()

average_release_year = collection.get_average_release_year()
print(average_release_year)

# Esercizio 14 - get_longest_title()

longest_title = collection.get_longest_title()
print(f"The longest title is : {longest_title}") 

# Esercizio 15 - Metodo get_titles_between_years()

movies_between_years = collection.get_titles_between_years(1994, 1998)
print(f"The movies released between the selected years are: {movies_between_years}")

# Esercizio 16 - Metodo get_most_common_year()



# Esercizio 18 - Eccezione sollevata dal metodo remove_movie modificato

removed_movie = collection.remove_movie("Le Iene")

# Esercizio 18 - Eccezione sollevata dal metodo update_movie modificato

updated_movie = collection.update_movie("Spider-Man", None, None, ["Action", "Sci-Fi"])

"""
