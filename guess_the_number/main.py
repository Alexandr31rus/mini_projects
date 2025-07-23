import random

random_number = random.randint(1, 100)
count = 0

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False

print('Добро пожаловать в числовую угадайку')
while True:
    user_number = input("Введите целое число от 1 до 100: ")

    if not is_valid(user_number):
        print("Введите целое число!\n")
        continue
    user_number = int(user_number)
    if random_number < user_number:
        print()
        print('Слишком много, попробуйте еще раз')
    elif random_number > user_number:
        print()
        print("Слишком мало, попробуйте еще раз")
    else:
        print()
        print(f"Вы угадали за {count} ходов, поздравляем!")
        break
    count += 1
print('Спасибо, что играли в числовую угадайку.')
