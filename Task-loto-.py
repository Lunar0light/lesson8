import sys
import random


def card(x):
    if x == 'player':
        print('------Ваша карточка------')
        for line1 in pl_field:
            for n1 in line1:
                print(f'{n1}', end=' ')       #числа в карточке не всегда располагаются ровно

            print()
        print('-------------------------')
    if x == 'comp':
        print('---Карточка компьютера---')
        for line2 in com_field:
            for n2 in line2:
                print(f'{n2}', end=' ')
            print()
        print('__________________________')


def player_step():
    cross = input('Зачеркнуть цифру? (y/n): ')
    if cross == 'y':
        if barrel in pl_num:
            for z in pl_field:
                try:
                    z.insert(z.index(barrel), '-')
                    z.pop(z.index(barrel))
                except ValueError:
                    continue
            return 1
        else:
            print('Player lost')
            sys.exit()
    if cross == 'n':
        if barrel in pl_num:
            print('Player lost')
            sys.exit()

def com_step():
    if barrel in com_num:
        for i in com_field:
            try:
                i.insert(i.index(barrel), '-')
                i.pop(i.index(barrel))
            except ValueError:
                continue
        return 1

total_barrels = 90
pl = 15
com = 15
barrels = random.sample(range(90), 90)
numbers = random.sample(range(90), 30)

pl_num = random.sample(numbers, 15)

com_num = [q for q in numbers if not q in pl_num]

pl_field = [pl_num[:5], pl_num[5:10], pl_num[10:]]
com_field = [com_num[:5], com_num[5:10], com_num[10:]]

for pline in pl_field:
    pline.sort()
    pline.insert(random.randint(0, 4), ' ')
    pline.insert(random.randint(0, 5), ' ')
    pline.insert(random.randint(0, 6), ' ')
    pline.insert(random.randint(0, 7), ' ')
for comline in com_field:
    comline.sort()
    comline.insert(random.randint(0, 4), ' ')
    comline.insert(random.randint(0, 5), ' ')
    comline.insert(random.randint(0, 6), ' ')
    comline.insert(random.randint(0, 7), ' ')


for barrel in barrels:
    total_barrels -= 1
    print(f'Бочонок номер: {barrel}\n (осталось: {total_barrels})\n')
    card('player')
    card('comp')
    if player_step() == 1:
        pl -= 1
    if com_step() == 1:
        com -= 1
    if pl == 0:
        print('Player win')
        sys.exit()
    if com == 0:
        print('Computer win')
        sys.exit()