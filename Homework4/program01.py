'''Definire una classe PColor e una classe PImage secondo le seguenti specifiche.
La classe PColor rappresenta un pixel che puo' avere un colore RGB o essere
trasparente e deve implementare i seguenti metodi:

- Costruttore, senza argomenti, che inizializza l'oggetto come pixel trasparente.
  
- set_RGB(r, g, b) imposta il colore RGB dell'oggetto con i valori r,g,b e
  ritorna l'oggetto.

- to_RGB() ritorna una tripla (r,g,b) che sono i valori dei canali RGB
  dell'oggetto. Se e' trasparente, ritorna (255,255,255).

- set_transparent() imposta l'oggetto come pixel trasparente.

- istransparent() ritorna True se l'oggetto e' trasparente, False altrimenti.

La classe PImage rappresenta un'immagine che sara' implementata come matrice
(lista di liste) di oggetti PColor e deve implementare i seguenti metodi:

- Costruttore, con argomento fname, legge dal file fname l'immagine PNG e
  inizializza l'immagine dell'oggetto con tale immagine.

- size() ritorna una coppia (w, h) dove w e h sono la larghezza e l'altezza
  dell'immagine dell'oggetto.

- get_pixel(i, j) ritorna l'oggetto PColor del pixel in posizione (i, j)
  dell'immagine dell'oggetto. L'oggetto PColor ritornato e' proprio quello
  usato dall'immagine, per cui modificando questo si modifica l'immagine.

- set_transparent(rgbs, t) imposta come trasparenti tutti i pixels dell'immagine
  dell'oggetto il cui colore e' a distanza al piu' t da uno dei colori (espressi
  come triple RGB) della lista rgbs. La distanza e' la somma delle differenze
  assolute delle componenti colore.

- copy(pimg, x, y) copia l'immagine pimg (di tipo PImage) sull'immagine
  dell'oggetto con lo spigolo in alto a sinistra in (x, y). Sono copiati
  solamente i pixel di pimg che non sono trasparenti.

- save(fname) salva l'immagine dell'oggetto nel file fname.

Se necessario, si possono aggiungere altri metodi ad entrambe le classi.

Per gli esempi vedere il file grade01.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework.
'''

import image

class PColor :
	
	def __init__ ( self ) :
		
		self . r = 255
		
		self . g = 255
		
		self . b = 255
		
		self . isTransparent = True
	
	def __init__ ( self , rgb ) :
		
		self . r , self . g , self . b = rgb
		
		self . isTransparent = False
	
	def istransparent ( self ) :
		
		return self . isTransparent
	
	def set_RGB ( self , r , g , b ) :
		
		self . isTransparent = False
		
		self . r = r
		
		self . g = g
		
		self . b = b
		
		return self
	
	def SetRGB ( self , rgb ) :
		
		self . isTransparent = False
		
		self . r , self . g , self . b = rgb
		
		return self
	
	def to_RGB ( self ) :
		
		if self . isTransparent :
			
			return ( 255 , 255 , 255 )
		
		else :
			
			return ( self . r , self . g , self . b )
	
	def set_transparent ( self ) :
		
		self . isTransparent = True
	
	def Distance ( self , rgb ) :
		
		d = 0
		
		d += abs ( self . r - rgb [ 0 ] )
		
		d += abs ( self . g - rgb [ 1 ] )
		
		d += abs ( self . b - rgb [ 2 ] )
		
		return d

class PImage :
	
	def __init__ ( self , fname ) :
		
		self . img = [ ]
		
		tempImg = image . load ( fname )
		
		width = len ( tempImg [ 0 ] )
		
		height = len ( tempImg )
		
		for r in range ( height ) :
			
			imgRow = [ ]
			
			for c in range ( width ) :
				
				imgRow . append ( PColor ( tempImg [ r ] [ c ] ) )
			
			self . img . append ( imgRow )

	def size ( self ) :
		
		return ( len ( self . img [ 0 ] ) , len ( self . img ) )
	
	def get_pixel ( self , i , j ) :
		
		return self . img [ j ] [ i ]
	
	def set_transparent ( self , rgbs , t ) :
		
		width , height = self . size ( )
		
		for r in range ( height ) :
			
			for c in range ( width ) :
				
				for i in rgbs :
					
					if self . img [ r ] [ c ] . Distance ( i ) <= t :
						
						self . img [ r ] [ c ] . set_transparent ( )

	def inside ( self , i , j ) :
		
		width , height = self . size ( )
    	
		return 0 <= i < width and 0 <= j < height
	
	def ToRGB ( self ) :
		
		rgbImg = [ ]
		
		width , height = self . size ( )
		
		for r in range ( height ) :
			
			rgbImgRow = [ ]
			
			for c in range ( width ) :
				
				rgbImgRow . append ( self . img [ r ] [ c ] . to_RGB ( ) )
			
			rgbImg . append ( rgbImgRow )
		
		return rgbImg		
	
	def copy ( self , pimg , x , y ) :
		
		width , height = pimg . size ( )
		
		for r in range ( height ) :
			
			for c in range ( width ) :
			
				if not pimg . get_pixel ( c , r ) . istransparent ( ) :
					
					if self . inside ( c + x , r + y ) :
						
						self . img [ r + y ] [ c + x ] . SetRGB ( pimg . get_pixel ( c , r ) . to_RGB ( ) )
	
	def save ( self , fname ) :
		
		image . save ( fname , self . ToRGB ( ) )
