'''Write a function bytes(k, m, g) that returns the number of bytes
equal to the som of k KB, m MB and g GB. Examples:

bytes(0, 1, 0)  returns   1048576
bytes(3, 2, 1)  returns   1075842048
'''

def bytes(kb, mb, gb):
    '''Implementare la funzione qui'''
    return kb * ( 2 ** 10 ) + mb * ( 2 ** 20 ) + gb * ( 2 ** 30 )
    
print bytes(0, 1, 0)
print bytes(3, 2, 1)
