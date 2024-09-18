
#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Adds all unique integers in a list(Only once for each integr).'''
    alll = 0
    for x in set(my_list):
        alll += x
    return (alll)

