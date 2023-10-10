try:
    import os
    import sys
    from faker import Faker
    import socket
    import services
    from services import api_key_num
    import textrm
    from textrm import short_cybersec
    import threading
    import requests
    import datetime
    from colorama import init, Fore, Style
    import time
except:
    print(' Произошла ошибка при импорте библиотек\n Попробуйте установить их по команде:\n pip3 install faker requests colorama')

import services
from services import api_key_num
import textrm
from textrm import short_cybersec

init()

# Определение цветов
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN

yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT



def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def oshibka():
    input(f"{red}Произошла ошибка.\n{yellow}Enter{reset} - для возврата в меню  ")
    menu()
def about():
    about_text = f"""

       {reset}{bold}   Над проектом работали:{reset}
              {green}.:{yellow} Luka  {green}:.
              {green}::{yellow}Rimmase{green}::
              {green}::{cyan}ProxitQ{green}::
              {green}::{cyan}Soci3ty{green}::
        
        {reset} {bold}   Социальные сети:   {reset}
   {bold}{yellow}GitHub{reset}:{cyan} https://github.com/TheCyberStalker/RimmaPy
   {bold}{yellow}Telegram{reset}:{cyan} telegram.dog/CyberStalker1337
   {bold}{yellow}Telegram{reset}:{cyan} telegram.dog/pr0xit
   
   {bold}{yellow}EMail для ваших вопросов и решения ошибок!
   {reset}{bold}{cyan}      Cyb3rSt4lk3r@proton.me 
   
   {bold}{yellow}Лицензия:{reset}{bold}{cyan}[GNU v3.0]               
   {reset}

  Данный проект, служит отличным примером того, 
  насколько простым может быть сбор информации 
  через открытые API сторонних сервисов. 
  
  Важно подчеркнуть, что наш проект не несет ответственности
  за действия пользователей при его использовании.
  
  Мы создали "RimmaPy" с целью показать, как можно
  эффективно использовать открытые API для сбора данных.
  
  Тем не менее, мы настоятельно рекомендуем всем пользователям
  соблюдать правила анонимности и правила связанные с сбором данных.
  
  Наш проект призван подчеркнуть важность соблюдения этических норм
  и нормативных требований при работе с данными из открытых источников.
  
  Мы надеемся, что "RimmaPy" будет полезным инструментом для вас, и поможет
  вам легко и безопасно получать доступ к данным через открытые API.
  
        Спасибо за использование нашего проекта!
 Не забывайте соблюдать правила и законы анонимности в сети.{reset}     
    """

    os.system('cls' if os.name == 'nt' else 'clear')

    for line in about_text.split('\n'):
        print(line)
        time.sleep(0.1)

def logo():
    logo_text = f"""
{bold}{green}    Welcome to RimmaPy
{yellow}    {name}!{reset}

        {green}.:{yellow} Luka  {green}:.
        {green}::{yellow}Rimmase{green}::
        {green}::{cyan}ProxitQ{green}::
        {green}::{cyan}Soci3ty{green}::            
    
   {bold}{yellow}GitHub{reset}:{cyan} https://github.com/TheCyberStalker
   {bold}{yellow}Telegram{reset}:{cyan} telegram.dog/CyberStalker1337
   {bold}{yellow}Telegram{reset}:{cyan} telegram.dog/pr0xit

                     
"""

    os.system('cls' if os.name == 'nt' else 'clear')

    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.2)


# Определение функции для вывода информации о студенте
def print_student_info(row):
    clear_terminal()
    print(red + f"""
          
    ██████╗ ██╗███╗   ███╗███╗   ███╗ █████╗ 
    ██╔══██╗██║████╗ ████║████╗ ████║██╔══██╗
    ██████╔╝██║██╔████╔██║██╔████╔██║███████║
    ██╔══██╗██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║
    ██║  ██║██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║
    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
""" + reset)
    print(cyan + "-"*100 + reset)
    print("Email:", row['Электронная почта'])
    print("Телефон:", row['Телефон'])
    print("Дата рождения:", row['Дата рождения'])
    print("Адрес:", row['Адрес'])
    print("Гражданство:", row['Гражданство'])
    print("Школа:", row['Наименование учреждения'])
    print("Класс:", row['Класс'])
    print("Регион:", row['Регион'])
    print("Страна:", row['Страна обучения'])
    print("Пол:", row['Пол'])
    print("Статус:", row['Роль'])
    print("Фамилия:", row['Фамилия'])
    print("Имя:", row['Имя'])
    print("Отчество:", row['Отчество'])
    print(cyan + "-"*100 + reset)

# Определение функции для поиска студента
##   last_name_mask = data['Фамилия'] == last_name
#
 #   if first_name:
  #      first_name_mask = data['Имя'] == first_name
   #     last_name_mask = last_name_mask & first_name_mask

    #if middle_name:
     #   middle_name_mask = data['Отчество'] == middle_name
      #  last_name_mask = last_name_mask & middle_name_mask

    #filtered_data = data[last_name_mask]

    #return filtered_data

