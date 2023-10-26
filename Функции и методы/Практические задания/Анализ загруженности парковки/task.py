# TODO Напишите функцию `calculate_parking_load`

def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    return (occupied_parking_spaces / total_parking_spaces) * 100 \
        if 0 <= occupied_parking_spaces <= total_parking_spaces else f'error'
