import random

def table(mx):
    for i in range(4):
        print(f'{(mx[i])[0]} {(mx[i])[1]} {(mx[i])[2]} {(mx[i])[3]}')

def win_check(mx):
    max_sum = 0
    sum_d1_u = 0
    sum_d1_c = 0
    sum_d2_u = 0
    sum_d2_c = 0
    for i in range(1, 4):
        sum_row_u = 0
        sum_row_c = 0
        sum_col_u = 0
        sum_col_c = 0
        for j in range (1, 4):
            if (mx[i])[j] == mark_u:
                sum_row_u += 1
            elif (mx[i])[j] == mark_c:
                sum_row_c += 1
            if (mx[j])[i] == mark_u:
                sum_col_u += 1
            elif (mx[j])[i] == mark_c:
                sum_col_c += 1
        if (mx[i])[i] == mark_u:
            sum_d1_u += 1
        if (mx[i])[i] == mark_c:
            sum_d1_c += 1
        if (mx[i])[-i] == mark_u:
            sum_d2_u += 1
        if (mx[i])[-i] == mark_c:
            sum_d2_c += 1
        max_sum = max(max_sum, sum_row_u, sum_row_c, sum_col_u, sum_col_c,
                      sum_d1_u, sum_d1_c, sum_d2_u, sum_d2_c)
    if max_sum == 3:
        return True

def comp_turn(mx, turns=9):
    free =[]
    if turns == 9:
        if chance >= random.randint(0, 100):
            (mx[1])[2] = mark_c
            turns -= 1
            return human_turn(mx, turns)
        else:
            (mx[2])[2] = mark_c
            turns -= 1
            return human_turn(mx, turns)
    elif turns == 8 and chance >= random.randint(0, 100) and (mx[2])[2] == mark_u:
        (mx[1])[2] = mark_c
        turns -= 1
        return human_turn(mx, turns)
    elif turns == 8 and (mx[2])[2] == mark_u:
        (mx[1])[1] = mark_c
        turns -=1
        return human_turn(mx, turns)
    elif turns == 7 and ((mx[1])[2] == mark_u
        or (mx[2])[1] == mark_u
        or (mx[2])[3] == mark_u
        or (mx[3])[2] == mark_u):
        if (mx[1])[1] == ' ':
            (mx[1])[1] = mark_c
            turns -= 1
            return human_turn(mx, turns)
        else:
            (mx[1])[3] = mark_c
            turns -= 1
            return human_turn((mx, turns))
    else:
        sum_d1 = 0
        sum_d2 = 0
        for i in range (1, 4):
            sum_row = 0
            sum_col = 0
            for j in range (1, 4):
                if (mx[i])[j] == mark_c:
                    sum_row += 1
                if (mx[i])[j] == mark_u:
                    sum_row -= 1
                if (mx[j])[i] == mark_c:
                    sum_col += 1
                if (mx[j])[i] == mark_u:
                    sum_col -=1
                if (mx[i])[j] == ' ':
                    free.append([i, j])
            if sum_row == 2:
                for j in range (1, 4):
                    if (mx[i])[j] == ' ':
                        (mx[i])[j] = mark_c
                        table(mx)
                        print('Компьютер выиграл')
                        return True
            if sum_col == 2:
                for j in range (1, 4):
                    if (mx[j])[i] == ' ':
                        (mx[j])[i] = mark_c
                        table(mx)
                        print('Компьютер выиграл')
                        return True
            if (mx[i])[i] == mark_c:
                sum_d1 += 1
            if (mx[i])[i] == mark_u:
                sum_d1 -= 1
            if (mx[i])[-i] == mark_c:
                sum_d2 += 1
            if (mx[i])[-i] == mark_u:
                sum_d2 -= 1
        if sum_d1 == 2:
            for i in range(1, 4):
                if (mx[i])[i] == ' ':
                    (mx[i])[i] = mark_c
                    table(mx)
                    print('Компьютер выиграл')
                    return True
        if sum_d2 == 2:
            for i in range(1, 4):
                if (mx[i])[-i] == ' ':
                    (mx[i])[-i] = mark_c
                    table(mx)
                    print('Компьютер выиграл')
                    return True
        sum_d1 = 0
        sum_d2 = 0
        for i in range(1, 4):
            sum_row = 0
            sum_col = 0
            for j in range(1, 4):
                if (mx[i])[j] == mark_u:
                    sum_row += 1
                if (mx[i])[j] == mark_c:
                    sum_row -= 1
                if (mx[j])[i] == mark_u:
                    sum_col += 1
                if (mx[j])[i] == mark_c:
                    sum_col -= 1
            if sum_row == 2:
                for j in range(1, 4):
                    if (mx[i])[j] == ' ':
                        (mx[i])[j] = mark_c
                        turns -=1
                        return human_turn(mx, turns)
            if sum_col == 2:
                for j in range(1, 4):
                    if (mx[j])[i] == ' ':
                        (mx[j])[i] = mark_c
                        turns -=1
                        return human_turn(mx, turns)
            if (mx[i])[i] == mark_u:
                sum_d1 += 1
            if (mx[i])[i] == mark_c:
                sum_d1 -= 1
            if (mx[i])[-i] == mark_u:
                sum_d2 += 1
            if (mx[i])[-i] == mark_c:
                sum_d2 -= 1
        if sum_d1 == 2:
            for i in range(1, 4):
                if (mx[i])[i] == ' ':
                    (mx[i])[i] = mark_c
                    turns -=1
                    return human_turn(mx, turns)
        if sum_d2 == 2:
            for i in range(1, 4):
                if (mx[i])[-i] == ' ':
                    (mx[i])[-i] = mark_c
                    turns -=1
                    return human_turn(mx, turns)
        if turns != 1:
            couple = free[random.randint(0, (len(free)-1))]
        else:
            couple = free[0]
        (mx[couple[0]])[couple[1]] = mark_c
        turns -= 1
        return human_turn(mx, turns)

def human_turn(mx, turns=9):
    table(mx)
    if turns == 0:
        print('Ничья')
        return True
    cor_turn = False
    while not cor_turn:
        row = input('В какую стоку ходим?')
        col = input('В какой столбик ходим?')
        if (row.isdigit()
            and col.isdigit()
            and (0 < int(row) < 4)
            and (0 < int(col) < 4)
            and (mx[int(row)])[int(col)] == ' '):
                cor_turn = True
                (mx[int(row)])[int(col)] = mark_u
        else:
            print('В эту ячейку нельзя ходить')
    table(mx)
    turns -= 1
    if win_check(mx):
        print('Пользователь выиграл')
        return True
    elif turns == 0:
        print('Ничья')
        return True
    else:
        return comp_turn(mx, turns)

game = True

while game:
    matrix = [[' ', '1', '2', '3'],
          ['1', ' ', ' ', ' '],
          ['2', ' ', ' ', ' '],
          ['3', ' ', ' ', ' ']]

    chance = 25
    first = input('Чей ход первый? u - пользователь, c - компьютер')
    first = first.lower()
    while 'u' != first != 'c':
        first = input('Нет такой буквы. Чей ход первый? u - пользователь, c - компьютер')
        first = first.lower()

    if first == 'u':
        mark_u = 'X'
        mark_c = 'O'
        human_turn(matrix)
    else:
        mark_u = 'O'
        mark_c = 'X'
        comp_turn(matrix)
    new_g = input('Сыграем ещё раз? y - да')
    new_g = new_g.lower()
    if new_g != 'y':
        game = False