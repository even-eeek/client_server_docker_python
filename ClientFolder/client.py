import requests, sys

# url pentru getOptimalRoute
url_getRoute = 'http://server:80/getOptimalRoute/'
# url pentru bookTicket
url_book = 'http://server:80/bookTicket/'
# url pentru buyTicket
url_buy = 'http://server:80/buyTicket/'

# functiile care apeleaza functiile serverului
def get_route(sursa, destinatie, maxFlights, ziPlecare):
	new_url = url_getRoute + str(sursa) + '/' + str(destinatie) + '/' + str(maxFlights) + '/' + str(ziPlecare)
	response = requests.get(new_url).content
	print response
def book(flightIDs):
	new_url = url_book + str(flightIDs)
	response = requests.get(new_url).content
	print response
def buy(reservationID, creditCardInformation):
	new_url = url_buy + str(reservationID) + '/' + str(creditCardInformation)
	response = requests.get(new_url).content
	print response
def exit():
	sys.exit(0)

# interfata text
while True:
    # citire comada
    x = raw_input('> ')
    l = x.split()
    # functie + parametrii
    func = l[0]
    args = l[1:]

    # verifica daca functia se gaseste in dictionar
    try:
        f = {
                'get_route': get_route,
                'book': book,
                'buy': buy,
                'exit': exit,

        }[func]
        
        # executa functia cu parametrii
        f(*args)
    except Exception as e:
        print('error', str(e))