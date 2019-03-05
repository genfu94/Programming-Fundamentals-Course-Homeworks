'''Implementare il seguente gioco simile al Tetris visto a lezione, che
chiameremo Pile. Come nel Tetris ci sono dei pezzi che cadono ma in questo
caso hanno solamente la forma di un singolo blocchetto (o quadratino). Possono
avere diversi colori scelti tra i seguenti 6:
'r' -> (255,0,0);   'g' -> (0,255,0);   'b' -> (0,0,255);
'o' -> (255,165,0); 'v' -> (255,0,255); 'y' -> (255,255,0)
Ogni colore e' quindi identificato da uno specifico carattere. I 6 colori
sono accoppiati in 3 coppie dalla relazione di anticolore:
'r' <-> 'g',  'b' <-> 'o',  'v' <-> 'y'
Quindi, ad esempio, il rosso 'r' e' l'anticolore del verde 'g' e viceversa.
Quando il pezzo corrente cade e' arriva (sbattendo contro o il fondo o un altro
pezzo gia' caduto), puo' formare una pila critica. Un pila critica e' una
pila di pezzi che ha in cima k pezzi di un colore x e dopo di questi esattamente
k pezzi dell'anticolore di x, ma non di piu'. Se il pezzo corrente una volta
caduto crea una pila critica tutti i pezzi che formano quella pila sono
eliminati e il punteggio e' incrementato del quadrato di 2*k (cioe' il quadrato
del numero di pezzi eliminati). Ad esempio, ecco una possibile sequenza di
situazioni di gioco consecutive, in cui i pezzi sono rappresentati dai caratteri
che ne identificano il colore:

                                                                        o
                                                             o          o
               g                                 b           b          b
____r____  ____r____  _________  ____b____   ____b____   ____b____  ____b____
          pila critica                                            pila critica


                                     r
                          g          g
_________  ____v____  ____v____  ____v____   ____v____
                                pila critica

Il movimento dei pezzi e' come nel Tetris relativo ad una matrice di celle
quadrate e il lato di ogni cella deve essere di 16 pixels. Le dimensiioni devono
essere 9 colonne e 16 righe. I tasti accettati devono essere i seguenti 3:
'a'  -->  spostamento a sinistra di una cella
'd'  -->  spostamento a destra di una cella
' '  -->  caduta rapida del pezzo

La gestione delle collisioni, con le pareti della matrice di gioco o coi pezzi
gia' caduti, deve seguire lo stesso schema del Tetris visto a lezione. La
caduta del pezzo corrente (cioe' lo spostamento di una cella verso il basso)
deve avvenire ogni 10 frames. La posizione iniziale di un nuovo pezzo e', come
nel Tetris, al centro della riga piu' alta. Il colore di ogni nuovo pezzo deve
essere ottenuto dal metodo next_val(piece_count) dell'oggetto info del painter
che viene passato alla funzione paint() che aggiorna ogni frame. L'argomento
piece_count deve essere il conteggio dei pezzi gia' caduti. Quindi il primo
pezzo avra' colore painter.info.next_val(0), il secondo painter.info.next_val(1)
e cosi' via. Il metodo ritorna il carattere che identifica il colore.

Il punteggio deve essere aggiornato ogni volta che una pila critica e' eliminata.
All'inizio e' automaticamente inizializzato a 0. Per aggiornarlo basta impostare
il valore dell'attributo score di info.

Come nel Tetris, se il nuovo pezzo appena creato e' gia' in collisione nella
posizione iniziale, il gioco deve terminare e deve iniziare un nuovo gioco con
la matrice vuota e lo score a 0 (e riportando a 0 il conteggio dei pezzi).

Eseguendo direttamente program03.py si puo' provare il gioco a piacimento.
Mentre l'esecuzione di grade03.py mette alla prova l'implementazione
controllando che l'evoluzione del gioco e le risposte agli eventi rispettino
le richieste.

Si consiglia di partire dal codice del Tetris visto a lezione e di modificarlo
opportunamente.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework o non sono esplicitamente autorizzati.
'''

# NON MODIFICARE I SEGUENTI IMPORT
from PySide.QtGui import *
from PySide.QtCore import *
from testapp import run         # NON IMPORTARE NIENT'ALTRO DA testapp

#Define the colors of blocks

colors = { 
			'r' : QColor ( 255 , 0 , 0 ) ,

			'g' : QColor ( 0 , 255 , 0 ) ,
			
			'b' : QColor ( 0 , 0 , 255 ) ,
			
			'o' : QColor ( 255 , 165 , 0 ) ,
			
			'v' : QColor ( 255 , 0 , 255 ) ,
			
			'y' : QColor ( 255 , 255 , 0 )
			
		 }

#Define color rules

colorRules = {

				'r' : 'g' ,
				
				'g' : 'r' ,
				
				'b' : 'o' ,
				
				'o' : 'b' ,
				
				'v' : 'y' ,
				
				'y' : 'v'
				
			}

score = 0

#Define objects size

boardWidth = 9

boardHeight = 16

pieceSize = 16

#Define and initialize the board

board = [ ]

for r in range ( boardHeight ) :
	
	board . append ( [''] * boardWidth )

#Define Input Keys

moveLeftKey = 'a'

moveRightKey = 'd'

instantFallKey = ' '

#Define piece stats

pieceX = 0

pieceY = 0

pieceCount = 0

pieceColor = ''

pieceFallingTime = 10

frameCount = 0

isRunning = False

#Empty board

def EmptyBoard ( ) :
	
	global board , boardHeight , boardWidth
	
	for r in range ( boardHeight ) :
		
		for c in range ( boardWidth ) :
			
			board [ r ] [ c ] = ''

#Convert a split Pile

