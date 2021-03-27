import random

def decide_square_number():
    #square_listは使う数字を順に羅列したリスト+最後に空欄を配置、square_list_numberは、そのリストをランダムに配置したもの
    global square_number, square_list, square_list_number
    print('数字パズルを始めます。')
    square_number = input('何行にしますか？(4行以上)')
    while not enable_choice_square_number(square_number):
            square_number = input('何行にしますか？(4行以上)')
    square_number = int(square_number)
    square_list = list(range(1, square_number * square_number, 1))
    square_list.append('  ')
    square_list = list(map(str, square_list))
    square_list_number = random.sample(square_list, square_number * square_number)
    print('数字を左上から1~' + str(square_number * square_number - 1) + 'の順に並べて下さい。')

def show_square():
    rows = []
    for n in range(square_number):
        rows.append('|')

    for i in range(square_number):
        for j in range(square_number * i, (square_number * (i + 1))):
            rows[i] += square_list_number[j]
            if len(square_list_number[j]) == 1:
                rows[i] += ' '
            rows[i] += '|'

    line = '-'
    line += '---' * square_number
    print(line)
    for row in rows:
        print(row + '\n' + line)

def choice_box():
    #xで空欄部のインデックスナンバーを取得
    x = square_list_number.index('  ')
    show_square()    
    number = input('動かすマスを選んで下さい。(1~' + str(square_number * square_number - 1) + ')')
    while not enable_choice_box(number):

        print('\n1~' + str(square_number  * square_number - 1) + 'の間で選んで下さい。')
        show_square()
        number = input('動かすマスを選んで下さい。(1~' + str(square_number * square_number - 1) + ')')
    #yで入力した数字のインデックスナンバーを取得
    y = change_index(number)
    #xの場所をインデックス番号に変換
    if enable_move_x(x, y):
        square_list_number[x], square_list_number[y] = square_list_number[y], square_list_number[x]
    else: 
        print('\nそのマスは選べません。別のマスを選んでください。')

#行数制限のためのバリデーション
def enable_choice_square_number(string):
    if string.isdigit():
        number = int(string)
        if number < 4:
            return False
        else:
            return True
    else:
        return False

#選ぶマスのバリデーション
def enable_choice_box(string):
    if string.isdigit():
        number = int(string)
        if number >= 1 and number <= square_number * square_number - 1:
            return True
        else:
            return False
    else:
        return False

#入力した数字をリストのインデックス番号に変換する
def change_index(number):
    index_number = square_list_number.index(number)
    return index_number

def enable_move_x(x, y):
    #'X'が4隅の場合
    if x == 0 or x == (square_number - 1) or x == (square_number * (square_number - 1)) or x == ((square_number * square_number)) - 1:
        #選んだ場所が左上の場合
        if x == 0:
            if y == 1 or y == square_number:
                return True
            else:
                return False
        #選んだ先が右上の場合
        elif x == (square_number - 1):
            if y == (square_number - 2) or y == ((square_number * 2) - 1):
                return True
            else:
                return False
        #選んだ場所が左下の場合
        elif x == square_number * (square_number - 1):
            if y == square_number * (square_number - 2) or y == square_number * (square_number - 1) + 1:
                return True
            else:
                return False
        #選んだ場所が右下の場合
        elif x == square_number - 1:
            if y == square_number * (square_number - 1) - 1 or y == square_number * square_number - 2:
                return True
            else:
                return False
    else:
        #'X'が左端の場合
        if x % square_number == 0:
            if y == x + 1 or y == x + square_number or y == x - square_number:
                return True
            else:
                return False
        #'X'が右端の場合
        elif x % square_number == (square_number - 1):
            if y == x - 1 or y == x + square_number or y == x - square_number:
                return True
            else:
                return False
        #'X'が上端の場合               
        elif x // square_number == 0:
            if y == x + square_number or y == x + 1 or y == x - 1:
                return True
            else:
                return False
        #'X'が下端の場合
        elif (x / square_number) == (square_number - 1):
            if y == (x - square_number) or y == x + 1 or y == x - 1:
                return True
            else:
                return False
        #その他
        else:
            if y == x + 1 or y == x - 1 or y == (x + square_number) or y == (x - square_number):
                return True
            else:
                return False
 #完成か判定
def finish():
    if square_list_number == square_list:
        return True
    else:
        return False

def play():
    decide_square_number()
    choice_box()
    while not finish():
        choice_box()
    else:
        print('完成！！')

play()