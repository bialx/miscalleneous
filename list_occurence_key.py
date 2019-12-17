def occurence(l):
    """ Function to create from a list a dictionary with the number of times the key appear in the list as a value
        Here we rather return a list instead of a dictionnary """

    liste_occurence = []
    compte = {}.fromkeys(set(l),0)
    for valeur in l:
        compte[valeur] += 1
    for cle, valeur in compte.items():
        liste_occurence.append((cle, valeur))
    return liste_occurence
