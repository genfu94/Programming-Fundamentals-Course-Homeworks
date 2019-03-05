'''Scrivere una funzione codes(cs, ds) che prende in input una lista cs di 
stringhe che rappresentano codici e una lista ds di stringhe s tali che i primi
due caratteri di s contengono la lunghezza n di un codice i successivi n caratteri 
contengono un codice e i successivi 8 caratteri contengono una data nel formato
ggmmaaaa, la funzione deve modificare la lista cs in modo che per ogni codice di 
cod in cs se una stringa s di ds ha codice cod allora cod e' sostituito dai tre 
valori numerici della data di s, altrimenti cod e' rimosso. Per maggiore 
chiarezza, ogni stringa di ds ha il formato nnc...cggmmaaaa, dove la lunghezza
del blocco c...c e' uguale al numero specificato da nn. Si assume che non ci sono
due stringhe in ds con lo stesso codice. Per gli esempi vedere il file
grade02.txt

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''

#-------------------------------------------------------------------------------

def GetStringCodeLenght( string ) :
    
    return int( string[ 0 : 2 ] )

#-------------------------------------------------------------------------------

def GetStringCode( string ) :
    
    return string[ 2 : 2 + GetStringCodeLenght( string ) ]

#-------------------------------------------------------------------------------

def GetStringCodeDate( string ) :
    
    return string[ 2 + GetStringCodeLenght( string ) : ]

#-------------------------------------------------------------------------------

def SplitDate( date ) :
    
    dateList = []
    
    dateList += [ int( date[ 0 : 2 ] ) , int( date[ 2 : 4 ] ), int ( date[ 4 : 8 ] ) ]
    
    return dateList

#-------------------------------------------------------------------------------
    
def codes(cs, ds):
    '''Implementare qui la funzione'''
    
    newcs = []
    
    for csItem in cs :
        
        for dsItem in ds :
            
            if GetStringCode( dsItem ) == csItem :
                
                newcs += SplitDate( GetStringCodeDate( dsItem ) )
    
    del cs[:]
    
    cs += newcs
    
    return

#-------------------------------------------------------------------------------
