

if __name__ == "__main__":
    import random

N, M = 5, 10

cinema_hall = [[random.choice([0, 1]) for _ in range(M)] for _ in range(N)]# 0 - свободно, 1 - это занято
                                                                             # при этом каждый раз порядок и количество занятых мест
                                                                            # в ряду разнится


def book_seats(cinema_hall, num_seats):
    for row in range(len(cinema_hall)):
        # Ищем подходящие места подряд
        for col in range(len(cinema_hall[row]) - num_seats + 1):
            if all(cinema_hall[row][col + i] == 0 for i in range(num_seats)):  # Проверка на свободные места
                # Бронируем места
                for i in range(num_seats):
                    cinema_hall[row][col + i] = 1
                return f"Места забронированы в ряду {row + 1}, с {col + 1} по {col + num_seats}"
    return "Нет свободных мест"



result = book_seats(cinema_hall, 3)
print(result)
