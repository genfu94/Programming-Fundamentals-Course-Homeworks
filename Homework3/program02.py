'''Diciamo che un dizionario rappresenta una rubrica se associa ad ogni nome
un set di numeri di telefono (cellulari, fax, ecc.) relativi a quel nome. I nomi
sono stringhe che rispettano un formato standard in cui tutti i caratteri
alfabetici sono in maiuscolo, non ci due spazi consecutivi e non ci sono spazi
all'inizio e alla fine della stringa. I numeri di telefono sono stringhe in un
formato standard che contiene solamente le cifre '0',...,'9'.
Inoltre, diciamo che un file di testo rappresenta una rubrica se contiene solamente
caratteri ASCII e ogni linea del file contiene un nome (cioe' una
qualsiasi sequenza di caratteri escluso ':') seguito dal carattere ':' e poi
uno o piu' numeri di telefono separati da virgole (un numero di telefono puo'
contenere anche caratteri diversi dalle cifre ma questi devono essere
ignorati).
Scrivere una funzione phonebook(phbook, fname) che prende in input un
dizionario phbook che rappresenta una rubrica e il nome di un file fname che
rappresenta una rubrica e aggiorna la rubrica phbook tramite la rubrica
rappresentata dal file. Questo significa che per ogni nome contenuto nel file
se, una volta messo in formato standard, e' gia' presente in phbook, allora i
numeri di telefono (in formato standard) relativi a quel nome nel file devono
essere uniti al set in phbook, se invece non e' presente, il nome (in formato
standard) e i relativi numeri di telefono devono essere aggiunti a phbook.

Per gli esempi vedere il file grade02.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''

#----------------------------------------------------------------------------

def GetEntryFields ( entry ) :
	
	entry = entry . replace ( ',', ':' )
	
	entry = entry . replace ( '\n', '' )
	
	return entry . split ( ':' )

#----------------------------------------------------------------------------

def StandardizeName ( name ) :
	
	sn = ' ' . join ( name . split ( ) )
	
	sn = sn . upper ()
	
	return sn

#----------------------------------------------------------------------------

def StandardizeNumber ( number ) :
	
	sn = ''
	
	for c in number :
		
		if c.isdigit() :
			
			sn += c
	
	return sn
	
#----------------------------------------------------------------------------
         
def phonebook(phbook, fname) :
	
	f = open ( fname, "r" )
	
	entryFields = []
	
	name = ''
	    
	for entry in f :
	
		numberSet = set()
		
		entryFields = GetEntryFields ( entry )
		
		name = StandardizeName ( entryFields [ 0 ] )
		
		for number in entryFields [ 1 : ] :
			
			numberSet . add ( StandardizeNumber ( number ) )
		
		if name in phbook :
			
			numberSet = numberSet . union ( phbook [ name ] )
		
		phbook [ name ] = numberSet
		
	print phbook

#----------------------------------------------------------------------------
