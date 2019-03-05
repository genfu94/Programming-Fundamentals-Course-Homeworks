'''Scrivere una funzione search_page(url, enc, searches) che legge la pagina
all'indirizzo URL url, decodificandola tramite la codifica enc, e ritorna un
dizionario che ad ogni stringa nella lista searches associa il numero di
occorrenze della stringa nella pagina.

Per gli esempi vedere il file grade01.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''

import urllib2 as ul



def search_page(url, enc, searches):
    '''Implementare qui la funzione'''
    
    stringOccurrences = {}
    
    f = ul.urlopen ( url )
    
    webPage = f.read ()
    
    webPage.decode ( enc )
    
    for s in searches :
    	
    	stringOccurrences [ s ] = webPage.count ( s )
    
    return stringOccurrences

print search_page('https://sites.google.com/a/di.uniroma1.it/fondamenti/notes03.html', 'utf8', ['python', 'programmazione', 'shell', 'variabile', 'funzione', 'def'])
