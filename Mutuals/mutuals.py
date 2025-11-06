# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Mutuals is a powerful Python script designed to discover and display mutual followers and followings between two Instagram accounts. Whether you're looking to strengthen connections or gain insights into shared networks, Mutuals simplifies the process, allowing users to identify and connect with those who share mutual interests and connections on Instagram.

For output example >>> ./Photos/output.png

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of Mutuals.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! IsVer requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3 : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use IsVer ✅")
        sleep(1.2)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'ctypes', 'csv', 'argparse')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import platform
    from os import system
    import instaloader
    import os
    import logging
    import requests
    import argparse
    import ctypes
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Mutuals have been installed !")
    sleep(1.5)
    print("[+] Ignoring warning...")
    sleep(0.6)
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        if os.geteuid():
            print("[✘] Root user not detected !")
            sleep(2)
            print("[+] Attempting to enable root user...")
            sleep(1)
            os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("sudo pip install -r ./../requirements.txt" if sys.platform.startswith('linux') else "python -m pip install ./../requirements.txt")
    elif platform.system() == 'Windows':
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("[✘] Root user not detected !")
            sleep(2)
            print("[+] Attempting to enable root user...")
            sleep(1)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("[+] Root user permission denied.")
                sleep(1)
                print("[+] Exiting...")
                sys.exit()
            print("[✔] Done.")
            sleep(0.6)
            print("[+] Loading required modules...")
            sleep(0.4)
        system("pip install -r ./../requirements.txt")

init(autoreset=True)
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.LIGHTYELLOW_EX

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.[/]")
sleep(0.8)
clear()

ANS = ('yes','no')
EMPTY = ('', ' ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
js = ''
resp = requests.get('https://api.github.com/repos/new92/InstaTools', headers=headers)
if resp.status_code == 200:
    js = resp.json()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))

def ScriptInfo():
    rest = requests.get('https://api.github.com/repos/new92/InstaTools/contributors', headers=headers)
    contribs = []
    if rest.status_code == 200:
        jsn = rest.json()
        contribs = [jsn[i]['login'] for i in range(len(jsn))]
    lang = requests.get('https://api.github.com/repos/new92/InstaTools/languages', headers=headers)
    languages = list(lang.json().keys()) if lang.status_code == 200 else []
    print(f"{YELLOW}[+] Author | {js['owner']['login']}")
    print(f"{YELLOW}[+] Github | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Leetcode | @{js['owner']['login']}")
    print(f"{YELLOW}[+] PyPI | @{js['owner']['login']}")
    print(f"{YELLOW}[+] Contributors | {contribs}")
    print(f"{YELLOW}[+] License | {js['license']['spdx_id']}")
    print(f"{YELLOW}[+] Programming language(s) used | {languages}")
    print(f"{YELLOW}[+] Script's name | {js['name']}")
    print(f"{YELLOW}[+] Latest update | {js['updated_at']}")
    print(f"{YELLOW}[+] File size | {os.stat(__file__).st_size} bytes")
    print(f"{YELLOW}[+] File path | {os.path.abspath(__file__)}")
    print(f"{YELLOW}[+] Directory path | {os.path.dirname(os.path.abspath(__file__))}")
    print(f"{YELLOW}|======|GITHUB REPO INFO|======|")
    print(f"{YELLOW}[+] Repo name | {js['name']}")
    print(f"{YELLOW}[+] Description | {js['description']}")
    print(f"{YELLOW}[+] Repo URL | {js['html_url']}")
    print(f"{YELLOW}[+] Stars | {js['stargazers_count']}")
    print(f"{YELLOW}[+] Forks | {js['forks']}")
    print(f"{YELLOW}[+] Watchers | {js['subscribers_count']}")
    print(f"{YELLOW}[+] Open issues | {js['open_issues_count']}")

