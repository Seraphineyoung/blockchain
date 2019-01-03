# Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.

# 1) Create a list of names and use a for loop to output the length of each name (len() ).

list_of_name = ['edem','Nancybabes','nina','enoanwan','Makims','Asibong','pam','Sarah']

for each_name in list_of_name:
    lenght_of_each_name = len(each_name)
    #print(len(each_name))

# 2) Add an if  check inside the loop to only output names longer than 5 characters.
       
# 3) Add another if  check to see whether a name includes a “n”  or “N”  character.
    if lenght_of_each_name > 5:
        if  'n' in each_name or 'N' in each_name:
            print(each_name)
# 4) Use a while  loop to empty the list of names (via pop() )