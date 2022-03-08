"""
write a function that takes a dictionary
count how many keys in the dictionary has the value "online"
"""
objeto={
    'status1':'online',
    'status2':'offline',
    'status3':'online',
    'status4':'online'
}
def count_values(obj):
    counter=0
    for key in obj:
        if(obj[key]=='online'):
            counter=counter+1
    return counter
    

print(count_values(objeto))