from dictionary_comprehension import print_dict_comprehension
from dictionary_pop import pop_item_by_key, pop_dict_last_item
from dictionary_search import search_item_square_bracket, search_item_by_get
from dictionary_merge import merge_dict_unique_keys
from dictionary_match import match_day_task
# a=5
# b=7
# c=5+7
# print(f'The sum of 5 and 7 is:{c}')
names=['Narayana', 'Jagannath']    
ages=[100, 100]
names_ages:dict=print_dict_comprehension(names, ages)

# Print the dictionary
print(f'The Dictionary Comprehension is:\n{names_ages}')

# Remove the item
pop_dict_last_item()
pop_item_by_key('Kelly')

# Search the Item
search_item_square_bracket('Kelly')
search_item_by_get('Mary')

# Merge two dictionaries
name_dict_1={'name':'John'}
age_dict_1={'age':23}
result=merge_dict_unique_keys(name_dict_1, age_dict_1)
print(f'The Merged Dictionary is:{result}')

# Match Value for the Key
day_task=match_day_task('Thursday')
print(day_task)

day_task=match_day_task('Sunday')
print(day_task)