TABLE = (
    (
        "[b white]Author[/]: [i light_green]new92[/]",
        "[green]https://new92.github.io/[/]"
    ),
    (
        "[b white]Github[/]: [i light_green]@new92[/]",
        "[green]https://github.com/new92[/]"
    ),
    (
        "[b white]Leetcode[/]: [i light_green]@new92[/]",
        "[green]https://leetcode.com/new92[/]"
    ),
    (
        "[b white]PyPI[/]: [i light_green]@new92[/]",
        "[green]https://pypi.org/user/new92[/]"
    )
)

def banner() -> str:
    console.log("""[bold green]
   _____    ____ ___ ___________ ____ ___   _____   .____       _________ 
  /     \  |    |   \\__    ___/|    |   \ /  _  \  |    |     /   _____/ 
 /  \ /  \ |    |   /  |    |   |    |   //  /_\  \ |    |     \_____  \  
/    Y    \|    |  /   |    |   |    |  //    |    \|    |___  /        \ 
\____|__  /|______/    |____|   |______/ \____|__  /|_______ \/_______  / 
        \/                                       \/         \/        \/  
[/]""", justify='center')

def Uninstall() -> str:
    def rmdir(dire):
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            DIRS = (os.path.join(root,dir) for dir in dirs)
        for i in DIRS:
            os.rmdir(i)
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f'{GREEN}[✔] Files and dependencies removed successfully !'

name = 'mutuals.txt'

