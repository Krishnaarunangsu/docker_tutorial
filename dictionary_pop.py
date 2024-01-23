my_dict={'Kelly':23, 'John':35, 'Tom':37}

def pop_dict_last_item():
    """
    Remove the last item of the dictionary
    """
    # my_dict={'Kelly':23, 'John':35, 'Tom':37}
    print(f'The last item of the dictionary is:{my_dict.popitem()}')

def pop_item_by_key(key:str) :
    """
    Remove the item of the dictionary specified by the key
    """
    print(f'The removed item is:{my_dict.pop(key)}')

#if __name__=='__main__':
#    pop_dict_last_item()
#    pop_item_by_key('Kelly')    