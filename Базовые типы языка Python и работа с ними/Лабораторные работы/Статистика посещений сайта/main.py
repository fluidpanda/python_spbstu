users: list = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

value_total: dict = {"Общее количество": len(users), "Уникальные посещения": len(set(users))}

print(value_total)