def ConvertSplitPile ( splitPile ) :
	
	pile = [ ]
	
	for element in splitPile :
		
		for i in range ( element [ 1 ] ) :
			
			pile . append ( element [ 0 ] )
	
	pileLenght = len ( pile )
	
	for j in range ( boardHeight - pileLenght ) :
		
		pile . insert ( 0 , '' )
	
	return pile

#Get Pile

def GetPile ( c ) :
	
	global board , boardWidth , boardHeight
	
	pile = [ ]
	
	for r in range ( boardHeight ) :
			
		if board [ r ] [ c ] != '' :
			
			pile . append ( board [ r ] [ c ] )
	
	return pile

#Set Pile

def SetPile ( i , pile ) :
	
	global board , boardWidth , boardHeight
	
	for r in range ( boardHeight ) :
		
		board [ r ] [ i ] = pile [ r ]

#Split pile

def SplitPile ( pile ) :
	
	splitPile = [ ]
	
	i = 0
	
	while i < len ( pile ) :
		
		c = 1
		
		j = i + 1
		
		while j < len ( pile ) and pile [ j ] == pile [ i ] :
			
			c += 1
			
			j += 1
		
		splitPile += [ ( pile [ i ] , c ) ]
		
		i = j
	
	return splitPile

#Check critic pile

def CheckCriticPile ( splitPile ) :
	
	score = 0
	
	sp = [ ]
	
	for i in range ( 0 , len ( splitPile ) - 1 ) :
		
		if splitPile [ i ] [ 0 ] == colorRules [ splitPile [ i + 1 ] [ 0 ] ] :
			
			if splitPile [ i ] [ 1 ] == splitPile [ i + 1 ] [ 1 ] :
				
				score = ( splitPile [ i ] [ 1 ] * 2 ) ** 2
	
	if score != 0 :
		
		sp = splitPile [ 2 : ]
	
	return ( score , sp )

#Check if the piece hit something

def hit ( ) :

	global pieceX , pieceY , boardWidth , boardHeight , board
	
	if pieceX < 0 or pieceX >= boardWidth :
		
		return True
        
	if pieceY < 0 or pieceY >= boardHeight :
		
		return True
		
	if board [ pieceY ] [ pieceX ] :
		
		return True
	
	return False

#Make a new piece fall

def GetNewPiece ( color ) :
	
	global pieceX , pieceY , pieceCount , pieceColor , colors , frameCount
	
	print color
	
	pieceX = int ( boardWidth / 2 )
	
	pieceY = 0
	
	pieceCount += 1
	
	pieceColor = color
	
	frameCount = 0

#Handle user input

def HandleInput ( key ) :
	
	global moveLeftKey , moveRightKey , pieceX , pieceY
	
	if key == moveLeftKey :
		
		pieceX += -1
		
		if hit ( ) :
			
			pieceX += 1
	
	elif key == moveRightKey :
		
		pieceX += 1
		
		if hit ( ) :
			
			pieceX += -1
	
	elif key == instantFallKey :
		
		while not hit ( ) : pieceY += 1
		
		pieceY -= 1

#Render routine

def Draw ( painter ) :
	
	global boardWidth , boardHeight , pieceColor , pieceX , pieceY , pieceSize , colors
	
	#Clear the screen
	
	painter . setBrush ( QColor ( 128 , 128 , 128 ) )
	
	painter . drawRect ( 0 , 0 , boardWidth * pieceSize , boardHeight * pieceSize )
	
	#Draw the board
	
	for r in range ( boardHeight ) :
		
		for c in range ( boardWidth ) :
			
			if board [ r ] [ c ] != '' :
				
				painter . setBrush ( colors [ board [ r ] [ c ] ] )
			
				painter . drawRect ( c * pieceSize , r * pieceSize , pieceSize , pieceSize )
	
	#Draw the current piece
	
	painter . setBrush ( colors [ pieceColor ] )
	
	painter . drawRect ( pieceX * pieceSize , pieceY * pieceSize , pieceSize , pieceSize )
				
#Resolve board

def ResolveBoard ( ) :
	
	global board , boardHeight , boardWidth , score
	
	app = 0
	
	for c in range ( boardWidth ) :
		
		app = CheckCriticPile ( SplitPile ( GetPile ( c ) ) )
		
		if app [ 0 ] > 0 :
			
			score += app [ 0 ]
			
			SetPile ( c , ConvertSplitPile ( app [ 1 ] ) )					

#Game Loop

def Update ( painter ) :
	
	global frameCount , pieceFallingTime , pieceX , pieceY , pieceCount , board , score
	
	frameCount += 1
	
	if frameCount < pieceFallingTime :
		
		return
	
	pieceY += 1
	
	if hit ( ) :
		
		pieceY -= 1
		
		board [ pieceY ] [ pieceX ] = pieceColor
		
		ResolveBoard ( )
		
		GetNewPiece ( painter . info . next_val ( pieceCount ) )
		
		if hit ( ) :
		      
		      score = 0
		      
		      EmptyBoard ( )
		      
		      GetNewPiece ( painter . info . next_val ( pieceCount ) )
	
	painter . info . score = score
	
	frameCount = 0

#This function is run every frame

def paint ( painter ) :
	
	global isRunning
	
	'''Implementare qui la funzione che aggiorna il gioco ad ogni frame'''
	
	if isRunning == False :
	
		EmptyBoard ( )
	
		GetNewPiece ( painter . info . next_val ( pieceCount ) )
		
		isRunning = True
	
	if painter . info . key :
		
		HandleInput ( painter . info . key )
		
		painter . info . key = ''
	
	Update ( painter )
	
	Draw ( painter )
		
# Crea la GUI (la finestra) e chiama la funzione paint() ad ogni frame
run(paint, globals(), 144, 256, title='Pile', score=True)    # NON MODIFICARE