def main(username: str, session: str, user1: str, user2: str):
    console = Console()
    table = Table(show_footer=False)
    centered = Align.center(table)
    banner()
    print("\n")
    with Live(centered, console=console, screen=False):
        table.add_column('Socials', no_wrap=False)
        table.add_column('Url', no_wrap=False)
        for row in TABLE:
            table.add_row(*row)
    print("\n")
    console.print("[bold yellow][+] Python script to retrieve the mutual followers/followings between 2 accounts.[/]")
    print("\n")
    console.print("[bold yellow][1] Find mutuals[/]")
    console.print("[bold yellow][2] Show Mutuals's info[/]")
    console.print("[bold yellow][3] Uninstall InstaTools[/]")
    console.print("[bold yellow][4] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1,5):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-5]")
        sleep(2)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        if not os.path.exists('./consent.txt'):
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            while con not in ANS or con in EMPTY:
                if con in EMPTY:
                    print(f"{RED}[✘] This field can't be blank !")
                else:
                    print(f"{RED}[✘] Invalid answer !")
                    sleep(1)
                    print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").strip().lower()
            if con == ANS[0]:
                logging.basicConfig(
                    filename='consent.txt',
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                logging.info('Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.')
            else:
                print(f"{YELLOW}[OK]")
                sleep(1)
                print(f"{YELLOW}[1] Exit")
                print(f"{YELLOW}[2] Uninstall Mutuals and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                valErr = num in (1, 2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall Mutuals and exit")
                        sleep(1)
                        num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones) >>> "))
                        valErr = num in (1,2)
                    except ValueError:
                        print(f"{RED}[!] Please enter a valid number.")
                        sleep(1)
                        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                        sleep(1)
                if num == 1:
                    clear()
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    sys.exit()
                else:
                    clear()
                    print(Uninstall())
                    sleep(2)
                    print(f"{RED}[+] Exiting...")
                    sleep(1)
                    print(f"{YELLOW}[+] Thank you for using Mutuals 🫡")
                    sleep(2)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(1)
                    sys.exit()
        sleep(2)
        clear()
        sleep(0.5)
        print(f"{GREEN}[*] Using session file >>> {session}...")
        sleep(1.3)
        try:
            with open(session, 'rb') as sessionfile:
                loader.context.load_session_from_file(username, sessionfile)
        except instaloader.exceptions.ConnectionException as ex:
            print(f"{RED}[✘] Error loading session file !")
            sleep(1)
            print(f"{YELLOW}[+] Error message >>> {ex}")
            sleep(0.8)
            print(f"{RED}[+] Exiting...")
            sys.exit()
        print(f"{GREEN}[✔] Session loaded successfully !")
        sleep(1.4)
        print(f"{GREEN}[✔] Login successfull !")
        sleep(0.85)
        clear()
        sleep(0.4)
        print(f"{YELLOW}[+] Loading profile...")
        sleep(0.6)
        profile = None
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
        except instaloader.ProfileNotExistsException:
            print(f"{RED}[✘] Profile not found")
            sleep(1)
            print("[1] Return to menu")
            print("[2] Exit")
            num=int(input("[::] Please enter a number (from the above ones) >>> "))
            while num not in range(1,3):
                print(f"{RED}[✘] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                sleep(1)
                num=int(input("[::] Please enter again a number (from the above ones) >>> "))
            if num == 1:
                clear()
                main(username, session, user1, user2)
            else:
                clear()
                print(f"{RED}[+] Exiting...")
                sleep(1)
                print(f"{GREEN}[+] See you next time 👋")
                sleep(0.8)
                sys.exit()
        if profile:
            sleep(0.5)
            print(f"{GREEN}[✔] Profile loaded successfully !")
            sleep(0.85)
            clear()
            print(f"{YELLOW}[1] Find the mutual followers")
            print(f"{YELLOW}[2] Find the mutual followees")
            print(f"{YELLOW}[3] Find the mutual followers & followees")
            t=int(input(f"{YELLOW}[::] Number >>> "))
            while t not in range(1,4):
                print(f"{RED}[✘] Invalid number !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
                sleep(2)
                print(f"{YELLOW}[1] Find mutual followers")
                print(f"{YELLOW}[2] Find mutual followees")
                print(f"{YELLOW}[3] Find the mutual followers & followees between 2 accounts")
                t=int(input(f"{YELLOW}[::] Number >>> "))
            profilef=instaloader.Profile.from_username(loader.context, user1)
            profiles=instaloader.Profile.from_username(loader.context, user2)
            if t == 1:
                clear()
                print(f"{GREEN}[*] Extracting mutual followers...")
                sleep(0.5)
                FOLLOWERSF=[follower.username for follower in profilef.get_followers()]
                FOLLOWERSS=[follower.username for follower in profiles.get_followers()]
                if FOLLOWERSF and FOLLOWERSS:
                    sumf = len(FOLLOWERSF) + len(FOLLOWERSS)
                    MUTUALS = [mutual for mutual in FOLLOWERSF if mutual in FOLLOWERSS] + [mutual for mutual in FOLLOWERSS if mutual in FOLLOWERSF]
                    if not MUTUALS:
                        print(f"{RED}[✘] No mutual followers found between {user1} & {user2}")
                        sleep(0.8)
                        print(f"{RED}[+] Exiting...")
                        sleep(1)
                        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                        sys.exit()
                    else:
                        print(f"{GREEN}[✔] Extracted {len(MUTUALS)} mutual followers from {user1} & {user2}")
                        sleep(1)
                        print(f"{YELLOW}[+] Percentage of mutual followers >>> {'{:.2f}'.format((len(MUTUALS) / float(sumf))*100)}%")
                        sleep(1)
                        print(f"{YELLOW}[+] Mutual followers betweeen {user1} & {user2}\n")
                        print('-' * 30 + '\n')
                        for counter, username in enumerate(MUTUALS):
                            print(f"{YELLOW}[{counter+1}] >>> https://www.instagram.com/{username}/")
                        sleep(3)
                        print("\n\n")
                        print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                        sleep(1)
                        savem=input(f"{YELLOW}[?] Save mutual followers ? ").strip().lower()
                        while savem not in ANS:
                            print(f"{RED}[✘] Invalid answer !")
                            sleep(1)
                            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                            sleep(1)
                            savem=input(f"{YELLOW}[?] Save mutual followers ? ").strip().lower()
                else:
                    print("\n\n")
                    print(f"{RED}[✘] No followers found on >>> {user1}" if not len(FOLLOWERSF) else f"{RED}[✘] No followers found on >>> {user2}")
                    sleep(0.6)
                    print(f"{RED}[+] Exiting...")
                    sleep(0.7)
                    print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                    sleep(0.8)
                    sys.exit()
            elif t == 2:
                clear()
                print(f"{GREEN}[*] Extracting mutual followees...")
                sleep(0.5)
                FOLLOWINGSF=[following.username for following in profilef.get_followees()]
                FOLLOWINGSS=[following.username for following in profiles.get_followees()]
                if FOLLOWINGSF and FOLLOWINGSS:
                    sumf = len(FOLLOWINGSF) + len(FOLLOWINGSS)
                    MUTUALS = [mutual for mutual in FOLLOWINGSF if mutual in FOLLOWINGSS] + [mutual for mutual in FOLLOWINGSS if mutual in FOLLOWINGSF]
                    if not MUTUALS:
                        print(f"{RED}[✘] No mutual followees found !")
                        sleep(0.8)
                        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                        sleep(0.8)
                        print(f"{RED}[+] Exiting...")
                        sleep(0.8)
                        sys.exit()
                    else:
                        print(f"{GREEN}[✔] Extracted {len(MUTUALS)} mutual followees from {user1} & {user2}")
                        sleep(0.8)
                        print(f"{YELLOW}[+] Percentage of mutual followees >>> {'{:.2f}'.format(len(MUTUALS) / float(sumf))*100}%")
                        sleep(0.8)
                        print(f"{YELLOW}[+] Mutual followees betweeen {user1} & {user2}\n")
                        print('-' * 30 + '\n')
                        for counter, username in enumerate(MUTUALS):
                            print(f"{YELLOW}[{counter+1}] https://www.instagram.com/{username}/")
                        sleep(3)
                        print("\n\n")
                        print(f'{GREEN}[+] Acceptable answers >>> {ANS}')
                        sleep(1)
                        savem=input(f"{YELLOW}[?] Save mutual followees ? ").strip().lower()
                        while savem not in ANS:
                            print(f"{RED}[✘] Invalid answer !")
                            sleep(1)
                            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                            sleep(1)
                            savem=input(f"{YELLOW}[?] Save mutual followees ? ").strip().lower()
                else:
                    print("\n\n")
                    print(f"{RED}[✘] No followees found on >>> {user1}" if not len(FOLLOWINGSF) else f"{RED}[✘] No followees found on >>> {user2}")
                    sleep(0.6)
                    print(f"{RED}[+] Exiting...")
                    sleep(0.7)
                    print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                    sleep(0.8)
                    sys.exit()
            else:
                clear()
                print(f"{GREEN}[*] Extracting both mutual followers & followees...")
                sleep(0.5)
                FOLLOWERSF=[follower.username for follower in profilef.get_followers()]
                FOLLOWERSS=[follower.username for follower in profiles.get_followers()]
                FOLLOWINGSF=[following.username for following in profilef.get_followees()]
                FOLLOWINGSS=[following.username for following in profiles.get_followees()]
                if FOLLOWERSF and FOLLOWERSS and FOLLOWINGSF and FOLLOWINGSS:
                    sumf = len(FOLLOWERSF) + len(FOLLOWERSS) + len(FOLLOWINGSF) + len(FOLLOWINGSS)
                    MUTUALS = [mutual + '| follower' for mutual in FOLLOWERSF if mutual in FOLLOWERSS] + [mutual + '| follower' for mutual in FOLLOWERSS if mutual in FOLLOWERSF] + [mutual + '| followee' for mutual in FOLLOWINGSF if mutual in FOLLOWINGSS] + [mutual + '| followee' for mutual in FOLLOWINGSS if mutual in FOLLOWINGSF]
                    if not MUTUALS:
                        print(f"{RED}[✘] No mutuals found !")
                        sleep(0.8)
                        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
                        sleep(0.8)
                        print(f"{RED}[+] Exiting...")
                        sleep(0.8)
                        sys.exit()
                    else:
                        print(f"{GREEN}[✔] Extracted {len(MUTUALS)} mutual followees from {user1} & {user2}")
                        sleep(0.8)
                        print(f"{YELLOW}[+] Percentage of mutuals >>> {'{:.2f}'.format(len(MUTUALS) / float(sumf))*100}%")
                        sleep(0.8)
                        print(f"{YELLOW}[+] Mutual followers / followees betweeen {user1} & {user2}\n")
                        print('-' * 30 + '\n')
                        for counter, username in enumerate(MUTUALS):
                            print(f"{YELLOW}[{counter+1}] https://www.instagram.com/{username[:username.find('|')]}/ {username[username.find('|'):]}")
                        sleep(3)
                        print("\n\n")
                        print(f'{GREEN}[+] Acceptable answers >>> {ANS}')
                        sleep(1)
                        savem=input(f"{YELLOW}[?] Save mutuals ? ").strip().lower()
                        while savem not in ANS:
                            print(f"{RED}[✘] Invalid answer !")
                            sleep(1)
                            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                            sleep(1)
                            savem=input(f"{YELLOW}[?] Save mutuals ? ").strip().lower()
                        with open(f'./{name}', 'w', encoding='utf-8') as f:
                            for counter, username in enumerate(MUTUALS):
                                f.write(f"{YELLOW}[{counter+1}] https://www.instagram.com/{username[:username.find('|')]}/ {username[username.find('|'):]}")
                else:
                    print("\n\n")
                    print(f"{RED}[✘] Error: Unable to gather enough data for extraction !")
                    sleep(0.6)
                    print(f"{RED}[+] Exiting...")
                    sleep(0.7)
                    sys.exit()
            if savem == ANS[0] and MUTUALS and num != 3:
                print(f"{YELLOW}[*] Writing mutuals in {name}...")
                with open(f'./{name}', 'w', encoding='utf-8') as f:
                    for counter, username in enumerate(MUTUALS):
                        f.write(f"[{counter+1}] https://www.instagram.com/{username}/\n")
            sleep(0.8)
            print(f"{GREEN}[✔] Successfully saved mutuals !")
            sleep(0.8)
            print(f"{YELLOW}[↪] Name >>> {name}", f"{YELLOW}[↪] Location >>> ./{name}", f"{YELLOW}[↪] Size >>> {os.stat(('./' + name)).st_size}", sep='\n')

    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
        sleep(1.5)
        print(f"{GREEN}[+] Until we meet again 🫡")
        sleep(0.8)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Mutuals 😁")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()

    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while number not in range(1, 3):
        print(f"{RED}[✘] Invalid number !")
        sleep(0.8)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(1)
        number=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if number == 1:
        clear()
        main(username, session, user1, user2)
    else:
        print(f"{RED}[+] Exiting...")
        sleep(1)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(2)
        sys.exit()
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Mutuals is a python script used to find the mutual followers and/or followings between 2 accounts on Instagram.')
        parser.add_argument('-u', '--username', help='Your Instagram username.')
        parser.add_argument('-u1', '--user1', help='The first username for the mutuals retrieval')
        parser.add_argument('-u2', '--user2', help='The second username for the mutuals retrieval')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >>> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 5:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 mutuals.py -u <username> -u1 <user_1> -u2 <user_2> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
            args.u1=input(f"{YELLOW}[::] Please enter the first username for the mutuals retrieval >>> ") if not args.u1 else args.u1
            args.u2=input(f"{YELLOW}[::] Please enter the second username for the mutuals retrieval >>> ") if not args.u2 else args.u2
        main(args.username.strip().lower(), args.session.strip().replace('\\', '/'), args.user1.strip().lower(), args.user2.strip().lower())
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()
