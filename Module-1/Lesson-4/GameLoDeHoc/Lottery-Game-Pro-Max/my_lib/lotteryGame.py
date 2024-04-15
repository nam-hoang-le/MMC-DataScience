import random
from .processAccount import *
from datetime import datetime

def shuffle_numbers():
    list_of_prizes = {}

    name_prizes = ["FIRST PRIZE", "SECOND PRIZE", "THIRD PRIZE", "FIFTH PRIZE", "SIXTH PRIZE", "SEVENTH PRIZE"]

    for prize in name_prizes:
        number = ""
        for i in range(5):
            number += str(random.randint(0, 9))  # Create a random number from 0 to 9
        list_of_prizes[prize] = number

    return list_of_prizes

def print_list_of_prizes(list_of_prizes):
    print('-' * 20)
    print("---LIST OF PRIZES---")
    for prize, number in list_of_prizes.items():
        print(f"{prize}: {number}")
    print('-' * 20)

def insert_lucky_number():
    while True:
        lucky_numbers = input("Inser the numbers you want to play, seperate by comma: ")
        list_of_lucky_numbers = lucky_numbers.split(",")

        legit_lucky_number = True

        for lucky_number in list_of_lucky_numbers:
            if len(lucky_number) != 2 or not lucky_number.isdigit():
                print("Invalid lucky number. Please insert again!")
                legit_lucky_number = False
                break

        if legit_lucky_number:
            return list_of_lucky_numbers

def enter_money_playing(username, number_of_lucky_numbers):
    total_money = int(take_info_account(username)[2])
    
    while True:
        money_playing = input("Insert amount of money you want to play (money playing < your total money): ")
        if money_playing.isdigit() and int(money_playing) * number_of_lucky_numbers < total_money:
            return int(money_playing)
        else:
            print("Wrong format or more than total money. Please insert again!")


def update_money_playing(username, total_money):
    try:
        data_account = read_file(PATH_DATA_ACCOUNT, "r")
        if data_account:
            for i, account in enumerate(data_account):
                if account[0] == username:
                    data_account[i][2] = str(total_money)  
                    write_file([','.join(account) + '\n' for account in data_account], PATH_DATA_ACCOUNT, "w")
                    return
    except Exception as e:
        print(f"There is problem in update account's information: {e}")


def save_info_playing_game(username, list_of_lucky_numbers, money_playing, list_of_prizes,  winning_money, losing_money):
    try:
        time_playing = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        thong_tin = f"{time_playing},{username},{','.join(list_of_lucky_numbers)},{money_playing}," \
                    f"{','.join(list_of_prizes.values())},{winning_money},{losing_money}\n"
        
        write_file(thong_tin, PATH_DATA_PLAYING_LOTTERY, "a")
        print("Info about this time was saved.")
        

    except Exception as e:
        print(f"There is problem in saving information: {e}")

def shuffle_game(username, list_of_lucky_numbers, money_playing):
    total_money = int(take_info_account(username)[2])

    list_of_prizes = shuffle_numbers()

    print_list_of_prizes(list_of_prizes)
    winning_count = 0
    winning_numbers = []  

    print("Number you've played:", list_of_lucky_numbers)
    for prize, number in list_of_prizes.items():
        for lucky_number in list_of_lucky_numbers:
            if lucky_number == number[-2:]:
                winning_count += 1
                winning_numbers.append(lucky_number)

    winning_money = 0  
    losing_money = 0   

    if winning_count > 0:
        winning_money = money_playing * winning_count * 70
        losing_money = money_playing * (len(list_of_lucky_numbers) - len(winning_numbers))

        total_money += winning_money - losing_money

        print(f"You've won {winning_count} times!")
        print("Winning numbers:", ", ".join(winning_numbers))
        print(f"Money you've won: {winning_money}")
        print(f"Money you've lost {losing_money}")
        print(f"Your total money: {total_money}")
    else:
        losing_money = money_playing * len(list_of_lucky_numbers)
        total_money -= losing_money

        print("You've lost!")
        print(f"Money you lost: {losing_money}")
        print(f"Your money left: {total_money}")

    save_info_playing_game(username, list_of_lucky_numbers, money_playing, list_of_prizes, winning_money, losing_money)
    update_money_playing(username, total_money)

