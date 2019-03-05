'''Scrivere una funzione findlines(t, w) che ritorna una lista di stringhe tali 
che ogni stringa riporta il numero di linea e il numero di occorrenze della 
parola w in quella linea del testo t (vedi gli esempi nel file grade03.txt),
sono riportate solamente le linee che contengono almeno un'occorrenza di w.
Per parola si intende una qualsiasi sequenza di caratteri alfabetici
(maiuscoli o minuscoli) di lunghezza masssimale. Per gli esempi vedere il
file grade03.txt.

AVVERTENZE: non usare caratteri non ASCII, come le lettere accentate;
non usare moduli che non sono nella libreria standard.
'''

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
    
    

def findlines(t, w):
    '''Implementare qui la funzione'''
    
    occurences = 0
    
    line_counter = 0
    
    string_list = []
    
    for line in t.splitlines() :
        
        occurences = 0
        
        for word in words( line ) :
            
            if word == w :
                
                occurences += 1
        
        if occurences > 0 :
            
            string_list.append( 'Line ' + str(line_counter) + ': ' + str(occurences) )
        
        line_counter += 1
    
    return string_list
        
print 
findlines('''Alice did not at all like the tone of this remark, and thought it would
be as well to introduce some other subject of conversation. While she
was trying to fix on one, the cook took the cauldron of soup off the
fire, and at once set to work throwing everything within her reach at
the Duchess and the baby--the fire-irons came first; then followed a
shower of saucepans, plates, and dishes. The Duchess took no notice of
them even when they hit her; and the baby was howling so much already,
that it was quite impossible to say whether the blows hurt it or not.''', 'the')