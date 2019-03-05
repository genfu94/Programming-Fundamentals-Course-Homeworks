'''Scrivere una funzione actorDirGraph(filmfile) che prende in input un file
filmfile in formato JSON contenente dati di films (vedi dopo) e ritorna una
coppia (gf, gd) di due grafi di tipo Graph (lo stesso tipo visto a lezione)
descritti dopo. Il file contiene un dizionario le cui chiavi sono titoli di
film e ad ogni titolo e' associato un dizionario con le seguenti chiavi-valori:
'ACTORS': lista dei nomi degli attori che hanno recitato nel film
'DIRECTORS': lista dei registi del film
Entrambi i grafi devono avere come nodi tutti gli attori che hanno recitato
in almeno uno dei film nel file. Due nodi (attori) del grafo gf (chiamato grafo
ACTORS-FILM) sono adiacenti se hanno recitato nello stesso film. Due nodi del
grafo gd (chiamato grafo ACTORS-DIRECTOR) sono adiacenti se hanno recitato con
lo stesso regista (quindi, non necessariamente nello stesso film). Ad esempio,
Audrey Hepburn e Frank Sinatra, nel file 'file01_01_in.json', non hanno mai
recitato nello stesso film e quindi non sono adiacenti nel grafo ACTORS-FILM ma
hanno entrambi recitato in film con il regista Stanley Donen e quindi sono
adiacenti nel grafo ACTORS-DIRECTOR. Chiaramente, tutti gli archi del grafo
ACTORS-FILM sono anche archi nel grafo ACTORS-DIRECTOR.

A titolo d'esempio diamo i seguenti dati:
'file01_01_in.json'  numero nodi: 2896,
                     numero archi: ACTORS-FILM 20839, ACTORS-DIRECTOR 26947
'file01_02_in.json'  numero nodi: 5939,
                     numero archi: ACTORS-FILM 46024, ACTORS-DIRECTOR 82807
'file01_03_in.json'  numero nodi: 7854,
                     numero archi: ACTORS-FILM 64111, ACTORS-DIRECTOR 138843

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework o non sono esplicitamente autorizzati.
'''

class Graph(object):
    def __init__(self):
        self._nodes = {}

    def addNode(self, name, info=None):
        '''Aggiunge un nodo name, se non esiste'''
        if name not in self._nodes:
            self._nodes[name] = (set(), info)

    def addEdge(self, name1, name2):
        '''Aggiunge un arco che collega i nodi name1 e name2'''
        if name1 in self._nodes and name2 in self._nodes:
            self._nodes[name1][0].add(name2)
            self._nodes[name2][0].add(name1)
            return True
        return False

    def adjacents(self, name):
        '''Ritorna una lista dei nomi dei nodi adiacenti al nodo name,
        se il nodo non esiste, ritorna None'''
        if name in self._nodes:
            return list(self._nodes[name][0])
        return None

    def nodes(self):
        '''Ritorna una lista dei nomi dei nodi del grafo'''
        return self._nodes.keys()

    def nodeInfo(self, name):
        '''Ritorna l'info del nodo name'''
        return self._nodes[name][1] if name in self._nodes else None

import json

def actorDirGraph(filmfile):

	gf = Graph ( )
	
	gd = Graph ( )
	
	directorActors = { }
	
	with open ( filmfile ) as f :
    	
		a = json . load ( f )
		
		#Create the film actor graph
			
		for film in a :
			
			for actor in a [ film ] [ 'ACTORS' ] :
				
				for director in a [ film ] [ 'DIRECTORS' ] :
					
					if director not in directorActors :
						
						directorActors [ director ] = [ actor ]
					
					else :
						
						if actor not in directorActors [ director ] :
						
							directorActors [ director ] += [ actor ]
					
				gf . addNode ( actor )
				
				gd . addNode ( actor )
			
			actorsNumber = len ( a [ film ] [ 'ACTORS' ] )
			
			for i in range ( actorsNumber - 1 ) :
				
				actor1 = a [ film ] [ 'ACTORS' ] [ i ]
			
				for j in range ( i , actorsNumber ) :
					
					actor2 = a [ film ] [ 'ACTORS' ] [ j ]
					
					if i != j :
				
						gf . addEdge ( actor1 , actor2 )
		
		#Create the actor director graph
		
		for director in directorActors :
			
			actorsNumber = len ( directorActors [ director ] )
			
			for i in range ( actorsNumber - 1 ) :
				
				actor1 = directorActors [ director ] [ i ]
			
				for j in range ( i , actorsNumber ) :
					
					actor2 = directorActors [ director ] [ j ]
					
					if i != j :
						
						gd . addEdge ( actor1 , actor2 )

		return ( gf , gd )

'''gf , gd = actorDirGraph ( 'file01_02_in.json' )

edges = 0

for u in gd . nodes ( ) :
	
	edges += len ( gd . adjacents ( u ) )

edges /= 2

print edges'''
