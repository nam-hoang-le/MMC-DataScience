from .processFile import *
from .myPath import *
from IPython.display import clear_output


def create_account(username, password, total_money):
    user_info = f'{username},{password},{total_money}\n'
    write_file([user_info], PATH_DATA_ACCOUNT, 'a')
    print(f"Create account {username} successfully!")

def delete_account(username):
    lst_account = read_file(PATH_DATA_ACCOUNT, "r")
    for account in lst_account:
        if account[0] == username:
            lst_account.remove(account)
            write_file([','.join(account) + '\n' for account in lst_account], PATH_DATA_ACCOUNT, "w")
            print ("Delete account successfully!")


def check_admin(username):
    if username == "admin":
        return 1
    else:
        return 0 

def check_account(username, password):
    global login_status, user
    lst_account = read_file(PATH_DATA_ACCOUNT, "r")

    if lst_account is None:
        return False

    for account in lst_account:
        if account[0] == username and account[1] == password:
            return check_admin(username)
            
def check_account_exist(username):
    lst_account = read_file(PATH_DATA_ACCOUNT, "r")
    if lst_account is None:
        return False

    for account in lst_account:
        if account[0] == username:
            return True
    
    return False

def take_info_account(username):
    try:
        data_account = read_file(PATH_DATA_ACCOUNT, "r")
        if data_account:
            for account in data_account:
                if account[0] == username:
                    return account
        else:
            return None
    except Exception as e:
        print(f"There is problem happening: {e}")
        return None
    

def check_login(username, password):
    if check_account(username, password) in (0,1):
        return True
    else:
        return False

def change_password(username, old_password, new_password):
    lst_account = read_file(PATH_DATA_ACCOUNT, "r")
    
    for account in lst_account:
        if account[0] == username and account[1] == old_password:
            account[1] = new_password
            write_file([','.join(account) + '\n' for account in lst_account], PATH_DATA_ACCOUNT, "w")
            print("Change password successfully")
            return

    print("Can't find account or the old password isn't correct.")
    return

def insert_money(username, money):
    lst_account = read_file(PATH_DATA_ACCOUNT, "r")
    
    for account in lst_account:
        if account[0] == username:
            account[2] = str(int(account[2]) + money)
            write_file([','.join(account) + '\n' for account in lst_account], PATH_DATA_ACCOUNT, "w")
            print(f"Đã nạp {money} vào tài khoản {username}.")
            return

    print("Can't find the account!")
    return
