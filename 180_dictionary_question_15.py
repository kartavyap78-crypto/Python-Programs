# 15. We have following information on countries and their population (population is in crores),
# Country Population
# China 	143
# India 	136
# USA 	32
# UK 	21

# Using above create a dictionary of countries and its population

# Write a program that asks user for 4 type of inputs,

# option 1 print: if user enter print then it should print all countries with their population
# in this format,

#         china==>143
#         india==>136
#         usa==>32
#         uk==>21

# option 2 add: if user input add then it should further ask for a country name to add. 
# If country already exist in our dataset then it should print that it exist and do nothing.
# If it doesn't then it asks for population and add that new country/population in our dictionary 
# and print it

# option 3 remove: when user inputs remove it should ask for a country to remove. If country exist
#      in our dictionary then remove it and print new dictionary using format shown above in (a). 
# Else print that country doesn't exist!

# option 4 query: on this again ask user for which country he or she wants to query. 
# When user inputs that country it will print population of that country.


details = {"China" : 143 , "India" : 136 , "USA" : 32 , "UK" : 21}

choice = input("enter a choice = ")




if choice == "print":
    print("Country\tPopulaton(in crores)")
    for k,v in details.items():
        print(k,"\t",v,"\t")

if choice == "add":
    c = input("enter a country = ")

    if c in details:
        print("It exists")
    else:
        p = int(input("enter a population = "))

        details[c] = p
        print("Country\tPopulaton(in crores)")
        for k , v in details.items():
            print(k,"\t",v,"\t")

if choice == "remove":
    c = input("enter a country = ")

    if c in details:
        details.pop(c)
        print(details)
    else:
        print("Country is not exists")

if choice == "query":
    c = input("enter a country = ")

    count = 0
    print("Country\tPopulaton(in crores)")
    for k , v in details.items():
        if k == c:
            print(k,"\t",v,"\t")
            count = count + 1
    if count == 0:
        print("Country is not exists")