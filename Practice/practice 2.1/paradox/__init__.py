def birthday(iterations, people=23):
    import random

    count = 0

    for i in range(iterations):
        bdays = []
        for i in range(people):
            bdays.append(random.randint(1, 336))
        for i in bdays:
            if bdays.count(i) > 1:
                count += 1
                break
    return count / iterations * 100


def monty_hall(iterations):
    import random

    doors = [0, 1, 0]
    win_cnt_agree = 0
    win_cnt_pursue = 0

    for i in range(iterations):
        first = random.choice(doors)
        if first == 1:
            win_cnt_pursue += 1  # если дверь выигрышная и настаиваем на своём выборе
        else:
            win_cnt_agree += 1  # если дверь проигрышная и соглашаемся поменять дверь
    return f"Вероятность выигрыша при смене двери: {win_cnt_agree / iterations * 100:.2f}%\nВероятность выигрыша без смены двери: {win_cnt_pursue / iterations * 100:.2f}%"