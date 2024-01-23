my_dict={'Kelly':23, 'John':35, 'Tom':37}

def search_item_square_bracket(key:str):
    """
    Search Item by Square Bracket
    """
    print(f'The Searched item is:{my_dict[key]}')

def search_item_by_get(key:str) :
    """
    Search Item by Get(Softly handles if the key is not present in the dictionary)
    """
    print(f'The Searched item is:{my_dict.get(key)}')


# if __name__=="__main__":
#    search_item_square_bracket('Kelly')
#    search_item_by_get('Mary')
