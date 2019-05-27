import MySQLdb, random, sys

# conexiune cu baza de date
db = MySQLdb.connect(host="db-mysql",
                     user="root",
                     passwd="sqlrootpass",
                     db="newDatabase")

# crearea tabelei
def creare_tabela():
	cursor = db.cursor()
	cursor.execute("CREATE TABLE tickets (ID varchar(10), sursa varchar(255), destinatie varchar(255), oraPlecare int NOT NULL, ziPlecare int NOT NULL, durata int NOT NULL, nrLocuri int, booking int, sold int, PRIMARY KEY(ID))")
	db.commit()
	cursor.close()
	print 'Tabela tickets a fost creata cu succes.'

# adugarea unui zbor intr-o tabela
def adaugare_zbor(sursa, destinatie, oraPlecare, ziPlecare, durata, nrLocuri):
	# verificare oraPlecare si ziPlecare
	if (int(oraPlecare) < 0 or int(oraPlecare)  > 23):
		print 'Ora de Plecare trebuie sa fie intre 0 si 23'
		return
	if (int(ziPlecare)  < 1 or int(ziPlecare)  > 365):
		print 'Ziua de Plecare trebuie sa fie intre 1 si 365'
		return
	# variabilele pentru id-ul zborului, numarul rezervarilor si numarul vanzarilor
	flightId = random.randint(1, 999999999)
	booked = 0;
	sold = 0;
	cursor = db.cursor()
	cursor.execute("INSERT INTO tickets (ID, sursa, destinatie, oraPlecare, ziPlecare, durata, nrLocuri, booking, sold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
		(flightId, sursa, destinatie, oraPlecare, ziPlecare, durata, nrLocuri, booked, sold))
	db.commit()
	cursor.close()
	print 'Zborul a fost adaugat cu succes.'

# anularea unui zbor intr-o tabela
def anulare_zbor(id_zbor):
	cursor = db.cursor()
	cursor.execute("SELECT ID FROM tickets WHERE ID=%s", [id_zbor])
	data = cursor.fetchall()
	if (cursor.rowcount == 0):
		print 'Id-ul zborului este gresit'
		return
	cursor.execute("DELETE FROM tickets WHERE ID=%s", [id_zbor])
	db.commit()
	cursor.close()
	print 'Zborul a fost sters cu succes.'

# lista zborurilor intr-o tabela
def lista_zborurilor():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM tickets")
	for row in cursor.fetchall():
		print row

# functia de exit
def exit():
	sys.exit(0)

#interfata text
while True:
	# citire comanda
    x = raw_input('> ')
    l = x.split()
    # functie + parametrii
    func = l[0]
    args = l[1:]

    # verifica daca functia se gaseste in dictionar
    try:
        f = {
        		'creare_tabela': creare_tabela,
                'adaugare_zbor': adaugare_zbor,
                'anulare_zbor': anulare_zbor,
                'lista_zborurilor': lista_zborurilor,
                'exit': exit,

        }[func]
        
        # executa functia cu parametrii
        f(*args)
    except Exception as e:
        print 'error', str(e)
