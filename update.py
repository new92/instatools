import subprocess, os
from time import sleep
from colorama import init, Fore

def update():
    init(autoreset=True)
    print(f"{Fore.LIGHTYELLOW_EX}[+] Updating InstaTools...")
    try:
        subprocess.run(['git', 'pull'], cwd=os.getcwd())
        print(f"{Fore.GREEN}[✔] InstaTools updated successfully.")
    except Exception as ex:
        print(f"{Fore.LIGHTRED_EX}[✘] An error occured !")
        sleep(0.5)
        print(f"{Fore.LIGHTYELLOW_EX}[+] Error message >>> {ex}")
        sleep(0.5)
        print(f"{Fore.LIGHTRED_EX}[+] Exiting...")
        quit()

if __name__ == '__main__':
    update()
