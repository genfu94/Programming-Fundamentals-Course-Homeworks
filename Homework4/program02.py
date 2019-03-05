'''Partendo da una parola e' possibile, a volte, formare altre parole inserendo
una lettera all'inizio, alla fine o in mezzo alla parola. Ad esempio, partendo
dalla parola 'seta' possiamo inserire una 't' in mezzo formando 'setta', inserendo
poi una 'p' otteniamo 'spetta' e aggiungendo una 'i' alla fine formiamo 'aspettai'.
Partendo quindi da una parola possiamo considerare tutte le parole che si ottengono
inserendo una lettera e poi possiamo ripetere la stessa operazione a partire da
quest'ultime e cosi' via ottenendo un albero di parole. Ad esempio, ecco l'albero
che si ottiene partendo dalla parola 'posta':

posta
    sposta
        esposta
        sposata
            spossata
            spostata
        spostai
            spostati
                spostarti
                spostasti
            spostavi
                spostarvi
    posata
        sposata
            spossata
            spostata
    posita

Definire una classe WNode che rappresenta un nodo di un albero di parole. La
classe deve implementare i metodi di seguito specificati. Nel seguito per albero
intenderemo l'albero che ha per radice l'oggetto su cui e' invocato il metodo.

- Costruttore, con argomento w, crea un nodo relativo alla parola w, inizialmente
  senza figli.
  
- count() ritorna il numero di nodi dell'albero.

- count_d() ritorna il numero di parole distinte presenti nell'albero.

- height() ritorna l'altezza dell'albero. L'altezza e' la lunghezza del piu'
  lungo cammino dalla radice a una foglia dell'albero. Ad esempio, l'albero di
  'posta' ha altezza 5.

- leaves() ritorna un insieme (tipo set) delle parole che sono nelle foglie
  dell'albero.

- path(w) ritorna un insieme (tipo set) che per ogni nodo u dell'albero che ha
  la parola w contiene una tupla della sequenza delle parole dei nodi dalla
  radice dell'albero fino al nodo u. Ad esempio, se path('spostata') e' invocato
  sul nodo 'posta' ritorna
  set([('posta', 'posata', 'sposata', 'spostata'),
       ('posta', 'sposta', 'sposata', 'spostata')])

Scrivere infine la funzione gen_wtree(wfile, word) che prende in input il
percorso di un file wfile e una parola word e genera l'albero con radice la
parola word e ritorna il nodo radice (di tipo WNode). Il file wfile contiene
le parole lecite. E' garantito che il file contenga solamente caratteri ascii e
che ogni linea contenga solamente una parola con soli caratteri alfabetici
minuscoli. L'albero genearato contiene solamente parole presenti nel file wfile.

Se necessario, si possono aggiungere altri metodi alla classe e si possono
definire altre funzioni.

Per gli esempi vedere il file grade02.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework.
'''


'''Implementare qui la classe WNode'''

def ListToSet ( array , x ) :
	
	s = set ( )
	
	p = 0
	
	for i in range ( len ( array ) ):
		
		if array [ i ] == x :
			
			s . add ( tuple ( array [ p : i + 1 ] ) )
			
			p = i + 1
	
	return s

def MergeStrings ( s1 , s2 , index ) :
	
	return s1 [ 0 : index ] + s2 + s1 [ index : ]

def BinarySearch ( array , x ) :
		
	p = 0
	
	u = len ( array ) - 1
	
	m = 0
	
	while p <= u :
		
		m = ( p + u ) / 2
		
		if array [ m ] == x :
			
			return m
		
		if array [ m ] < x :
			
			p = m + 1
		
		else :
			
			u = m - 1
	
	return -1

class WNode ( object ) :
	
	def __init__ ( self , w ) :
		
		self . nodeWord = w
		
		self . content = [ ]
	
	def count ( self ) :
		
		c = 0
		
		for node in self . content :
			
			c += node . count ( )
		
		return c + 1
	
	def GetNodeSet ( self ) :
		
		s = set ( )
		
		s . add ( self . nodeWord )
		
		for node in self . content :
			
			s = s . union ( node . GetNodeSet ( ) )
		
		return s
	
	def count_d ( self ) :
		
		return len ( self . GetNodeSet ( ) )
	
	def height( self ) :
		
		h = 1
		
		for node in self . content:
			
			h = max( h , node.height() + 1 )
                
		return h
	
	def leaves ( self ) :
		
		l = set ( )
		
		if self . content == [ ] :
			
			l . add ( self . nodeWord )
		
		else :
			
			for node in self . content :
				
				l = l . union ( node . leaves ( ) )
		
		return l
	
	def GetPath ( self , word ) :
		
		l = [ ]
		
		m = [ ]
		
		if self . nodeWord == word :
			
			l += [ word ]
		
		else :
			
			for node in self . content :
				
				m = [ ]
				
				a = node . GetPath ( word )
				
				if a != [ ] :
					
					for i in a :
						
						if i == node . nodeWord :
							
							m . append ( self . nodeWord )
						
						m . append ( i )
				
				l += m
		
		return l
	
	def path ( self , word ) :
		
		return ListToSet ( self . GetPath ( word ) , word)

	def print_tree ( self, level = 0 ) :
		
		print '    ' * level + self . nodeWord
			
		for node in self . content:           # stampa ricorsivamente i
        	
			node . print_tree ( level + 1 )   # sottoalberi dei nodi figli

def GenerateTree ( lines , word ) :
	
	root = WNode ( word )
	
	words = [ ]
	
	for i in range ( len ( word ) + 1 ) :
		
		for j in range ( ord ( 'a' ) , ord ( 'z' ) + 1 ) :
			
			w = MergeStrings ( word , chr ( j ) , i )
			
			if w not in words :
				
				words += [ w ]
				
				if BinarySearch ( lines , w ) > 0 :
					
					root . content += [ GenerateTree ( lines , w ) ]
	
	return root

def gen_wtree ( wfile , word ) :

	f = open ( wfile , "r" )
	
	lines = f . read ( ) . splitlines ( )
	
	f . close ( )
	
	return GenerateTree ( lines , word )
