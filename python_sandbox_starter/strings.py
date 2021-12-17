# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


# String Formatting


# counting the power of strings 

string = 'cc'

count=1
temp_count = 1

for x in range(0, len(string)-1):

    if(string[x] == string[x+1]):
        temp_count+=1

    else:
        temp_count=1

    if(count < temp_count):
        count = temp_count


print(f'String power: {count}')

# String Methods
