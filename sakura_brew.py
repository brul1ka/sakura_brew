import msvcrt
import os
from random import randint
from time import sleep
from colorama import Fore, init
import pyfiglet

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    clear_screen()
    print(f"{Fore.CYAN}{pyfiglet.figlet_format('SakuraBrew')}{Fore.RESET}")
    print(f"{Fore.YELLOW}1. Начать игру")
    print(f"2. Настройки")
    print(f"3. Выход\n{Fore.RESET}")

    choice = input(f"{Fore.GREEN}Выберите опцию: {Fore.RESET}")

    if choice == "1":
        return True
    elif choice == "2":
        settings_menu()
    elif choice == "3":
        exit(0)
    else:
        print(f"{Fore.RED}Неверный выбор! Попробуйте снова.{Fore.RESET}")
        input("Нажмите Enter, чтобы продолжить...")
        return False


def settings_menu():
    clear_screen()
    print(f"{Fore.YELLOW}Настройки{Fore.RESET}")
    print(f"1. Выход\n{Fore.RESET}")

    choice = input(f"{Fore.GREEN}Выберите опцию: {Fore.RESET}")

    if choice == "1":
        return False
    else:
        print(f"{Fore.RED}Неверный выбор! Попробуйте снова.{Fore.RESET}")
        input("Нажмите Enter, чтобы продолжить...")


clear_screen()
print(
    f"Добро пожаловать в \n{pyfiglet.figlet_format('SakuraBrew')}Нажмите любую клавишу для предыстории игры."
)
msvcrt.getch()

clear_screen()
print(
    f"{Fore.YELLOW}Расположенная в тихом уголке города, Sakura Brew — это больше, чем просто кофейня — это святилище. "
    f"Основанное путешественником, влюбившимся в культуру японских кафе, это уютное место сочетает тепло "
    f"традиционного японского гостеприимства с насыщенными ароматами фирменного кофе.{Fore.RESET}\n"
    "Нажмите любую клавишу..."
)
msvcrt.getch()

DAY = 1
BALANCE = 100
COFFEE_BEANS = 500
COFFEE_PRICE = 0
CONSUMPTION_OF_BEANS_PER_ONE_GLASS_OF_COFFEE = 10

while not main_menu():
    pass

