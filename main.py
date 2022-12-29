import shutil
import os
import schedule

all_computer = ['\\\DIREKKTOR-PC\\архив', '\\\karpova-ai\\Архив',\
                '\\\kondakova\\архив','\\\Karpova\архив',\
                '\\\Help\архив','\\\KANISHCHEVA\\архив','\\\KOBRANITSKAJA\\архив',\
                '\\\LUBETSKAYA1\\архив', '\\\MITJAEVA\\архив','\\\SAFRONOVA\\архив',\
                '\\\SELEZNEVA\\архив','\\\GAVRILOVA\\архив','\\\DESKTOP-H405I1B\архив'] #имена всех компьютеров
def copy_files_from_base():
    if os.path.exists("\\\glavhran\\c$\\Архив\\Архив.mdb") == True:
        shutil.copy("\\\glavhran\\c$\\Архив\\Архив.mdb", r"C:\\архив")
        shutil.copy("\\\glavhran\\c$\\Архив\\Архив_база.mdb", r"C:\\архив")
        print('Резервное копирование выполнено!')                               #резервная копия
    else:
        return 'Компьютер Кан не доступен, резервное копирование невозможно'

def copy(computer):
    if os.path.exists("{}".format(computer)) == True:
        shutil.copy("C:\\архив\\Архив.mdb", "{}".format(computer))
        shutil.copy("C:\\архив\\Архив_база.mdb", "{}".format(computer))
        return f'{computer[2:-6]} --- успешно'
    else:
        return f'Компьютер {computer[2:-6]} --- недоступен'                 #копирование на пк пользователей

def copy_all_users():
    for computer in all_computer:
        result = copy(computer)
        print(result)                    #проблегаемся по списку компьютеров
def timer():
    schedule.every().day.at('15:23').do(copy_files_from_base)
    schedule.every().day.at('15:23').do(copy_all_users)
    while True:
        schedule.run_pending()                #таймер

timer()





