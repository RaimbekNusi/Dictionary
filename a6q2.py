#Raimbek Nussipkhozhin, NFU892, 11313819, Jeffrey Long
name = []
names = []
type = []
types = []
locations = []

def read_pokedata(x):
    """
    The function opens and reads a txt file and creates a database
    :param x: is a txt file, in this case pokemonLocations.txt
    :return: database, which is dictionary containing a database based on the txt file created by the
    function
    """
    database = {}
    data_names = {}
    f = open(x, "r")
    for line in f:
        name.append(line.strip())
        for i in range(len(name)):
            n = name[i]
            text = n.split(",")
        names.append(text[0])
        types.append(text[1])
        locations.append(text[2:7])
        data_names = {"Name" : names[i],
                      "Type" : types[i],
                      "Location" : locations[i]}
        database[names[i]] = data_names
    return database


def find_continents(x):
    """
    The function shows all of the locations where you could find pokemons
    :param x: is a dictionary, containing a database created by function "read_pokedata()"
    :return: text2, which is a list containing strings of names of all of the locations
    """
    text2 = []
    dict = {}
    for i in x:
        dict = x[i]
        dict = dict["Location"]
        for i in dict:
            if i not in text2:
                text2.append(i)
    return text2


def pokemon_in_continent(x, y):
    """
    The function makes a list of all the pokemon that could be found in the certain location
    :param x: is a dictionary, containing a database created by function "read_pokedata()"
    :param y: A string/An item from a list developed by the function "find_continents", containing names
    of locations
    :return: text, which is a list of names of all the pokemons that could be found in the certain location
    """
    dict = {}
    text = []
    for i in x:
        dict = x[i]
        if y in dict["Location"]:
            text.append(dict["Name"])
    return text

def count_types(x, y):
    """
    The function counts how many of each pokemon type occur within a certain location
    :param x: is a dictionary, containing a database created by function "read_pokedata()"
    :param y: a list created by the function "pokemon_in_continent", containing pokemon names as a string
    :return: new, which is a dictionary containing types and number of each pokemon type
    """
    dict = {}
    new = {}
    text = []
    for i in x:
        dict = x[i]
        for i in y:
            if i == dict["Name"]:
                text.append(dict["Type"])
    for i in y:
        new = {i:text.count(i) for i in text}
    return new

text = []
text = find_continents(read_pokedata("pokemonLocations.txt"))
number = []
for i in range(len(text)):
    number = pokemon_in_continent(read_pokedata('pokemonLocations.txt'), text[i])
    print(text[i], ": ", str(len(number)), " total", "\n", count_types(read_pokedata("pokemonLocations.txt"),pokemon_in_continent(read_pokedata('pokemonLocations.txt'), text[i])))