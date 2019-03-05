'''In questo esercizio, per parola intendiamo una qualsiasi sequenza di caratteri
alfabetici (a-z, A-Z) di lunghezza massimale e due parole sono uguali se sono la
stessa sequenza di lettere, indipendentemente dalle maiuscole/minuscole (cioe'
"the", "The", "THE" sono la stessa parola). La forma standard di una parola e'
quella in cui tutte le sue lettere sono in minuscolo. Dato un testo T, il grafo
delle parole di T e' il grafo i cui nodi sono le parole di T in forma
standard e due parole sono adiacenti se nel testo T appaiono l'una di seguito
all'altra e separate solamente da caratteri whitespaces (cioe' caratteri il cui
codice ASCII e' <= 32).
Scrivere una funzione wdist(fname, word) che prende in input il nome fname di
un file di testo e una parola word e ritorna un dizionario delle distanze delle
parole del file dalla parola word nel grafo delle parole del testo del file.
Se una parola del testo del file non e' connessa a word (cioe' non e' nella
componente connessa di word) non deve comparire nel dizionario delle distanze.
Esempio,

wdist('file02_01_in.txt', 'and')  -->

{'and': 0, 'golden': 3, 'all': 4, 'existence': 7, 'deal': 4, 'ran': 2, 'is': 4,
'in': 6, 'back': 3, 'as': 4, 'sudden': 2, 'at': 2, 'escape': 6, 'table': 3,
'still': 5, 'frightened': 3, 'find': 3, 'worse': 3, 'again': 5, 'little': 2,
'for': 2, 'herself': 4, 'things': 1, 'to': 2, 'change': 3, 'before': 5, 'was': 3,
'speed': 4, 'poor': 2, 'shut': 4, 'good': 5, 'door': 3, 'garden': 2, 'that': 4,
'very': 4, 'never': 2, 'but': 5, 'it': 3, 'glass': 2, 'key': 4, 'child': 3,
'now': 1, 'with': 3, 'than': 4, 'glad': 3, 'a': 4, 'on': 2, 'i': 1, 'ever': 5,
'thought': 2, 'this': 5, 'so': 4, 'she': 1, 'small': 5, 'the': 1, 'narrow': 5,
'declare': 2, 'lying': 3, 'are': 2}

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

def distance(graph, name):
    '''Ritorna un dizionario che ad ogni nodo visitato a partire
    dal nodo name associa la distanza da tale nodo'''
    visited = set([name])
    active = set([name]) 
    dist = {name:0}           # Dizionario delle distanze
    while len(active) > 0:
        newactive = set() 
        while len(active) > 0: 
            u = active.pop()
            for v in graph.adjacents(u):
                if v not in visited: 
                    visited.add(v) 
                    newactive.add(v)
                    # La distanza del nodo appena visitato
                    dist[v] = dist[u] + 1
        active = newactive      
    return dist

def NoAlpha ( s ) :
	
	noAlpha = ''
	
	for c in s :
		
		if not ( c in noAlpha or c . isalpha ( ) ) :
			
			if ord ( c ) > 32 :
				
				noAlpha += c
	
	return noAlpha

def SplitWords ( s ) :
	
	noAlpha = NoAlpha ( s )
	
	for c in noAlpha :
		
		s = s . replace ( c , "| " )
	
	return s . split ( )

def GetNoAlpha ( s ) :
	
	na = NoAlpha ( s )
	
	for c in na :
		
		s = s . replace ( c , "" )
	
	return s

def wdist(fname, word):

	graph = Graph ( )
	
	with open ( fname , 'U' ) as f :
		
		text = f . read ( )
		
		splitWords = SplitWords ( text )
		
		graph . addNode ( GetNoAlpha ( splitWords [ 0 ] . lower ( ) ) )
		
		for i in range ( 1 , len ( splitWords ) ) :
			
			word1 = GetNoAlpha ( splitWords [ i - 1 ] . lower ( ) )
			
			word2 = GetNoAlpha ( splitWords [ i ] . lower ( ) )
 			
 			graph . addNode ( word2 )
 			
 			if splitWords [ i - 1 ] [ len ( splitWords [ i - 1 ] ) - 1 ] . isalpha ( ) :
				
				if word1 != '' and word2 != '' :
				
					graph . addEdge ( word1 , word2 )
	
	return distance ( graph , word )
