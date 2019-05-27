NUME: Nastasiu Ciprian Marius
GRUPA: 341C2

Tema se ruleaza astfel:
	- se ruleaza scriptul "db" pentru crearea bazei de date in docker
	- se ruleaza scriptul "start" pentru rularea docker-composer-ul care porneste serverul, clientul, adminul si leaga 
	componentele intre ele dupa cum este descris in fisierul yaml
	- se ruleaza scriptul "admin" pentru a activa interfata text
		-- prima data trebuie sa fie rulata functia creare_tabela() pentru a fi creata tabela tickets
		-- functiile adaugare_zbor, anulare_zbor, lista_zborurilor cu prametrii mentionati in enuntul temei vor fi disponibile
		-- functia exit pentru a iesi din interfata
	- se ruleaza scriptul "client" pentru a rula functiile get_route, book, buy cu parametrii mentionati in enuntul temei
		-functiile creeaza url-ul si apeleaza functiile getOptimalRoute, bookTicket si buyTicket