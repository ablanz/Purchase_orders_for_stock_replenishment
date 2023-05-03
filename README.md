# Purchase_orders_for_stock_replenishment
 
 Lo script fa uso di librerie builtin di python, l'unica libreria che necessita di essere installata è flask che può essere installata tramite il semplice comando "pip install flask"


L'architettura del software del codice Python fornito consiste in tre moduli: item.py, supplier.py e main.py, ognuno contenente classi e funzioni relative alla funzionalità dell'applicazione.

Il modulo item.py definisce due classi: Discount e Item. La classe Discount rappresenta uno sconto su un articolo e ha attributi come percentage, quantity, value e interval, che ne definiscono le caratteristiche. La classe Item rappresenta un articolo che può essere ordinato e ha attributi come name, price, stock e delivery_date, nonché una lista di oggetti Discount che possono essere applicati all'articolo.

Il modulo supplier.py definisce una classe Supplier che rappresenta un fornitore di articoli. La classe Supplier ha un attributo items, che è una lista di oggetti Item forniti dal fornitore. Definisce anche un metodo search_item_byname che consente di cercare articoli per nome.

Il modulo main.py definisce la logica principale dell'applicazione e contiene l'applicazione web Flask. Importa le classi Item, Discount, Supplier e Combo dagli altri moduli e definisce una funzione find_cheapest_supplier che prende il nome di un articolo, la quantità e una lista di oggetti Supplier e restituisce una lista ordinata di oggetti Combo che rappresentano i fornitori più economici per l'articolo e la quantità richiesti. Definisce anche un'applicazione Flask con due percorsi: / per la homepage e /search per gestire le richieste di ricerca.

Per quanto riguarda le scelte tecniche, il codice utilizza le seguenti librerie e strumenti:

modulo datetime: per lavorare con date e orari
funzione functools.cmp_to_key: per ordinare una lista di oggetti Combo utilizzando una funzione di confronto
framework Flask: per la costruzione dell'applicazione web e la gestione delle richieste e delle risposte HTTP
modulo utils: per fornire dati di test

Complessivamente, l'applicazione segue un design semplice e modulare, in cui ciascun modulo è responsabile di un dominio o di una funzionalità specifica. L'uso del framework Flask consente una facile comunicazione con il lato client e l'uso di richieste e risposte HTTP.

Sono inoltre presenti i moduli test_item e test_main_funcs che consentono di adottare un approccio Test Driven


Nel mio script ho utilizzato del codice presente nel modulo utils come input ma, visto che le linee guida lo menzionano, penso possa essere utile mostrare come eventualmente strutturerei un database mysql se lo script dovesse gestire più dati:
PNG: https://imgur.com/a/PHAJLXo
LucidCharts: https://lucid.app/lucidchart/08712d31-0f33-4157-9e89-56b8cd1e731/edit?viewport_loc=278%2C-72%2C1496%2C833%2CZkpUJ_WpuzUy&invitationId=inv_ad75c038-51d0-4384-975c-3f2ef7c37463