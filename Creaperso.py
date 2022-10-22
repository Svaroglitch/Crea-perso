'''
CREAPERSO
createur : Lehag

Creer des perso avec inventaire, metier, type, caracteristique (systeme S.P.E.C.I.A.L) et aptitude
Adapté au systeme de jeu FLT simplifié.

'''

import random

list_perso = list()
nbp = int(input("nombre de perso ?"))
for x in range(0,nbp):
    list_apt = (("Sang froid","Vous êtes immunisé au effet qui diminue la PER, le CHAR ou la CHAN"),
            ("Berserk","votre Force est augmenté de 1 point pour chaque autre competence en dessous de 4"),
            ("Bluff: Ajouter a votre CHAR la moitié de votre CHAN"),
            ("Androgyne: Vous êtes vu comme une femme ou un homme en fonction de ce qui vous arrange"),
            ("Organisé : Vous êtes immunisé au effet qui diminue l'INT, Les objets qui ont un poid de moins de 2 ne sont pas compté"),
            ("Surarmé : vous pouvé porté autant d'armes et de munition que vous voulez"),
            ("Aptitude de Chasse : Bonus d'attaque face au bête"),
            ("Tete solide : Les tir a la tête ne vous inflige pas plus de dégat "),
            ("Tombeur : Bonus de CHAR quand vous parlez avec une personne du sexe opposé"),
            ("Farfouilleur : Augmente les chance de trouver des munition pendant une fouille"),
            ("Mains Baladeuse : bonus pour voler"),
            ("Organisme Rapide : Les effet des comsommable sont deux fois plus puissant mais dure deux fois moins longtemps"),
            ("Specialiste : doublez votre stat la plus grosse, divisé par deux les autre stat"),
            ("Sensible : Votre force est divisé par deux, votre charisme est multiplié par deux")
            )
            
    list_rac = ("Slave","Celte","Romain","Indo-européen","Mongol","Nord-asiatique","Sudasiatique","Primo-americain","Sud-americain",
            "Insulaire","Sudafricain","Arabe","Semite","Subsaharien")

    list_met = ("Chasseur","Politicien","Officier","Soldat","Technicien","Magistrat","Milicien","Ingenieur","Financier","Journaliste",
            "Medecin","Infirmier","Dealer","Mafieux","Prostitué","Curé","Religieux","Comptable","Pompier","Chirurgien","Cordonnier",
            "Hackers","Prof")
    list_inv = ("Clef à molette","Fusil de chasse (12G)","Pistolet (9MM)","Livre","Sac à dos","torche","Couteau de cuisine",
            "Sabre","Gourde","Fusil au canon scié (12G)","Uzi (9mm)","Pied de biche","Casque de moto", "Revolver (cal44)",
            "Boite de munitions 9mm", "Boite de Cal44", "Boite de cal 12","Sandwich","Conserve", "paquet de cigarette",
            "radio","boite de thon","Bandage","Anti-douleur","Biere","Bouteille de whisky","Barre à mine","batte de basseball",
            "Couteau de Boucher")
            


    dicp= {}
    apt = str(random.choice(list_apt))
    rac = str(random.choice(list_rac))
    met = str(random.choice(list_met))
    inv = random.sample(list_inv,5)

    
    S = random.randint(1,10)
    P = random.randint(1,10)
    E = random.randint(1,10)
    C = random.randint(1,10)
    I = random.randint(1,10)
    A = random.randint(1,10)
    L = random.randint(1,10)

    while S+P+E+C+I+A+L != 30:
        if S+P+E+C+I+A+L > 30:
            S -= random.randint(0,3)
            P -= random.randint(0,3)
            E -= random.randint(0,3)
            C -= random.randint(0,3)
            I -= random.randint(0,3)
            A -= random.randint(0,3)
            L -= random.randint(0,3)
        
        elif S+P+E+C+I+A+L < 30:
            S += random.randint(0,3)
            P += random.randint(0,3)
            E += random.randint(0,3)
            C += random.randint(0,3)
            I += random.randint(0,3)
            A += random.randint(0,3)
            L += random.randint(0,3)
    
        if S < 1 :
            S = random.randint(0,10)
        if P < 1 :
            P = random.randint(0,10)
        if E < 1 :
            E = random.randint(0,10)
        if C < 1 :
            C = random.randint(0,10)
        if I < 1 :
            I = random.randint(0,10)
        if A < 1 :
            A = random.randint(0,10)
        if L < 1 :
            L = random.randint(0,10)

    nom = input("nom ?")
    
    dicp = {"nom" : nom,
            "metier" : met,
            "type" : rac,
            "aptitude" : apt,
            "inventaire" : str(inv),
            "Force" : str(S),
            "Perce" : str(P),
            "Endur" : str(E),
            "Chari" : str(C),
            "Intel" : str(I),
            "Agili" : str(A),
            "Chanc" : str(L)
            }
    list_perso.append(dicp)
    
for x in list_perso:
    print()
    print(x["nom"])
    print(x["metier"] + " " + x["type"])
    print(x["aptitude"])
    
    









