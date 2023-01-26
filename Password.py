import hashlib as hash


def mdp():

    list_carac_spl = ["!", "@", "#", "$", "%", "^", "&", "*"]

    mdp_long = False
    mdp_min = False
    mdp_maj = False
    mdp_numb = False
    mdp_spl = False

    while mdp_long is False and mdp_min is False and mdp_maj is False and mdp_numb is False and mdp_spl is False:

        psswrd = input("Veuillez saisir un mot de passe contentant les caractère suivant :"
                       "\n8 caractères."
                       "\nUne lettre majuscule."
                       "\nUne lettre minuscule."
                       "\nUn chiffre."
                       "\nUn caractère spécial (!, @, #, $, %, ^, &, *).")

        if len(psswrd) > 8:
            mdp_long = True
        else:
            print("Condition non respectée, mot de pase trop court ")

        if psswrd.islower():
            print("Condition non respectée, aucune minuscule")
        else:
            mdp_min = True

        if psswrd.isupper():
            print("Condition non respectée, aucune majuscule")
        else:
            mdp_maj = True

        if psswrd.isdigit():
            print("Condition non respectée, aucun chiffre")
        else:
            mdp_numb = True

        if psswrd not in list_carac_spl:
            mdp_spl = True
        else:
            print("Condition non respectée, aucun caractère spécial")

    print("Mot de passe valide, cryptage en cours")

    mdp_crypte = hash.sha256(psswrd.encode())
    print("Le mot de passe crypté est:", mdp_crypte.hexdigest())


mdp()
