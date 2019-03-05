'''Scrivere una funzione fill(img_in, boundaries, pp_cc, img_out) che prende
in input i seguenti argomenti:
- img_in: file che contiene un'immagine in formato PNG, leggibile con la
  funzione load() del modulo image.
- boundaries: un insieme di tipo set di pixel dell'immagine, ognuno specificato
  da una coppia di coordinate (x, y). Come al solito le coordinate crescono
  verso destra e verso il basso e il pixel nell'angolo in alto a sinistra ha
  coordinate (0, 0).
- pp_cc: una lista di coppie (p, c) dove p e' un pixel (cioe' una coppia di
  coordinate) e c e' un colore espresso come tripla (r,g,b).
- img_out: il nome di un file in cui salvare l'immagine risultato.
La funzione per ogni elemento (p, c) della lista pp_cc deve colorare con il
colore c tutti i pixel che sono connessi al pixel p nel grafo di pixel
dell'immagine letta dal file img_in senza pero' attraversare i pixel in
boundaries. Ad esempio, se boundaries consiste di tutti i pixel del contorno
di un cerchio e p e' un pixel all'interno del cerchio, allora la funzione
ricolora con colore c tutti i pixel all'interno del cerchio (esclusi quelli in
boundaries). Infine la funzione salva sul file img_out (tramite la funzione
save() del modulo image) l'immagine modificata.
Per gli esempi vedere grade03.py, i file di input img03_01_in.png,
img03_02_in.png e quelli di output img03_01_check.png, img03_02_check.png,
img03_03_check.png, img03_04_check.png, img03_05_check.png.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework o non sono esplicitamente autorizzati.
'''

import image

def bound_circle(w, h, center, radius):
    import math
    cx, cy = center
    b = set()
    a = 0.5/radius
    ang = 0.0
    while ang <= 2*math.pi:
        x, y = cx + radius*math.sin(ang), cy + radius*math.cos(ang)
        x, y = int(round(x)), int(round(y))
        if x >= 0 and x < w and y >= 0 and y < h:
            b.add((x, y))
        ang += a
    return b

def bound(w, h, center, rx, ry, n):
    import math
    cx, cy = center
    b = set()
    m = 7.0/n
    a = 0.5/max(rx, ry)
    ang = 0.0
    while ang <= 2*n*math.pi:
        x, y = cx + rx*math.sin(m*ang), cy + ry*math.cos(ang)
        x, y = int(round(x)), int(round(y))
        if x >= 0 and x < w and y >= 0 and y < h:
            b.add((x, y))
        ang += a
    return b

ADJACENTS = ((-1,0),(0,1),(1,0),(0,-1))

def fill(img_in, boundaries, pp_cc, img_out):
    '''Implementare qui la funzione'''
    
    img = image . load ( img_in )
    
    w , h = len ( img [ 0 ] ) , len ( img )
    
    for pc in pp_cc :
    	
    	visited = set ( [ pc [ 0 ] ] )
    	
    	active = set ( [ pc [ 0 ] ] )
    	
    	while len ( active ) > 0 :
    		
    		newactive = set ( )
    		
    		while len ( active ) > 0 :
    			
    			x , y = active . pop ( )
    			
    			for dx , dy in ADJACENTS :
    				
    				px , py = x + dx , y + dy
    				
    				if px >= 0 and px < w and py >= 0 and py < h :
    					
    					if ( px , py ) not in boundaries :
    						
    						img [ py ] [ px ] = pc [ 1 ]
    						
    						if ( px , py ) not in visited :
    							
    							visited . add ( ( px , py ) )
    							
    							newactive . add ( ( px , py ) )
    			
    			active = newactive
    
    image . save ( img_out , img )
'''
b = bound_circle(500, 400, (250, 200), 80)

fill('img03_01_in.png', b, [((300,220), (255,0,0))], 'img03_01_out.png')'''
