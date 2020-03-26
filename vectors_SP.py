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

    Examples
    --------
    >>> add_vectors([1, 2, 3], [1, 2, 5])
    [2, 4, 8]

    >>> add_vectors([-1, 3, 0, 6, 7], [0, 7, 10, -4, 3])
    [-1, 10, 10, 2, 10]

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

    Examples
    --------
    >>> scalar_mult(5, [1,2])
    [5, 10]

    >>> scalar_mult(3, [1,0,-1])
    [3, 0, -3]

    >>> scalar_mult(7, [3,0,5,11,2])
    [21, 0, 35, 77, 14]

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

    Examples
    --------
    >>> dot_product([1,1],[1,1])
    2

    >>> dot_product([1,2],[1,4])
    9

    >>> dot_product([1,2,1],[1,4,3])
    12

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

    Examples
    --------
    >>> replace("Mississippi","i","I")
    MIssIssIppI

    >>> replace("I love spom! Spom is my favorite food. Spom, spom, yum!","om","am")
    I love spam! Spam is my favorite food. Spam, spam, yum!
 
    """
    liste=s.split(old)
    glue=new
    return(glue.join(liste))


def nb_occurence(chaine):
    """ Creation of a dictionnary of letters and occurence from a chain chaine

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

    Examples
    --------
    >>> nb_occurence("ThiS is String with Upper and lower case Letters")
    {' ': 8, 'a': 2, 'c': 1, 'd': 1, 'e': 5, 'g': 1, 'h': 2, 'i': 4, 'l': 2, 'n': 2, 'o': 1,
    'p': 2, 'r': 4, 's': 5, 't': 5, 'u': 1, 'w': 2}

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
