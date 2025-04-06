# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
Leetcode: @new92
PyPI: @new92
Contributors: [@Itsfizziks, @ProgramR4732]

Tracker is a python script designed to monitor and maintain a record of a user's Instagram followers and followings

{*********IMPORTANT*********}
User's login credentials (such as: username, session file) won't be stored ! 
Will be used only for the purpose of Tracker.
"""
try:
    import sys
    from time import sleep
    if sys.version_info[0] < 3:
        print("[✘] Error ! Tracker requires Python 3 ! ")
        sleep(1.3)
        print("""[+] Instructions to download Python 3: 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        sleep(3)
        print("[+] Please install Python 3 and then use Tracker ✅")
        sleep(1)
        print("[+] Exiting...")
        sleep(0.8)
        sys.exit()
    from rich.align import Align
    from rich.table import Table
    from rich.live import Live
    from rich.console import Console
    console = Console()
    mods = ('sys', 'time', 'platform', 'os', 'colorama', 'rich', 'logging', 'requests', 'instaloader', 'csv', 'prettytable', 'argparse', 'ctypes')
    with console.status('[bold dark_orange]Loading module...[/]') as status:
        for mod in mods:
            sleep(0.85)
            console.log(f'[[bold red]{mod}[/]] => [bold green]okay ✔[/]')
    import platform
    from os import system
    import os
    import csv
    import argparse
    import ctypes
    import logging
    import instaloader
    import requests
    from colorama import init, Fore
except (ImportError, ModuleNotFoundError):
    print("[!] WARNING: Not all packages used in Tracker have been installed !")
    sleep(1.5)
    print("[+] Ignoring warning...")
    sleep(0.6)
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        if os.geteuid():
            print("[✘] Root user not detected !")
            sleep(1)
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
            sleep(1)
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
CYAN = Fore.LIGHTBLUE_EX

EMPTY = ('', ' ')
ANS = ('yes', 'no')

def clear():
    system('cls' if platform.system() == 'Windows' else 'clear')

sleep(0.8)
clear()
console.print("[bold green][✔] Successfully loaded modules.[/]")
sleep(0.8)
clear()

def fpath(fname: str):
    for root, dirs, files in os.walk('/'):
        if fname in files:
            return os.path.abspath(os.path.join(root, fname))

def Uninstall() -> str:
    def rmdir(dire):
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            DIRS = (os.path.join(root, dir) for dir in dirs)
        for i in DIRS:
            os.rmdir(i)
        os.rmdir(dire)
    rmdir(fpath('InstaTools'))
    return f'{GREEN}[✔] Files and dependencies removed successfully !'

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

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
js = ''
resp = requests.get('https://api.github.com/repos/new92/InstaTools', headers=headers)
if resp.status_code == 200:
    js = resp.json()

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

def banner() -> str:
    console.log("""[bold green]
 _______ _____            _____ _  ________ _____  
|__   __|  __ \     /\   / ____| |/ /  ____|  __ \ 
   | |  | |__) |   /  \ | |    | ' /| |__  | |__) |
   | |  |  _  /   / /\ \| |    |  < |  __| |  _  / 
   | |  | | \ \  / ____ \ |____| . \| |____| | \ \ 
   |_|  |_|  \_\/_/    \_\_____|_|\_\______|_|  \_\
[/]""", justify='center')

name = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TrackerLog.txt')).replace('\\', '/')
output = (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Tracker.csv')).replace('\\', '/')

def main(username: str, target: str, session: str):
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
    console.print("[bold yellow][+] Tracker is a python script which keeps track on the followers / followings of a user and informs the user for any changes.[/]")
    print("\n")
    console.print("[bold yellow][1] Start Tracker[/]")
    console.print("[bold yellow][2] Display Tracker's info[/]")
    console.print("[bold yellow][3] Clear log file[/]")
    console.print("[bold yellow][4] Uninstall InstaTools[/]")
    console.print("[bold yellow][5] Exit[/]")
    num=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while num not in range(1, 6):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1-5]")
        sleep(1)
        num=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if num == 1:
        clear()
        loader = instaloader.Instaloader()
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'consent.txt')):
            print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            con=input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").lower()
            while con not in ANS:
                print(f"{RED}[✘] Invalid answer !")
                sleep(1)
                print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
                sleep(1)
                con= input(f"{YELLOW}[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? ").lower()
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
                print(f"{YELLOW}[2] Uninstall Tracker and exit")
                num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                valErr = num in (1, 2)
                while not valErr:
                    try:
                        print(f"{YELLOW}[1] Exit")
                        print(f"{YELLOW}[2] Uninstall Tracker and exit")
                        sleep(1)
                        num=int(input(f"{YELLOW}[>] Please enter a number (from the above ones): "))
                        valErr = num in (1,2)
                    except ValueError:
                        print(f"{RED}[✘] Invalid number !")
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
                    sleep(0.8)
                    print(f"{YELLOW}[+] Thank you for using Tracker 🫡")
                    sleep(0.8)
                    print(f"{YELLOW}[+] Until we meet again 👋")
                    sleep(0.8)
                    sys.exit()
        sleep(2)
        clear()
        print(f"{GREEN}[*] Using session file >>> {session}...")
        sleep(1.3)
        try:
            with open(session, 'rb') as sessionfile:
                loader.context.load_session_from_file(username, sessionfile)
        except instaloader.exceptions.ConnectionException as ex:
            print(f"{RED}[✘] Error loading session file !")
            sleep(0.8)
            print(f"{YELLOW}[+] Error message >>> {ex}")
            sleep(1.5)
            print(f"{RED}[+] Exiting...")
            sys.exit()
        print(f"{GREEN}[✔] Session loaded successfully !")
        sleep(0.8)
        print(f"{GREEN}[✔] Login successfull !")
        sleep(0.85)
        clear()
        sleep(0.7)
        print(f"{YELLOW}[1] Track followers")
        print(f"{YELLOW}[2] Track followees")
        print(f"{YELLOW}[3] Track both")
        number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
        while number not in range(1,4):
            print(f"{RED}[✘] Invalid number !")
            sleep(1)
            print(f"{YELLOW}[1] Track followers")
            print(f"{YELLOW}[2] Track followees")
            print(f"{YELLOW}[3] Track both")
            number=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
        sleep(0.8)
        clear()
        sleep(0.8)
        print(f"{GREEN}[+] Acceptable answers >>> {ANS}")
        sleep(1)
        keep=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
        while keep in EMPTY or keep not in ANS:
            print(f"{RED}[✘] Invalid answer !")
            sleep(0.8)
            print(f"{YELLOW}[+] Acceptable answers >>> {ANS}")
            sleep(1)
            keep=input(f"{YELLOW}[?] Keep log ? ").strip().lower()
        keep = keep == ANS[0]
        sleep(0.8)
        clear()
        sleep(0.8)
        print(f"{CYAN}[*] Initiating Tracker...")
        sleep(0.8)
        if number == 1:
            print(f"{CYAN}[*] Loading profile...")
            sleep(0.8)
            profile = instaloader.Profile.from_username(loader.context, target)
            sleep(0.8)
            print(f"{GREEN}[✔] Profile loaded successfully !")
            sleep(0.5)
            print(f"{CYAN}[*] Extracting followers from {target}...")
            sleep(0.8)
            FOLLOWERS, FOLLOWERSAF = [follower.username for follower in profile.get_followers()], [follower.username for follower in profile.get_followers()]
            sleep(0.8)
            print(f"{GREEN}[✔] {len(FOLLOWERS)} extracted successfully !")
            sleep(1)
            print(f"{CYAN}[*] Starting tracker...")
            sleep(1.2)
            clear()
            sleep(0.8)
            while FOLLOWERS == FOLLOWERSAF:
                FOLLOWERSAF = [follower.username for follower in profile.get_followers()]
                print(f"{CYAN}[*] No new additions found on >>> {target}.")
                sleep(0.8)
                print(f"{YELLOW}[+] Sleeping for 5 minutes before checking again...")
                sleep(300)
                print('\n')
            if abs(len(FOLLOWERSAF) - len(FOLLOWERS)) > 1:
                if len(FOLLOWERS) > len(FOLLOWERSAF):
                    print(f"{GREEN}[*] {target} removed {len(FOLLOWERS) - len(FOLLOWERSAF)} follower(s).")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(0.5)
                    for follower in FOLLOWERS:
                        if follower not in FOLLOWERSAF:
                            print(f"{YELLOW}[⇒] User >>> https://instagram.com/{follower}/")
                else:
                    print(f"{GREEN}[*] {target} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers.")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(1)
                    for follower in FOLLOWERSAF:
                        if follower not in FOLLOWERS:
                            print(f"{YELLOW}[⇒] User >>> https://instagram.com/{follower}/")
                sleep(4)
            else:
                if len(FOLLOWERS) > len(FOLLOWERSAF):
                    print(f"{GREEN}[*] {target} removed 1 follower.")
                    sleep(0.5)
                    print(f"{YELLOW}[+] User >>> https://instagram.com/{[follower for follower in FOLLOWERS if follower not in FOLLOWERSAF][0]}/")
                else:
                    print(f"{GREEN}[*] {target} added 1 follower.")
                    sleep(0.5)
                    print(f"{YELLOW}[+] User >>> https://instagram.com/{[follower for follower in FOLLOWERSAF if follower not in FOLLOWERS][0]}/")
            sleep(0.8)
            print("\n\n")
            if keep:
                ADD, REM = [], []
                with open(name, 'w', encoding='utf-8') as f:
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        for counter, user in enumerate(FOLLOWERS):
                            if user not in FOLLOWERSAF:
                                f.write(f'{counter+1}) {user}\n')
                                REM.append(user)
                    else:
                        for counter, user in enumerate(FOLLOWERSAF):
                            if user not in FOLLOWERS:
                                f.write(f'{counter+1}) {user}\n')
                                ADD.append(user)
                ADD.extend([''] * (len(REM) - len(ADD))) if len(REM) > len(ADD) else REM.extend([''] * len(ADD) - len(REM))
                L = [
                    ['Followers removed', 'Followers added'],
                    [[REM[i], ADD[i]] for i in range(len(ADD))]
                ]
                with open(output, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(L)
                print(f"{GREEN}[✔] Successfully saved log.")
                sleep(1.3)
                print(f"{YELLOW}[↪] Log file name >>> 'TrackerLog.txt'")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV file name >>> 'Tracker.csv'")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log location >>> {name}")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV location >>> {output}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log file size >>> {os.stat(name).st_size} bytes")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV file size >>> {os.stat(output).st_size} bytes")
                sleep(2)

        elif number == 2:
            print(f"{CYAN}[*] Loading profile...")
            sleep(0.8)
            profile = instaloader.Profile.from_username(loader.context, target)
            sleep(0.8)
            print(f"{GREEN}[✔] Profile loaded successfully !")
            sleep(0.5)
            print(f"{CYAN}[*] Extracting followees from {target}...")
            sleep(0.8)
            FOLLOWEES, FOLLOWEESAF = [followee.username for followee in profile.get_followees()], [followee.username for followee in profile.get_followees()]
            sleep(0.8)
            print(f"{GREEN}[✔] {len(FOLLOWEES)} extracted successfully !")
            sleep(1)
            print(f"{CYAN}[*] Starting tracker...")
            sleep(1.2)
            clear()
            sleep(0.8)
            while FOLLOWEES == FOLLOWEESAF:
                FOLLOWEESAF = [followee.username for followee in profile.get_followees()]
                print(f"{CYAN}[*] No new additions found on >>> {target}.")
                sleep(0.8)
                print(f"{YELLOW}[+] Sleeping for 5 minutes before checking again...")
                sleep(300)
                print('\n')
            if abs(len(FOLLOWEESAF) - len(FOLLOWEES)) > 1:
                if len(FOLLOWEES) > len(FOLLOWEESAF):
                    print(f"{GREEN}[*] {target} unfollowed {len(FOLLOWEES) - len(FOLLOWEESAF)} users.")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(0.5)
                    for followee in FOLLOWEES:
                        if followee not in FOLLOWEESAF:
                            print(f"{YELLOW}[⇒] User >>> https://instagram.com/{followee}/")
                else:
                    print(f"{GREEN}[*] {target} started following {len(FOLLOWEESAF) - len(FOLLOWEES)} users.")
                    sleep(1)
                    print(f'{YELLOW}|----------|USERNAMES|----------|')
                    sleep(0.5)
                    for followee in FOLLOWEESAF:
                        if followee not in FOLLOWEES:
                            print(f"{YELLOW}[⇒] User >>> https://instagram.com/{followee}/")
                sleep(4)
            else:
                if len(FOLLOWEES) > len(FOLLOWEESAF):
                    print(f"{GREEN}[*] {target} stopped following 1 user.")
                    sleep(0.8)
                    print(f"{YELLOW}[+] User >>> https://instagram.com/{[followee for followee in FOLLOWEES if followee not in FOLLOWEESAF][0]}/")
                else:
                    print(f"{GREEN}[*] {target} started following 1 user.")
                    sleep(0.8)
                    print(f"{YELLOW}[+] User >>> https://instagram.com/{[followee for followee in FOLLOWEESAF if followee not in FOLLOWEES][0]}/")
            sleep(2)
            if keep:
                ADD, REM = [], []
                with open(name, 'w', encoding='utf-8') as f:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        for counter, user in enumerate(FOLLOWEES):
                            if user not in FOLLOWEESAF:
                                f.write(f'{counter+1}) {user}\n')
                                REM.append(user)
                    else:
                        for counter, user in enumerate(FOLLOWEESAF):
                            if user not in FOLLOWEES:
                                f.write(f'{counter+1}) {user}\n')
                                ADD.append(user)
                    ADD.extend([''] * (len(REM) - len(ADD))) if len(REM) > len(ADD) else REM.extend([''] * len(ADD) - len(REM))
                    L = [
                        ['Following removed', 'Followings added'],
                        [[REM[i], ADD[i]] for i in range(len(ADD))]
                    ]
                    with open(output, 'w') as f:
                        writer = csv.writer(f)
                        writer.writerows(L)
                print(f"{GREEN}[✔] Successfully saved log / CSV.")
                sleep(1.3)
                print(f"{YELLOW}[↪] Log file name >>> 'TrackerLog.txt'")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV file name >>> 'Tracker.csv'")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log location >>> {name}")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV location >>> {output}")
                sleep(0.4)
                print(f"{YELLOW}[↪] Log file size >>> {os.stat(name).st_size} bytes")
                sleep(0.4)
                print(f"{YELLOW}[↪] CSV file size >>> {os.stat(output).st_size} bytes")
                sleep(2)

        else:
            print(f"{CYAN}[*] Loading profile...")
            sleep(0.8)
            profile = instaloader.Profile.from_username(loader.context, target)
            sleep(0.8)
            print(f"{GREEN}[✔] Profile loaded successfully !")
            sleep(0.5)
            print(f"{CYAN}[*] Extracting followers/followees from {target}...")
            sleep(0.8)
            FOLLOWERS, FOLLOWERSAF, FOLLOWEES, FOLLOWEESAF = [follower.username for follower in profile.get_followers()], [follower.username for follower in profile.get_followers()], [followee.username for followee in profile.get_followees()], [followee.username for followee in profile.get_followees()]
            sleep(0.8)
            print(f"{GREEN}[✔] Successfully extracted {len(FOLLOWERS)} followers & {len(FOLLOWEES)} followees !")
            sleep(1)
            print(f"{CYAN}[*] Starting tracker...")
            sleep(1.2)
            clear()
            sleep(0.8)
            while FOLLOWERS == FOLLOWERSAF and FOLLOWEES == FOLLOWEESAF:
                FOLLOWERSAF = [follower.username for follower in profile.get_followers()]
                FOLLOWEESAF = [followee.username for followee in profile.get_followees()]
                print(f"{CYAN}[*] No changes found on {target}.")
                sleep(0.8)
                print(f"{YELLOW}[+] Sleeping for 5 minutes before checking again...")
                sleep(300)
                print('\n')
            if FOLLOWERS != FOLLOWERSAF:
                print(f"{GREEN}[!] Detected change on the {target}'s followers !")
                sleep(0.8)
                if abs(len(FOLLOWERSAF) - len(FOLLOWERS)) > 1:
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        print(f"{GREEN}[*] {target} removed {len(FOLLOWERS) - len(FOLLOWERSAF)} followers.")
                        sleep(1)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(0.5)
                        for follower in FOLLOWERS:
                            if follower not in FOLLOWERSAF:
                                print(f"{YELLOW}[⇒] User >>> https://instagram.com/{follower}/")
                    else:
                        print(f"{GREEN}[*] {target} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers.")
                        sleep(1)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(0.5)
                        for follower in FOLLOWERSAF:
                            if follower not in FOLLOWERS:
                                print(f"{YELLOW}[⇒] User >>> https://instagram.com/{follower}/")
                    sleep(4)
                else:
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        print(f"{GREEN}[*] {target} removed 1 follower.")
                        sleep(0.8)
                        print(f"{YELLOW}[⇒] User >>> https://instagram.com/{[usr for usr in FOLLOWERS if usr not in FOLLOWERSAF][0]}/")
                        sleep(0.8)
                    else:
                        print(f"{GREEN}[*] {target} added 1 follower.")
                        sleep(0.8)
                        print(f"{YELLOW}[*] User >>> https://instagram.com/{[follower for follower in FOLLOWERSAF if follower not in FOLLOWERS][0]}/")
                        sleep(0.8)
            else:
                print(f"{GREEN}[!] Detected change on the user's followings !")
                sleep(0.8)
                if abs(len(FOLLOWEESAF) - len(FOLLOWEES)) > 1:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        print(f"{GREEN}[*] {target} stopped following {len(FOLLOWEESAF) - len(FOLLOWEES)} users.")
                        sleep(1)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(0.5)
                        for followee in FOLLOWEES:
                            if followee not in FOLLOWEESAF:
                                print(f"{YELLOW}[⇒] User >>> https://instagram.com/{followee}/")
                    else:
                        print(f"{GREEN}[*] {target} started following {len(FOLLOWEESAF) - len(FOLLOWEES)}")
                        sleep(1)
                        print(f'{YELLOW}|----------|USERNAMES|----------|')
                        sleep(0.5)
                        for followee in FOLLOWEESAF:
                            if followee not in FOLLOWEES:
                                print(f"{YELLOW}[⇒] User >>> https://instagram.com/{followee}/")
                    sleep(4)
                else:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        print(f"{GREEN}[*] {target} stopped following 1 user.")
                        sleep(0.8)
                        print(f"{YELLOW}[⇒] User >>> https://instagram.com/{[FOLLOWEES[i] for i in range(len(FOLLOWEES)) if FOLLOWEES[i] not in FOLLOWEESAF][0]}/")
                    else:
                        print(f"{GREEN}[*] {target} started following 1 user.")
                        sleep(0.8)
                        print(f"{YELLOW}[⇒] User >>> https://instagram.com/{[FOLLOWEESAF[i] for i in range(len(FOLLOWEESAF)) if FOLLOWEESAF[i] not in FOLLOWEES][0]}/")
                    sleep(2)
        sleep(0.8)
        if keep:
            ADDFL, REMFL, ADD, RM = [], [], [], []
            with open(name, 'w', encoding='utf-8') as f:
                if len(FOLLOWERS) != len(FOLLOWERSAF):
                    if len(FOLLOWERS) > len(FOLLOWERSAF):
                        f.write(f'[*] {target} removed {len(FOLLOWERS) - len(FOLLOWERSAF)} followers.\n')
                        f.write('USERNAMES\n'+'-'*20+'\n')
                        for i in FOLLOWERS:
                            if i not in FOLLOWERSAF:
                                f.write(f'[⇒] User >>> https://instagram.com/{i}/\n')
                                REMFL.append(i)
                        f.write('-'*20)
                    else:
                        f.write(f'[*] {target} added {len(FOLLOWERSAF) - len(FOLLOWERS)} followers\n')
                        f.write('USERNAMES\n'+'-'*20+'\n')
                        for i in FOLLOWERSAF:
                            if i not in FOLLOWERS:
                                f.write(f'[⇒] User >>> https://instagram.com/{i}/\n')
                                ADDFL.append(i)
                        f.write('-'*20)
                else:
                    if len(FOLLOWEES) > len(FOLLOWEESAF):
                        f.write(f'[*] {target} stopped following {len(FOLLOWEES) - len(FOLLOWEESAF)} users\n')
                        f.write('USERNAMES\n'+'-'*20+'\n')
                        for i in FOLLOWEES:
                            if i not in FOLLOWEESAF:
                                f.write(f'[⇒] User >>> https://instagram.com/{i}/\n')
                                ADD.append(i)
                        f.write('-'*20)
                    else:
                        f.write(f'[*] {target} started following {len(FOLLOWEESAF) - len(FOLLOWEES)} users.\n')
                        f.write('USERNAMES\n' + '-' * 20 + '\n')
                        for i in FOLLOWEESAF:
                            if i not in FOLLOWEES:
                                f.write(f'[⇒] User >>> https://instagram.com/{i}/\n')
                            RM.append(i)
                        f.write('-'*20)
            ADDFL.extend([''] * len(REMFL) - len(ADDFL)) if len(REMFL) > len(ADDFL) else REMFL.extend([''] * len(ADDFL) - len(REMFL))
            ADD.extend([''] * len(RM) - len(ADD)) if len(RM) > len(ADD) else RM.extend([''] * len(ADD) - len(RM))
            L = [
                ['Followers removed', 'Followers added', 'Followings removed', 'Followings added'],
                [[REMFL[i], ADDFL[i]] for i in range(len(ADDFL))],
                [[RM[i], ADD[i]] for i in range(len(ADD))]
            ]
            with open(output, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(L)
            print(f"{GREEN}[✔] Successfully saved log / CSV.")
            sleep(1.3)
            print(f"{YELLOW}[↪] Log file name >>> 'TrackerLog.txt'")
            sleep(0.4)
            print(f"{YELLOW}[↪] CSV file name >>> 'Tracker.csv'")
            sleep(0.4)
            print(f"{YELLOW}[↪] Log location >>> {name}")
            sleep(0.4)
            print(f"{YELLOW}[↪] CSV location >>> {output}")
            sleep(0.4)
            print(f"{YELLOW}[↪] Log file size >>> {os.stat(name).st_size} bytes")
            sleep(0.4)
            print(f"{YELLOW}[↪] CSV file size >>> {os.stat(output).st_size} bytes")
            sleep(2)
    
    elif num == 2:
        clear()
        ScriptInfo()
        sleep(5)

    elif num == 3:
        clear()
        with open(name, 'w', encoding='utf-8') as f:
            pass
        print(f"{GREEN}[✔] Log file cleared successfully !")
        sleep(0.8)
        print(f"{YELLOW}[↪] Name >>> 'TrackerLog.txt'", f"{YELLOW}[↪] Location >>> {name}", f"{YELLOW}[↪] Size >>> 0 bytes", sep='\n')
        sleep(2)

    elif num == 4:
        clear()
        print(Uninstall())
        sleep(2)
        print(f"{GREEN}[+] Thank you for using Tracker 😁")
        sleep(0.8)
        print(f"{GREEN}[+] Until next time 🫡")
        sleep(0.8)
        sys.exit()

    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Tracker 😁")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()

    print(f"\n\n{YELLOW}[1] Return to menu\n{YELLOW}[2] Exit")
    numb=int(input(f"{YELLOW}[::] Please enter a number (from the above ones) >>> "))
    while numb not in range(1, 3):
        print(f"{RED}[✘] Invalid number !")
        sleep(1)
        print(f"{GREEN}[+] Acceptable numbers >>> [1,2]")
        sleep(1)
        numb=int(input(f"{YELLOW}[::] Please enter again a number (from the above ones) >>> "))
    if numb == 1:
        clear()
        main()
    else:
        clear()
        print(f"{GREEN}[+] Thank you for using Tracker 😁")
        sleep(0.8)
        print(f"{GREEN}[+] See you next time 👋")
        sleep(0.8)
        sys.exit()
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Tracker is a python script designed to monitor and maintain a record of a user's Instagram followers and followings. With Tracker, you can effortlessly keep tabs on changes in your Instagram network over time, making it a valuable tool for social media enthusiasts, influencers, and businesses looking to manage their online presence.")
        parser.add_argument('-u', '--username', help='Your instagram username.')
        parser.add_argument('-t', '--target', help='The target username to track their account.')
        parser.add_argument('-s', '--session', help='The session file to use. To generate it >>> python3 cookies.py')
        args = parser.parse_args()
        if len(sys.argv) < 4:
            print(f"{RED}[✘] Error: Missing arguments.")
            sleep(0.7)
            print(f"{GREEN}[+] Usage >>> python3 tracker.py -u <your_username> -t <target_username> -s <path_to_session_file>")
            sleep(1.5)
            args.username=input(f"{YELLOW}[::] Please enter your username >>> ") if not args.username else args.username
            args.target=input(f"{YELLOW}[::] Please enter the target username >>> ") if not args.target else args.target
            args.session=input(f"{YELLOW}[::] Please enter the session file >>> ") if not args.session else args.session
        main(args.username.strip().lower(), args.target.strip().lower(), args.session.strip().replace('\\', '/'))
except (KeyboardInterrupt, EOFError):
    print(f"\n\n{RED}[*] <Ctrl + C> detected. Exiting safely...")
    sys.exit()
