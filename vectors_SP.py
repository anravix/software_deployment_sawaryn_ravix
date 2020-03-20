""" 
Realisation des fonctions
========================
"""

def add_vectors(vector1,vector2):
    """Creation of a vector by the addition of two others. 

    Note
    ----
    The two vectors must have the same dimension. 

    Parameters
    ----------
    vector1 : list
	    The first vector.
    vector2 : list
	    The second vector.

    Returns
    -------
    list
        Sum of the corresponding  elements of each list. 

    """
    mat = []
    for i in range (len(vector1)):
        mat.append(vector1[i]+vector2[i])
    return mat


def scalar_mult(scalar, vector):
    """Creation of a vector by the multiplication of a vector by a scalar. 

    Parameters
    ----------
    scalar : int
	    The multiplier integer.
    vector : list
	    The vector to multiply.

    Returns
    -------
    list
        The multiplication of the corresponding  elements of the list by a scalar. 

    """
    mat =[]
    for i in vector:
        mat.append(scalar*i)
    return mat


def dot_product(vec1,vec2):
    """Computation of dot product.

    Note
    ----
    The two vectors must have the same dimension. 

    Parameters
    ----------
    vec1 : list
	    The first vector.
    vec2 : list
	    The second vector.

    Returns
    -------
    int
        The sum of the products of the corresponding elements of each.

    """
    count=0
    for i in range (len(vec1)):
        count+=vec1[i]*vec2[i]
    return count

def replace(s,old,new):
    """Replace all occurences of old with new in the string s.

    Parameters
    ----------
    s : string
	    The string to modify.
    old : string
	    The pattern to modify in the string.
    new : 
        The new pattern to replace in the string. 

    Returns
    -------
    string
        The modified list on each pattern. 

    """
    liste=s.split(old)
    glue=new
    return(glue.join(liste))


def nb_occurence(chaine):
    """ Creation of a dictionnary of letters and occurence from a chaine chaine

    Note
    ----
    The chain can contain upper case.

    Parameters
    ----------
    chaine : chain
        The chain to analyze.

	Returns
	-------
	dictionnary
        The sort dictionnary by alphabetical order of the letters of the chain and their ocurrence in the chain. 

    """
    table={}
    for i in chaine.lower():
        if i not in table :
            table[i]=1
        else:
            table[i]+=1
    t=list(table.items())
    t.sort()

    table_trie = {}
    for i in t:
        for j in range(len(i)):
            table_trie[i[0]] = i[j]

    return table_trie

"""
Tests unitaires
---------------

"""
print(replace("Mississippi","i","I"))
print(replace("I love spom! Spom is my favorite food. Spom, spom, yum!","om","am"))

print(scalar_mult(5, [1,2]))
print(scalar_mult(3, [1,0,-1]))
print(scalar_mult(7, [3,0,5,11,2]))

print(add_vectors([1,1],[1,1]))
print(add_vectors([1,2],[1,4]))
print(add_vectors([1,2,1],[1,4,3]))

print(dot_product([1,1],[1,1]))
print(dot_product([1,2],[1,4]))
print(dot_product([1,2,1],[1,4,3]))

print(nb_occurence("ThiS is String with Upper and lower case Letters"))

