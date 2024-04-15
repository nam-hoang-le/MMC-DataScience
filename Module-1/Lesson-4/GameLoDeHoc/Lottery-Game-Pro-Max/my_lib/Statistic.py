from .processFile import *
from .myPath import *

def statistic_user(username):
    try:
        data_playing = write_file(PATH_DATA_PLAYING_LOTTERY, "r")
        number_playing = 0
        total_winning = 0
        total_losing = 0
        number_winning = 0
        number_losing = 0

        for playing in data_playing:
            if playing[1] == username:
                number_playing += 1
                total_winning += int(playing[-2])
                total_losing += int(playing[-1])
                if int(playing[-2]) >  0:
                    number_winning += 1
                else:
                    number_losing += 1
        ratio_winning = round(number_winning / number_losing, 2) if number_losing > 0 else 0

        # In kết quả
        print("===STATISTICS USER: "+ username+"===")
        print("Number playing:", number_playing)
        print("Total winning money:", total_winning)
        print("Total losing money:", total_losing)
        print("Ration of winning game:", ratio_winning)

    except Exception as e:
        print(f"There is problem while executing statistic: {e}")


def statistics_admin():
    try:
        data_playing = read_file(PATH_DATA_PLAYING_LOTTERY, "r")
        number_account = len(read_file(PATH_DATA_ACCOUNT, "r"))
        number_playing = len(data_playing)
        total_winning = sum(int(playing[-2]) for playing in data_playing)
        total_losing = sum(int(playing[-1]) for playing in data_playing)
        times_winning = sum(1 for playing in data_playing if int(playing[-2]) > 0)
        times_losing = number_playing - times_winning

        ratio_win_lose = round(times_winning / times_losing, 2) if times_losing > 0 else 0

        print("===OVERALL STATISTIC===")
        print("Number of accounts:", number_account)
        print("Times playing game:", number_playing)
        print("Total money winning:", total_winning)
        print("Total money losing:", total_losing)
        print("Ratio winning/losing:", ratio_win_lose)

    except Exception as e:
        print(f"There is problem in executing overall statistic: {e}")
