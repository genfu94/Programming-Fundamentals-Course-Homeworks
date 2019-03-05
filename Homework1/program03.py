'''Write a function hms(lst) that takes as input a list lst of timestamps expressed
in seconds and returns a new list such that for each timestamp t in lst, it has a timestamp
t' equal to t converted in hours, minutes and seconds. Example:
    
hms([3600, 10000, 0, 1000])  returns  
    ['1h 0m 0s', '2h 46m 48s', '0h 0m 0s', '0h 16m 40s']
'''

def hms(lst):
    '''Implementare la funzione qui'''
    new_list = []
    
    for obj in lst :
    	seconds = ''
    	seconds += str(obj/3600) + 'h ' + str((obj%3600)/60) + 'm ' + str((obj%3600)%60) + 's'
    	new_list.append(seconds);

    return new_list

print hms([3600, 10000, 0, 1000])
