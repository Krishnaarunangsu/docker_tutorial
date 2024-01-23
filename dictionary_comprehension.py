def print_dict_comprehension(names:list, ages:list)->dict:
    """
    print the dictionary after successful dictionary comprehension
    """
    combined_dict:dict={key:value for key, value in zip(names, ages)}
    # print(f'The Dictionary Comprehension is:{combined_dict}')
    return combined_dict

# nam=['Narayana', 'Jagannath']    
# age=[100, 100]
# c_dict= print_dict_comprehension(nam, age)
# print(f'The Dictionary Comprehension is:{c_dict}')