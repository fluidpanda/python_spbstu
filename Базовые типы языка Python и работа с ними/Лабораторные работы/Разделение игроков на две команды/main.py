list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

list_players_len: int = len(list_players)
delimeter: int = int(list_players_len / 2)

print(list_players[0:delimeter], list_players[delimeter:], sep='\n')
