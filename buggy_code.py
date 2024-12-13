"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
def extract_and_rearrange(string): # I have changed the spelling and made spaces between the words
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
    str_2 = "".join(string[6:13].split('ro')) # spelling mistake 
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17])) # I have added a underscore between str and 3. # double quotes missing and dot
    str_4 = "".join(string[21:29].split(string[23:28]))

    return str_1 + " " + str_2 + " " + str_3 + " " +str_4 # plus sign missing

def ultra_extrct_and_rearrange(string): # colon missing
    first_transform = extract_and_rearrange(string)
    return first_transform

print(ultra_extrct_and_rearrange("egthb quirock nwoGrb forijmpxv"))# parenthessis added , spelling mistake , spaces missing and underscore added.

