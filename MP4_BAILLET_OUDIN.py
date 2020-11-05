import sqlite3
conn = sqlite3.connect('MP4.db')
cur = conn.cursor()
conn.commit()
cur.execute("CREATE TABLE IF NOT EXISTS ANNUAIRE(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT,prenom TEXT,telephone INT,email TEXT,qualite TEXT)")
datas = [
        ('Baillet','Maxime','0783115214','sparadra2@gmail.com','ami'),
        ('Oudin','Clément','0855334455','lavaclem@gmail.com','ami'),
        ('Duchenne','Nils','0934543533','bgsdferzrf@gmail.com','famille'),
        ('Franz','Loic','0877887789','fgegfrggdgbd@gmail.com','famille'),
        ('Mans','Léo','0889777380','fbhehfbhbsbzgg@gmail.com','collegue'),
        ('Barreau','Aurélien','00835563','dfgezgkgr@gmail.com','collegue'),
        ('Péchiodat','Maxence','032453545','dfgfhdhtt@gmail.com','ami')

]

cur.executemany("INSERT INTO ANNUAIRE(nom,prenom,telephone,email,qualite) VALUES(?, ?, ?, ?, ?)", datas)
conn.commit()
choix=" "
while choix!=5:
    print("""Base de donnee annuaire :
      1--> insertion
      2--> supression
      3--> modifier
      4--> recherche
      5--> fin du programme""")

    choix=int(input("choix : "))

    
    
    if choix==1:
        def ajouter():
            nom=str(input("Nom :"))
            prenom=str(input("Prenom :"))
            phone=int(input("Telephone :"))
            email=str(input("Email :"))
            qualite=str(input("Qualité :"))
            lst=(nom,prenom,phone,email,qualite)
            return lst
        liste=[ajouter()]
        cur.executemany("INSERT INTO ANNUAIRE(nom,prenom,telephone,email,qualite) VALUES(?, ?, ?, ?, ?)", liste)
        conn.commit()
        
        
    elif choix==2:
        def suppr():
            supprimer=[str(input("Nom de la personne que vous souhaitez supprimez : "))]
            return supprimer
        sup=suppr()
        cur.execute("DELETE FROM ANNUAIRE WHERE nom = ?",sup)
        conn.commit()


    elif choix==3:
        def modif():
            ligne=str(input("Ligne a modifier :"))          #ecrire en minuscule et sans faute
            mod=str(input("Quelle categorie a modifier :"))
            apres=str(input("Modification :"))
            lst=[apres,ligne,mod]
            return lst
        liste=modif()
        if liste[2]=="nom":
            liste.pop()
            cur.execute('UPDATE ANNUAIRE SET nom = ? WHERE id = ?', liste)
            conn.commit()
        elif liste[2]=="prenom":
            liste.pop()
            cur.execute('UPDATE ANNUAIRE SET prenom = ? WHERE id = ?', liste)
            conn.commit()
        elif liste[2]=="telephone":
            liste.pop()
            cur.execute('UPDATE ANNUAIRE SET telephone = ? WHERE id = ?', liste)
            conn.commit()
        elif liste[2]=="email":
            liste.pop()
            cur.execute('UPDATE ANNUAIRE SET email = ? WHERE id = ?', liste)
            conn.commit()
        else:
            liste.pop()
            cur.execute('UPDATE ANNUAIRE SET qualite = ? WHERE id = ?', liste)
            conn.commit()
            
            
    elif choix == 4:
        def recherche():
            print("""Que recherchez-vous :
                1--> Nom
                2--> Qualité""")
            ch=int(input("choix de recherche :"))
            if ch==1:
                Nom=[str(input("Quel nom recherchez-vous :"))]
                cur.execute('SELECT * FROM ANNUAIRE WHERE nom = ?',Nom)
                conn.commit()
                result=cur.fetchall()
            elif ch==2:
                Qualité=[str(input("Quel qualité recherchez-vous (ami,famille...) : "))]
                cur.execute('SELECT * FROM ANNUAIRE WHERE qualite = ?',Qualité)
                conn.commit
                result=cur.fetchall()
            return result
        print(recherche())

    elif choix == 5:
        print("Fin du programme")
        
            
cur.close()
conn.close()