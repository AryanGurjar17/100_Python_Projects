programming_dictionary = {"Bug": "an error in a program that prevents the program from running",
                          "Function": "a piece of code that you can easily call over and over again ",
                          "Loop": "The action of doing something over and over again ",
                          }
print(programming_dictionary["Function"])

#edit an item in a dictionary
programming_dictionary["Bug"] = "a moth in your computer."
print(programming_dictionary)

#loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])   #key , thing.... any word