while True:
    clear_screen()
    if DAY == 1:
        print(
            'В начале каждого дня будет какой-то "ивент", обозначен голубым цветом на главном экране дня. Сможете ли продавать кофе 10 дней подряд и не обанкротиться? Давайте же проверим!\n'
        )
    if DAY == 10:
        print(f"10 дней прошло! Ваш итоговый баланс: ${BALANCE}")
        sleep(5)
        exit(1)
    if COFFEE_BEANS == 0:
        print("Вы проиграли! У Вас кончились зёрна")
        exit(1)
    if COFFEE_BEANS <= 200:
        COFFEE_BEANS = f"{Fore.RED}{COFFEE_BEANS}{Fore.RESET}"

    BEANS_PRICE_100G = randint(5, 15)
    FANUM_TAX = int(max(10, BALANCE * 0.4))

    VISITORS_AMOUNT = max(2, randint(15 - COFFEE_PRICE * 2, 30 - COFFEE_PRICE * 3))
    event = randint(1, 5)
    if event == 1:
        print(
            f"{Fore.LIGHTBLUE_EX}В городе кофейный фестиваль! Вдвое больше клиентов сегодня!"
        )
        VISITORS_AMOUNT *= 2
    elif event == 2:
        print(
            f"{Fore.LIGHTBLUE_EX}Плохая погода. Людей сегодня будет в два раза меньше."
        )
        VISITORS_AMOUNT //= 2
    elif event == 3:
        print(
            f"{Fore.LIGHTBLUE_EX}Повышение налогов! Сегодня налог увеличен в 1.5 раза."
        )
        FANUM_TAX = int(FANUM_TAX * 1.5)
    elif event == 4:
        print(f"{Fore.LIGHTBLUE_EX}Акция! Цена зерна снижена на 30% сегодня.")
        BEANS_PRICE_100G = int(BEANS_PRICE_100G * 0.7)
    elif event == 5:
        print(f"{Fore.LIGHTBLUE_EX}Поломка кофемашины! Вы теряете $20 на ремонт.")
        BALANCE -= 20

    print(
        f"День {DAY}. У вас ${BALANCE} и {COFFEE_BEANS} грамм зерна. Вам также в конце дня надо будет заплатить {Fore.LIGHTMAGENTA_EX}FANUM TAXES{Fore.RESET} в размере ${FANUM_TAX}. На каждую чашку кофе расходуется {CONSUMPTION_OF_BEANS_PER_ONE_GLASS_OF_COFFEE}г зёрен."
    )
    day1 = input("Хотите ли подкупить немного зерна? (y/n) ")

    if day1.lower() == "y":
        while True:
            clear_screen()
            print(
                f"Сегодня 100 грамм зёрен стоит {Fore.CYAN}${BEANS_PRICE_100G}{Fore.RESET} (1 грамм - {Fore.CYAN}{BEANS_PRICE_100G / 100}¢{Fore.RESET})"
            )
            beans_buy_amount = input(
                'Сколько грамм хотите купить? (Для отмены напишите "c"): '
            )

            if beans_buy_amount.lower() == "c":
                break

            try:
                beans_buy_amount = int(beans_buy_amount)
                total_cost = (beans_buy_amount / 100) * BEANS_PRICE_100G

                if total_cost > BALANCE:
                    print("У вас недостаточно денег!")
                else:
                    BALANCE -= total_cost
                    COFFEE_BEANS += beans_buy_amount
                    print(f"Вы купили {beans_buy_amount} грамм зёрен за ${total_cost}.")
                input("Нажмите Enter, чтобы продолжить...")
                break

            except ValueError:
                print('Ошибка! Введите ЧИСЛО или "cancel".')
                input("Нажмите Enter, чтобы попробовать снова...")

    clear_screen()
    while True:
        try:
            coffee_price_input = input(
                "Цена чашки кофе? (в целых долларах и не больше пяти): "
            )

            coffee_price = int(coffee_price_input)

            if coffee_price > 5:
                print(
                    'Бро, сказали же: "до ПЯТИ". Не будь слишком наглым, пожалуйста.\n'
                )
            elif coffee_price <= 0:
                print(
                    f"Бесплатно? Нет. Ты, конечно, прости, но за такую щедрость тебя {Fore.RED}уволят.\n"
                )
            else:
                COFFEE_PRICE = coffee_price
                print(f"\nХорошо! Цена установлена на ${COFFEE_PRICE}.")
                break
        except ValueError:
            print("Ошибка! Введите число БЕЗ плавающей точки.")

    clear_screen()
    sleep(1)
    print(f"...Прошло 9 часов...\n")
    sleep(1)

    coffee_sold = min(
        VISITORS_AMOUNT, COFFEE_BEANS // CONSUMPTION_OF_BEANS_PER_ONE_GLASS_OF_COFFEE
    )
    revenue = round(coffee_sold * COFFEE_PRICE, 2)
    BALANCE += revenue - FANUM_TAX
    COFFEE_BEANS -= coffee_sold * CONSUMPTION_OF_BEANS_PER_ONE_GLASS_OF_COFFEE

    print(
        f"Ну что же, день подошёл к концу. Сегодня пришло {VISITORS_AMOUNT} посетителей."
    )
    print(
        f"Вы продали {coffee_sold} чашек кофе по ${COFFEE_PRICE} и заработали ${revenue}."
    )
    print(f"После уплаты налогов у вас осталось ${BALANCE}.")

    DAY += 1
    input("Нажмите Enter, чтобы продолжить...")
