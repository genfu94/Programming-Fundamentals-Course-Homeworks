'''Scrivere una funzione polarize(fname_in, colors, fname_out) che presa in
input un'immagine in formato PNG nel file fname_in e una lista colors di colori,
crea una nuova immagine con le stesse dimensioni dell'immagine originale in
cui ogni pixel ha un colore che e' il colore nella lista colors che piu' si
avvicina al colore originale del pixel, la funzione poi salva la nuova immagine
nel file fname_out. Per misurare la vicinanza di due colori la funzione usa
la somma delle differenze assolute delle tre componenti colore (RGB). Piu'
questa somma e' piccola e piu' i colori sono vicini. A parita' di vicinanza
la funzione seleziona il colore che viene prima nella lista colors.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''

import image as im

#-----------------------------------------------------------------------

def ColorsDistance ( firstColor , secondColor ) :
	
	distance = 0
	
	for i in range ( 3 ) :
		
		distance += abs ( firstColor [ i ] - secondColor [ i ] )
	
	return distance

#-----------------------------------------------------------------------

def ApproximateColor ( color , cList ) :
	
	closestColor = ( 1000 , 1000 , 1000 )
	
	for c in cList :
		
		if ColorsDistance ( color , c ) < ColorsDistance ( color , closestColor ) :
			
			closestColor = c
	
	return closestColor
		
#-----------------------------------------------------------------------		

def polarize(fname_in, colors, fname_out):
	
	inputImage = im . load ( fname_in )
	
	outputImage = []
	
	for r in range ( len ( inputImage ) ) :
		
		outputImageRow = []
		
		for c in range ( len ( inputImage [ 0 ] ) ) :
			
			outputImageRow . append ( ApproximateColor ( inputImage [ r ] [ c ] , colors ) )
		
		outputImage . append ( outputImageRow )
	
	im.save ( fname_out , outputImage )
					
#-----------------------------------------------------------------------			
	
polarize('img03_01_in.png', [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 165, 0), (238, 130, 238)], 'img03_01_out.png')
