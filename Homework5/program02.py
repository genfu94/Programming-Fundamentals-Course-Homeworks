'''Questo eserczio chiede di implementare una funzione che permette di disegnare
su una finestra (di Qt) in modo simile a come fatto nella lezione sulla grafica
interattiva. Si tratta quindi di implementare una funzione paint(painter) che
sara' chiamata ad ogni frame per aggiornare la grafica usando l'oggetto painter
che ha gli stessi metodi visti nella lezione suddetta. La funzione deve disegnare
solamente se il mouse e' premuto (painter.info.mouse_pressed e' True) seguendo il
movimento del mouse. Cio' che disegna dipendera' dallo stato in cui si trova.
Nello stato iniziale disegna un rettangolo con contorno bianco (255,255,255),
interno red (255,0,0) e che ha i due spigoli opposti rispetto ad una diagonale
nel punto precedente del mouse (painter.info.mouse_px, painter.info.mouse_py) e
nel punto corrente del mouse (painter.info.mouse_x, painter.info.mouse_y). Lo
stato e' modificato dalla pressione di alcuni tasti:
'r'  -->  colore interno red (255,0,0).
'g'  -->  colore interno green (0,255,0).
'b'  -->  colore interno blue (0,0,255).
'e'  -->  cambia la forma disegnata da rettangolo ad ellisse e
          viceversa (il rettangolo e' sempre lo stesso).
't'  -->  cambia la trasparenza dell'interno da opaco a trasparente e
          viceversa.
'd'  -->  cambia il rettangolo da quello di default ad uno di dimensione doppia
          e viceversa. Il rettangolo doppio ha larghezza e altezza doppie
          rispetto a quelle di default e uno spigolo rimane sul punto corrente
          del mouse.
          
Per gli esempi vedere le immagini img02_XX_check.png che mostrano i disegni
che devono risultare eseguendo grade02.py.

Eseguendo direttamente program02.py si puo' provare a disegnare a piacimento.
Mentre l'esecuzione di grade02.py mette alla prova l'implementazione
controllando che disegni in base agli eventi e rispettando le richieste.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework o non sono esplicitamente autorizzati.
'''

# NON MODIFICARE I SEGUENTI IMPORT
from PySide.QtGui import *
from PySide.QtCore import *
from testapp import run    # NON IMPORTARE NIENT'ALTRO DA testapp

colorMode = 'r'

drawingMode = ''

def paint(painter):
	'''Implementare qui la funzione che aggiorna la grafica ad ogni frame'''
	
	global colorMode
	
	global drawingMode
	
	penColor = QColor ( 255 , 255 , 255 )
	
	brushColor = 0
	
	alpha = 255
	
	painter . setPen ( penColor )
	
	#Set the color mode
	
	if painter . info . key in [ 'r' , 'g' , 'b' ] :
		
		colorMode = painter . info .key
		
		painter . info . key = ''
	
	#set the drawing mode
	
	elif painter . info .key in [ 'e' , 't' , 'd' ] :
		
		if drawingMode . find ( painter . info . key ) != -1 : #if it is already active, deactivate it
			
			drawingMode = drawingMode . replace ( painter . info . key , '' )
		
		else :
			
			drawingMode += painter . info . key #activate the mode
		
		painter . info . key = ''
	
	if drawingMode . find ( 't' ) != -1 :
		
		alpha = 0
	
	else :
		
		alpha = 255
	
	if colorMode == 'r' :
		
		painter . setBrush ( QColor ( 255 , 0 , 0 , alpha ) )
	
	elif colorMode == 'g' :

		painter . setBrush ( QColor ( 0 , 255 , 0 , alpha ) )
	
	elif colorMode == 'b' :

		painter . setBrush ( QColor ( 0 , 0 , 255 , alpha ) )
		
	if painter . info . mouse_pressed :
		
		if drawingMode . find ( 'd' ) == -1 :
		
			if painter . info . mouse_py <= painter . info . mouse_y :
		
				y = painter . info . mouse_py
		
			else :
			
				y = painter . info . mouse_y
		
			if painter . info .mouse_px <= painter . info . mouse_x :
			
				x = painter . info . mouse_px
		
			else :
			
				x = painter . info . mouse_x
		
			w = abs ( painter . info . mouse_px - painter . info . mouse_x)
		
			h = abs ( painter . info . mouse_py - painter . info . mouse_y)
		
		else :
			
			w = abs ( painter . info . mouse_px - painter . info . mouse_x) * 2
		
			h = abs ( painter . info . mouse_py - painter . info . mouse_y) * 2
			
			if painter . info . mouse_py <= painter . info . mouse_y :
		
				y = painter . info . mouse_py - h / 2
		
			else :
			
				y = painter . info . mouse_y - h / 2
		
			if painter . info . mouse_px <= painter . info . mouse_x :
			
				x = painter . info . mouse_px - w / 2
		
			else :
			
				x = painter . info . mouse_x - w / 2
		
		if drawingMode . find ( 'e' ) != -1 :
			
			painter . drawEllipse ( x , y , w , h )
		
		else :
		
			painter . drawRect ( x , y , w , h )
	
# Crea la GUI (la finestra) e chiama la funzione paint() ad ogni frame
run(paint, globals())       # NON MODIFICARE
