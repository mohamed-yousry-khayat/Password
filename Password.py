import hashlib as hash


def mdp():

    mdp_long = False
    mdp_min = False
    mdp_maj = False
    mdp_numb = False
    mdp_spl = False
    mdp_valid = False

    while mdp_valid is False:
        liste_carac_spl = ["!", "@", "#", "$", "%", "^", "&", "*"]

        psswrd = input("Veuillez saisir un mot de passe contentant les caractère suivant :"
                       "\n8 caractères."
                       "\nUne lettre majuscule."
                       "\nUne lettre minuscule."
                       "\nUn chiffre."
                       "\nUn caractère spécial (!, @, #, $, %, ^, &, *).")

        if len(psswrd) > 8:
            mdp_long = True

        for i in psswrd:
            if i.isupper():
                mdp_maj = True

        for i in psswrd:
            if i.islower():
                mdp_min = True

        for i in psswrd:
            if i.isdigit():
                mdp_numb = True

        for i in psswrd:
            if i in liste_carac_spl:
                mdp_spl = True

        if mdp_long is True and mdp_min is True and mdp_maj is True and mdp_numb is True and mdp_spl is True:
            mdp_valid = True

    print("Mot de passe valide, cryptage en cours")

    mdp_crypte = hash.sha256(psswrd.encode())
    print("Le mot de passe crypté est:", mdp_crypte.hexdigest())


mdp()
