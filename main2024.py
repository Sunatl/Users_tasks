from main1 import *
from main import *
while True:
    task = input("\nTasks\nUsers\nExit\n\nMa'lumotro vorid kuned: ")
    if task == 'Tasks':
        while True:
            b = input("Register\nGet_users\nlogin\nChange_password\nDelete\nExit\n\nMa'lumotro vorid kuned: ")
            if b == 'Register':
                register()
            elif b == 'Get_users':
                print(get_users())
            elif b == 'login':
                login()
            elif b == 'Change_password':
                change_password()
            elif b == 'Delete':
                delete()
            elif b == 'Exit':
                exit
    elif task == 'Users':
        while True:
            a = input("Add\nGet\nGet_by_id\ndelete\nUpdate\nExit\n\nMa'lumotro vorid kuned: ")
            if a == 'Add':
                add()
            elif a == 'Get':
                get()
            elif a == 'Get_by_id':
                get_by_id()
            elif a == 'Delete':
                delete()
            elif a == 'Update':
                update()
            elif a == 'Exit':
                exit
            else:
                print("rakami nodurust")
    elif task == 'Exit':
        exit
    else:
        print("Ma'lumoti nodurust!")
    