# Определение функции для MAC adress
def get_vendor_by_mac():
        mac_address = input(Fore.YELLOW + "Введите MAC-адрес для определения производителя: ")
        url = f"https://api.macvendors.com/{mac_address}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.text.startswith("No vendor"):
                print(Fore.RED + "Не удалось определить производителя.")
            else:
                print(Fore.GREEN + response.text)
        except requests.RequestException as e:
            print(Fore.RED + f"Ошибка при запросе: {e}")

        input(f"{yellow}Enter{reset} - {green}чтобы вернуться в главное меню ")

# Определение функции для проверки номера телефона через API NumVerify
def NumVerify(api_key_num):
    clear_terminal()
    user_input = input(f"   Номер должен быть без '+' и пробелов\n    {bold}{yellow}Введите номер ➤")

    url = f"http://apilayer.net/api/validate?access_key={api_key_num}&number={user_input}&country_code=&format=1"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            phone_number_info = response.json()

            if 'error' in phone_number_info:
                print(f"Ошибка: {phone_number_info['error']['info']}")
            else:
                print(f"{red}Телефонный номер:{bold}{red} {phone_number_info['number']}")
                print(f"{yellow}Валидность:{bold}{red} {phone_number_info['valid']}")
                print(f"{yellow}Код страны:{bold}{red} {phone_number_info['country_code']}")
                print(f"{yellow}Страна:{bold}{red} {phone_number_info['country_name']}")
                print(f"{yellow}Возможная локация:{bold}{red} {phone_number_info['location']}")
                print(f"{yellow}Оператор:{bold}{red} {phone_number_info['carrier']}")
        else:
            print(f"Ошибка при выполнении запроса. Код состояния HTTP: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

# Определение функции для сканирования портов в одной функции
def scan_ports_in_one_function():
    def scan_port(target_host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"{Fore.RED}Порт{Fore.WHITE} {port} открыт{Style.RESET_ALL}")
            sock.close()
        except Exception as e:
            pass

    target_host = input(f"   {red}Введите IP/hostname ➤  ")

    # Создаем список потоков
    threads = []

    # Сканируем порты от 1 до 1025
    for port in range(1, 1026):
        # Создаем поток для сканирования порта
        thread = threading.Thread(target=scan_port, args=(target_host, port))
        # Добавляем поток в список
        threads.append(thread)
        # Запускаем поток
        thread.start()

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    yn = input(f"{Fore.GREEN}{Style.BRIGHT}Вернуться в меню? Y/n: {Style.RESET_ALL}")
    if yn == "n":
        sys.exit()

def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    return response.json()

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(red + f"""
              
              
    ██████╗ ██╗███╗   ███╗███╗   ███╗ █████╗ 
    ██╔══██╗██║████╗ ████║████╗ ████║██╔══██╗
    ██████╔╝██║██╔████╔██║██╔████╔██║███████║
    ██╔══██╗██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║
    ██║  ██║██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║
    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
      {yellow}  user: {bold}{cyan}.:{name}:.{reset}
      {yellow}Telegram{reset}:{bold}{cyan} t.me/CyberStalker1337{reset}
      {yellow}Совет ➤ {cyan}{textrm.short_cybersec()}                     
""" + reset)
        print(f"""
    {red}+{'-'*34}+{reset}
    | {yellow}1{reset} - {bold}{green}Поиск по IP            {reset}      |
    | {yellow}2{reset} - {bold}{green}Поиск открытых портов{reset}        |
    | {yellow}3{reset} - {bold}{green}Поиск по номеру{reset}              |
    | {yellow}4{reset} - {bold}{green}Поиск по токену телеграм{reset}     |
    | {yellow}5{reset} - {bold}{green}Поиск по ФИО (need DataBase){reset} |
    | {yellow}6{reset} - {bold}{green}Поиск по MAC {reset}                |
    | {yellow}7{reset} - {bold}{green}Генерация данных (FakeDox){reset}   |
    | {yellow}8{reset} - {bold}{green}Fix меню{reset}                     |
    | {yellow}9{reset} - {bold}{green}О проекте/создателях{reset}         |
    | {yellow}0{reset} - {bold}{green}выход{reset}                        |
    {red}+{'-'*34}+{reset}
""")    
        home_page = int(input(f'\n     {cyan} {bold}{green}RimmaPy{reset} ➤{yellow} '))
        if home_page == 6:
            get_vendor_by_mac()
            # в следующих обновлениях выгрузим апи с базами и подробным геолокатором для софта
            time.sleep(1)
            menu()
        if home_page == 7:
            clear_terminal()
            fake = Faker('ru_RU')
            sex = Faker().random_element(elements=('male', 'female'))
            print(f'''

{yellow}
        ██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
        ██╔══██╗██╔═══██╗╚██╗██╔╝██╔════╝██╔══██╗
        ██║  ██║██║   ██║ ╚███╔╝ █████╗  ██████╔╝
        ██║  ██║██║   ██║ ██╔██╗ ██╔══╝  ██╔══██╗
        ██████╔╝╚██████╔╝██╔╝ ██╗███████╗██║  ██║
        ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                    TOOL-KIT BY {red}.:{name}:.      {reset}                           

                  ''')
            print(" Пол:", "Мужской" if sex == f"{Fore.BLUE}male" else f"{Fore.LIGHTMAGENTA_EX}Женский{reset}")
            print(" Имя:", fake.first_name_male() if sex == "male" else fake.first_name_female())
            print(" Фамилия:", fake.last_name_male() if sex == "male" else fake.last_name_female())
            print(" Отчество:", fake.middle_name_male() if sex == "male" else fake.middle_name_female())
            print(" Email:", fake.email())
            print(" Телефон:", fake.phone_number())
            print(" Адрес:", fake.address())
            print(" Город:", fake.city())
    
            input('\n  Enter - для возврата в меню')
            menu()

        if home_page == 9:
            clear_terminal()
            about()
            input('\n  Enter - для возврата в меню')
            menu()
        if home_page == 8:
            clear_terminal()
            menu()

        elif home_page == 0:
            clear_terminal()
            print(f"\n\n     {blue}Вы вышли из скрипта\n    Для запуска:\n    {yellow} python3 rimma.py")
            sys.exit()

        elif home_page == 1:
            clear_terminal()
            ip_address = input(f"\n      {yellow}/[-_•]\ Введите IP -{red}  ")
            try:
                url = f"https://ipinfo.io/{ip_address}/json"
                response = requests.get(url)
                data = response.json()
                clear_terminal()
                print(bold + red + """
      .---------.
      | IP INFO |
      '---------'
""" + reset)
                print(f"   {green} IP Адрес: {cyan}{data.get('ip', red + 'Н/Д')}")
                print(f"   {green} Город:{cyan} {data.get('city', red + 'Н/Д')}")
                print(f"   {green} Регион:{cyan} {data.get('region', red + 'Н/Д')}")
                print(f"    {green}Страна: {cyan}{data.get('country', red + 'Н/Д')}")
                print(f"    {green}Локация:{cyan} {data.get('loc', red + 'Н/Д')}")
                print(f"    {green}Провайдер: {cyan}{data.get('org', red + 'Н/Д')}")
                print(f"    {green}Домен:{cyan} {data.get('hostname', red + 'Н/Д')}")
                print(f"\n{cyan}    Результат: {reset}Н/Д это Нет Данных{reset}")
                input(f"    {yellow}Enter{reset} - {green}чтобы вернуться в главное меню ")
                clear_terminal()
                menu()
            except:
                oshibka()

        elif home_page == 2:
            clear_terminal()
            scan_ports_in_one_function()
            clear_terminal()
            menu()
        
        elif home_page == 3:
            services.api_key_num = api_key_num
            NumVerify(services.api_key_num)

            yn = input(f"{green}{bold}    Вернуться в меню? Y/n :")
            if yn.lower() == "y":
                menu()
            if yn.lower() == "n":
                sys.exit()

        elif home_page == 5:
            clear_terminal()
            print(f'В данной версии скрипта на данный момент\n не содержится возможность \nустановки DB p-1 p-5 для поиска по фио.')
##########################
    #        if all_data is None:
     #           loading_message = "Ожидайте, загружаются базы данных"
#
 #               def animate_loading():
  #                     for symbol in symbols:
    #                        clear_terminal()
     #                       print(f"{loading_message} {symbol}", end="\r")
      #                      time.sleep(0.2)
#
 #            loading_thread = threading.Thread(target=animate_loading)
   #             loading_thread.start()
#
 #               # Загружаем данные из всех CSV файлов
  #              input_files = ["part1.csv", "part2.csv", "part3.csv", "part4.csv", "part5.csv", "part6.csv"]
   #             data_frames = []
#              for file in input_files:
  #                  data = pd.read_csv(file, delimiter=';', encoding='utf-8')

   #                 data['Телефон'] = data['Телефон'].apply(convert_phone_number)

    #                data_frames.append(data)
##########################

            yn = input(f"{green}    Вернуться в меню? Y/n: {reset}")
            if yn == "n":
                sys.exit()

        elif home_page == 4:
            clear_terminal()
            token = input(f"  {yellow}  ⟨^-^⟩ Введите токен тг бота -{red} ")
            clear_terminal()
            try:
                bot_data = get_bot_info(token)
                if bot_data.get("ok"):
                    data = bot_data["result"]
                    print(f"    Айди: {data['id']}")
                    print(f"    Имя: {data['first_name']}")
                if 'username' in data:
                    print(f"    Юзернейм: @{data['username']}")
                if 'can_join_groups' in data:
                    print(f"    Вступление в группы: {data['can_join_groups']}")
                    input(f"\n     {yellow}Enter{reset} - {green}для входа в меню")
                    menu()
            except:
                oshibka()
        else:
            print(red + 'Введите существующий пункт меню!' + reset)
            time.sleep(1)
            continue

if __name__ == '__main__':
    with open("us3r.txt", "r") as file:
        name = file.read()
    logo()
    menu()