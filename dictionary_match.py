week_day_tasks:dict={
    'Monday': 'Learn Python',
    'Tuesday': 'Visit Grand Ma',
    'Wednesday': 'Go to the gym',
    'Thursday': 'Run a mile',
    'Friday': 'Go to a party'
}

def match_day_task(day:str):
    """
    Get the corresponding value from the dictionary
    if the key is present else show the message passed in the argument
    """
    result=week_day_tasks.get(day, 'Invalid Option')
    return result

  
# if __name__=="__main__":
#    day_task=match_day_task('Thursday')
#    print(day_task)
    