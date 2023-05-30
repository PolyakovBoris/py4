# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
#  банкомат.

user_balance = 0
check_sum = 50
reach_payments = 5_000_000
log = dict()

def put_money(user_balance):
    """ Функция увеличивает user_balance на сумму user_input и вызывает функцию logging для сохранения операции в логе"""
    print('введите сумму пополнения')
    while True:
        user_input = input()
        if float(user_input) > 0:
            user_balance = user_balance + float(user_input)
            logging(f'+{user_input}')
            return user_balance        


def get_money(user_balance):
    """ Функция уменьшает user_balance на сумму user_input и вызывает функцию logging для сохранения операции в логе"""
    print('введите сумму снятия ')
    while True:
        user_input = input()
        if float(user_input) > 0 and float(user_input) < user_balance:           
            user_balance = user_balance - float(user_input)
            logging(f'-{user_input}')
            return user_balance  

def logging(num: float):
    """ Функция записывает операции пользователей в словарь с последовательной нумерацией и суммой денег"""
    next_num_in_dict = len(log) + 1
    log[next_num_in_dict] = num

def main_menu(user_balance: float):
    """ Главное меню """
    while True:
        print(log)
        print('1 - пополнить, 2 - снять, 3 - выйти')
        user_input = input()
        match int(user_input):
            case 1:
                user_balance = put_money(user_balance)
            case 2:
                user_balance = get_money(user_balance)
            case 3:
                break

main_menu(user_balance)