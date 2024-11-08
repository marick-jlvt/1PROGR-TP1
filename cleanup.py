def produit(type_de_comparaison, comparaison_logique) -> None:
    """
    Prend un comparateur et son symbole en argument, détermine tout les couples entrées sorties associé
    """
    CHOIX_POSSIBLE = [False, True]
    for choix_1 in CHOIX_POSSIBLES:
        for choix_2 in CHOIX_POSSIBLES:
            print(f"{choix_1} {type_de_comparaison} {choix_2} = {comparaison_logique(choix_1, choix_2)}")


if __name__ == "__main__":
    produit("&", lambda x, y: x and y)
    produit("|", lambda x, y: x or y)
    produit("^", lambda x, y: x ^ y)


def tris(chaine : str) -> str:
    """
    Ordonne la string par ordre alphabétique
    """
    chaine_ordre = []
    while len(chaine) != 0:
        indice_retenu = None
        lettre_retenu = None
        for indice, lettre in enumerate(chaine):
            if lettre_retenu is None or ord(k) < m:
                lettre_retenu = ord(k)
                indice_retenu = indice
        assert lettre_retenu is not None
        chaine_ordre.append(chaine[i])
        chaine = chaine[:i] + chaine[i + 1 :]
    return "".join(chaine_ordre)


if __name__ == "__main__":
    print(R("qwertyuiop"))
    print(R("asdfghjkl"))
    print(R("zxcvbnm"))
