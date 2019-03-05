'''L'esercizio chiede di implementare una piccola applicazione con GUI tramite
Qt in modo analogo a quanto visto nella lezione sulle Interfacce Utente.
L'applicazione deve contenere le seguenti componenti:
- un campo (tipo QLineEdit) con nome 'FILE' (i nomi dei widget si impostano con
  il metodo setObjectName())
- una label (tipo QLabel) con nome 'LEN'
- un bottone (tipo QPushButton) con testo 'Stats'
- due label (tipo QLabel) con nomi 'LINES' e 'WORDS'
- un campo (tipo QLineEdit) con nome 'STR'
- un bottone (tipo QPushButton) con testo 'Find'
- infine una label (tipo QLabel) con nome 'COUNT'

Il comportamento dei componenti deve rispettare le seguenti specifiche.

Quando e' premuto Return sul campo'FILE', l'applicazione deve controllare
se il contenuto del campo e' il percorso di un file esistente, se lo e' deve
impostare il testo della label 'LEN' con la lunghezza del file, se non e' un
file esistente, deve impostare il testo della label 'LEN' alla stringa vuota.
In entrambi i casi deve anche impostare alla stringa vuota i testi di tutte le
altre tre label.

Quando il testo del campo 'FILE' cambia (evento rexrChanged), deve impostare
alla stringa vuota i testi di tutte e quattro le label.

Quando il bottone 'Stats' e' cliccato, se il contenuto del campo 'FILE' e'
stato testato corrispondere ad un file esistente, allora imposta la label
'LINES' al numero di linee del file e la label 'WORDS' al numero di parole
(come al solito, per parola si intende una qualsiasi sequenza di caratteri
alfabetici, maiuscoli o minuscoli, di lunghezza masssimale). Se il contenuto
di 'FILE' non e' stato testato corrispondere ad un file esistente, non fa nulla.

Quando il bottone 'Find' e' cliccato oppure il Return e' premuto sul campo 'STR',
se il contenuto del campo 'FILE' e' stato testato corrispondere ad un file
esistente, allora imposta la label 'COUNT' al numero di occorrenze della stringa
contenuta nel campo 'STR' nel file. Se il contenuto di 'FILE' non e' stato
testato corrispondere ad un file esistente, non fa nulla.

Infine, quando il testo del campo 'STR' cambia, deve impostare alla stringa vuota
il testo della label 'COUNT'.

E' assicurato che i file che saranno testati sono file di testo che contengono
solamente caratteri ASCII. Ai fini del grader la diposizione dei componenti e'
irrilevante.

Eseguendo direttamente program01.py si puo' provare l'applicazione a piacimento.
Mentre l'esecuzione di grade01.py mette alla prova l'applicazione controllando
che contenga tutti i componenti richiesti e che risponda agli eventi rispettando
le specifiche.

Si consiglia di partire dal codice di uno degli esempi della lezione sulle
Interfacce Utente e di modificarlo opportunamente (eccetto per la creazione
dell'oggetto QApplication e la chiamata al metodo _exec() che in questo caso
sono differenti come e' riportato nello schema qui sotto).

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework o non sono esplicitamente autorizzati.
'''
# NON MODIFICARE I SEGUENTI IMPORT
from PySide.QtGui import *
from testapp import startapp, runapp    # NON IMPORTARE NIENT'ALTRO DA testapp

import os

# Crea l'oggetto QApplication, NON chiamare QApplication
startapp()    # NON MODIFICARE

# Inizio implementazione dell'applicazione

'''Alcune variabili globali'''

text = ''

'''Funzioni utili'''

def noalpha(s):
        
	noa = ''
    
	for c in s :
	
		if not (c in noa or c.isalpha()):
		
			noa += c
	 
	return noa


def words(s):
	
	noa = noalpha(s)
	
	for c in noa:
		
		s = s.replace(c, ' ')
	
	return s.split()

def GetWordsNumber ( t ) :
	
	s = 0
	
	for line in t :
		
		s += len ( words ( line ) )
	
	return s

def CountStringOccurrences ( t , w ) :
	
	s = 0
	
	for line in t :
		
		for p in words ( line ) :
			
			s += p . count ( w )
	
	return s

'''Definisce il layout'''
window = QWidget ( )

windowLayout = QVBoxLayout ( )

filePath = QLineEdit ( )

fileLenght = QLabel ( '' )

getStatsButton = QPushButton ( "Stats" )

textLines = QLabel ( '' )

textWords = QLabel ( '' )

searchString = QLineEdit ( )

findStringButton = QPushButton ( "Find" )

stringOccurrences = QLabel ( '' )

filePath . setObjectName ( "FILE" )

fileLenght . setObjectName ( "LEN" )

textLines . setObjectName ( "LINES" )

textWords . setObjectName ( "WORDS" )

searchString . setObjectName ( "STR" )

stringOccurrences . setObjectName ( "COUNT" )

windowLayout . addWidget ( filePath )

windowLayout . addWidget ( fileLenght )

windowLayout . addWidget ( getStatsButton )

windowLayout . addWidget ( textLines )

windowLayout . addWidget ( textWords )

windowLayout . addWidget ( searchString )

windowLayout . addWidget ( findStringButton )

windowLayout . addWidget ( stringOccurrences )

'''Definisce le callbacks'''

def SearchFile ( ) :
	
	global text
	
	if os . path . exists ( filePath . text ( ) ) :
		
		f = open ( filePath . text ( ) , 'rU' )
		
		text = f . readlines ( )
		
		f . close ( )
		
		fileLenght . setText ( str ( os . path . getsize ( filePath . text ( ) ) ) )
		
		textLines . setText ( '' )
		
		textWords . setText ( '' )
		
		stringOccurrences . setText ( '' )
	
	else :
		
		fileLenght . setText ( '' )
		
		textLines . setText ( '' )
		
		textWords . setText ( '' )
		
		stringOccurrences . setText ( '' )
		
		text = ''

def OnFilePathChange ( ) :
	
	fileLenght . setText ( '' )
	
	textLines . setText ( '' )
	
	textWords . setText ( '' )
	
	stringOccurrences . setText ( '' )

def GetTextLinesAndWords ( ) :
	
	global text
	
	if text != '' :
		
		textLines . setText ( str ( len ( text ) ) )
		
		textWords . setText ( str ( GetWordsNumber ( text ) ) )

def GetOccurrences ( ) :
	
	global text
	
	if text != '' :
		
		stringOccurrences . setText ( str ( CountStringOccurrences ( text , searchString . text ( ) ) ) )

def ResetCount ( ) :
	
	stringOccurrences . setText ( '' )
		
'''Associa le callbacks'''

filePath . returnPressed . connect ( SearchFile )

filePath . textChanged . connect ( OnFilePathChange )

getStatsButton . clicked . connect ( GetTextLinesAndWords )

findStringButton . clicked . connect ( GetOccurrences )

searchString . returnPressed . connect ( GetOccurrences )

searchString . textChanged . connect ( ResetCount )

'''Crea la finestra e lancia l'applicazione'''

window . setLayout ( windowLayout )

window . resize ( 400 , 400 )

window . setWindowTitle ( "program01" )

window . show ( )

# Fine implementazione dell'applicazione

# Non chiamare exec_(), la prossima chiamata esegue l'applicazione
runapp(globals())   # NON MODIFICARE
