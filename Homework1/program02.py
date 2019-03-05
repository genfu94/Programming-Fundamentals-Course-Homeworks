'''Write a stutter(s, n) function that returns a string starting with 
the repetition n times of the first character of s. Repetitions are separated 
by spaces, and the returned string ends with s. You can assume non empty s. Examples:

stutter('hello', 4)    returns  'h h h h hello'
stutter('hello', 0)    returns  'hello'
stutter('Python', 3)  returns  'P P P Python'
'''

def stutter(s, n):
    ns = '';
    
    for i in range(n) :
        ns += s[0];
        ns += " ";
    
    ns += s;
    
    return ns;

print stutter('hello', 4);
print stutter('hello', 0);
print stutter('Python', 3);
