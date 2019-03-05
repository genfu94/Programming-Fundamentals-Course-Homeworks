'''Nell'albero di parsing di un file HTML, il t-path di un nodo u e' la lista
dei tags dei nodi che vanno dalla radice dell'albero, cioe' il nodo con tag
'html', fino al nodo u.
Scrivere una funzione tagset(htmlfile, tp) che preso in input il percorso di
un file HTML e una lista di tags tp, ritorna un insieme (tipo set) che contiene
l'unione di tutti i tags presenti nei sottoalberi relativi ai nodi con t-path tp.

Per gli esempi vedere il file grade03.txt

Suggerimento: usare il modulo html e definire un'opportuna classe...

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard o non sono forniti
nella cartella dell'homework.
'''

import html

class HTMLNode :
	
	def __init__ ( self , tag , attr , content , closed = True ) :
		
		self . tag = tag
		
		self . attr = attr
		
		self . content = content
		
		self . closed = closed
	
	def GetChildSubTree ( self ) :
		
		s = set ( )
		
		for child in self . content :
			
			if not child . IsText ( ) :
				
				s = s . union ( child . GetChildSubTree ( ) )
			
			else :
				
				s . add ( "_text_" )
		
		s . add ( self . tag )
		
		return s
	
	def GetTagNode ( self , path , level = 0 ) :
		
		l = [ ]
		
		if level == len ( path ) - 1 :
			
			l += [ self ]
		
		else :
			
			for child in self . content :
				
				if child . tag == path [ level + 1 ] :
					
					if not child . IsText ( ) :
					
						l += child . GetTagNode ( path , level + 1 )
					
					else :
						
						l += [ "_text_" ]
		
		return l
        
	def IsText (self ) :
		
		return self . tag == '_text_'

def ParseHTML ( fname ) :
	
	with open ( fname , 'U' ) as f :
	
		root = html . parse ( f . read ( ) , HTMLNode )
        
	return root


def tagset(htmlfile, tp) :
	
	s = set ( )
	
	tree = ParseHTML ( htmlfile )
	
	nodes = tree . GetTagNode ( tp )
	
	for n in nodes :
		
		if n != "_text_" :
		
			s = s . union ( set ( n . GetChildSubTree ( ) ) )
		
		else :
			
			s . add ( n )
	
	return s
