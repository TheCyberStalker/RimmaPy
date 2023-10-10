import os
import sys
import time
def profile_make():
    name = input("\n    Как вас называть?\n    >> ")
    with open("us3r.txt", "w") as file:
        file.write(name)
        print(f"""
    
    Приветствую вас {name}!\n
    
    Данный файл является установщиком:
    • дополнительных модулей
    • создания персонального профиля.
                
    """)
        time.sleep(1)
def installanswer():
        answer = input(    "Вы согласны на авто-установку модулей? (y/n): ").lower()
        if answer == 'y':
            clear_terminal()
        elif answer == 'n':
            clear_terminal()
            print("  Хорошо, если понадоблюсь\nИспользуйте: python3 rms.py")
            sys.exit()
        else:
            print("   Отвечайте только Yes и No, используя сокращение Y/n")
            installanswer()

def install_libraries():
    print("\n  Устанавливаю библиотеки...")
    result = os.system("pip install pytelegrambotapi requests colorama bs4 faker")
    
    if result == 0:
        clear_terminal()
        print("    Библиотеки успешно установлены!")
        return True
    else:
        print("    Ошибка при установке библиотек.")
        return False

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # 'nt' означает Windows

def run_main_script():
    response = input("    Хотите запустить RimmaPy сейчас? (Y/n): ")
    
    if response.lower() == 'y':
        os.system("py rimma.py" if os.name == 'nt' else 'python3 rimma.py')
    elif response.lower() == 'n':
        clear_terminal()
        print("\n    Для смены имени\n    Воспользуйтесь: python3 rms.py")

if __name__ == "__main__":
    clear_terminal()
    profile_make()
    installanswer()
    if install_libraries():
        run_main_script()
