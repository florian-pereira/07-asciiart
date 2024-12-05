"""
Ce module contient deux algorithmes pour encoder une chaîne de caractères :
1. Un algorithme itératif qui crée une liste de tuples (caractère, nombre d'occurrences).
2. Un algorithme récursif qui fait la même chose de manière récursive.
"""
import sys
sys.setrecursionlimit(1100)

def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme itératif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: Liste des tuples (caractère, nombre d'occurrences).
    """
    characters = [s[0]]
    occurrences = [1]
    k = 1

    while k < len(s):
        if s[k] == s[k - 1]:
            occurrences[-1] += 1
        else:
            characters.append(s[k])
            occurrences.append(1)
        k += 1

    return list(zip(characters, occurrences))


def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme récursif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: Liste des tuples (caractère, nombre d'occurrences).
    """
    if not s:
        return []

    char = s[0]
    count = 1

    while count < len(s) and s[count] == char:
        count += 1

    return [(char, count)] + artcode_r(s[count:])


def main():
    """
    Fonction principale pour tester les deux méthodes d'encodage (itérative et récursive).
    """
    chaine = 'MMMMaaacXolloMM'

    # Résultats avec les deux méthodes
    print("Résultat avec l'algorithme itératif :", artcode_i(chaine))
    print("Résultat avec l'algorithme récursif :", artcode_r(chaine))


if __name__ == "__main__":
    main()
