import random
import time
from asciimatics.screen import Screen
from copy import deepcopy
from win import demo #Win 
from virus import hacking_simulation
from downloading import download_animation #exeucting
from firewall_anim import firewall_creaion #Firewall
from thickofit import charging_animation #Charing RAHHHHH
from hadouken import bomb_animation
from win_bot import bot_win_cutscene
#Add Charge
def main(): 
    player = {
        "Health": 2,
        "Defense": 0,
        "Charge": 0 
    }
    bot = {
        "Health": 2,
        "Defense": 0,
        "Charge": 0
    }
    action = ["attack","defense","charge"] #Bot decision
    bold = "\033[1m"
    while bot["Health"] > 0 and player["Health"] > 0:
        #Player actions
        print()
        print("1: Charge\n2: Attack (Require 1 charge)\n3: Block (Stackable)\n4: Special attack (Bypass Block)\n")
        try:
            user = int(input("Action: "))
        except ValueError:
            print("Invalid input please input 1-4")
            continue
        prev_player = deepcopy(player)
        prev_bot = deepcopy(bot)
        if user == 1:
            user_str = "Charge"
            charge(player)
        elif user == 2:
            if player["Charge"] >0:
                user_str = "Attack"
                attack(player, bot)
            else:
                print("Not enough charge to attack! Choose another action.")
                continue
        elif user == 3:
            user_str = "Defense"
            block(player)
        elif user == 4:
            user_str = "Special_attack"
            special_move(player, bot)
        elif user == 5: #For debug purpose
            print(player)
            print(bot)
            continue
        else:
            print("Invalid input please input 1-3")
            continue    
            
        bot_decision = bot_action(bot, player, action)

        print("-" * 24)
        print()
        if user_str == "Defense":
            print(f"Your action: Block")
        else:
            print(f"Your action: {user_str}")
        print(f"Bot action: {bot_decision}\n")
        print("-" * 24)

        confirm = (input("Confirm action yes/no: ")).lower()
        if confirm == "yes" or confirm == 'y':
            #Trigger ascii animation
            download_animation()
            #Downlaod
            if user_str == "Attack":
                hacking_simulation()
                print()
                print(f"{bold}Completed!")
                print()
                #Update for player
                if bot_decision == "Attack":
                    player = prev_player
                    bot = prev_bot
                    player["Charge"] -= 1
                    bot["Charge"] -= 1
                    print(player)
                    print(bot)
                elif bot_decision == "Block":
                    player = prev_player
                    bot = prev_bot
                    player["Charge"] -= 1
                    print(player)
                    print(bot)
                else:
                    print(player)
                    print(bot)
            if user_str == "Special_attack" and bot_decision == "Attack":
                player["Health"] += 1
                print("RAH STRONGER ATTACk!!!!")
            if user_str == "Defense":
                firewall_creaion()
                print()
                #Firewall
                if bot_decision == "Attack":
                    player = prev_player
                    bot = prev_bot
                    bot["Charge"] -= 1
                    print(player)
                    print(bot)
                else:
                    print(player)
                    print(bot)
            
            if user_str == "Charge":
                charging_animation()
                print()
                #Data stream
                print(player)
                print(bot)
            if user_str == "Special_attack":
                bomb_animation()
                print()
                print()
                print(player)
                print(bot)
            if player["Health"] <= 0:
                print("BOT WIN")
                input("Please Enter to exit...")
                try:
                    Screen.wrapper(bot_win_cutscene)
                except TypeError:
                    break
            elif bot["Health"] <= 0:
                print("PLAYER WIN")
                input("Please Enter to continue...")
                try:
                    Screen.wrapper(demo)
                except TypeError:
                    break
        else:
            print("No take back executing...") #Repeatly
            #Trigger the ascii animation
            #Trigger ascii animation
            if confirm == "yes" or confirm == 'y':
            #Trigger ascii animation
                download_animation()
            #Downlaod
                if user_str == "Attack":
                    hacking_simulation()
                    print()
                    print(f"{bold}Completed!")
                    print()
                    #Update for player
                    if bot_decision == "Attack":
                        player = prev_player
                        bot = prev_bot
                        player["Charge"] -= 1
                        bot["Charge"] -= 1
                        print(player)
                        print(bot)
                    elif bot_decision == "Block":
                        player = prev_player
                        bot = prev_bot
                        player["Charge"] -= 1
                        print(player)
                        print(bot)
                    else:
                        print(player)
                        print(bot)
                if user_str == "Special_attack" and bot_decision == "Attack":
                    player["Health"] += 1
                    print("RAH STRONGER ATTACk!!!!")
                if bot_decision == "Attack":
                    if bot["Charge"] <= 0:
                        bot["Charge"] += 1
                if user_str == "Defense":
                    firewall_creaion()
                    print()
                    #Firewall
                    if bot_decision == "Attack":
                        player = prev_player
                        bot = prev_bot
                        bot["Charge"] -= 1
                        print(player)
                        print(bot)
                    else:
                        print(player)
                        print(bot)
                if user_str == "Charge":
                    charging_animation()
                    print()
                    #Data stream
                    print(player)
                    print(bot)
                if user_str == "Special_attack":
                    bomb_animation()
                    print()
                    print()
                    print(player)
                    print(bot)
                if player["Health"] <= 0:
                    print("BOT WIN")
                    input("Please Enter to exit...")
                    try:
                        Screen.wrapper(bot_win_cutscene)
                    except TypeError:
                        break
                elif bot["Health"] <= 0:
                    print("PLAYER WIN")
                    input("Please Enter to continue...")
                    try:
                        Screen.wrapper(demo)
                    except TypeError:
                        break

        # print(f"Debug: user: {user}, bot_decision: {bot_decision}")

        # Negate codition RAHHHH (Should work now)
        if (user == 2 and bot_decision == "Block") or (user == 3 and bot_decision == "Attack"):
            print("-"*12)
            print("Negated!!!! did not count!")
            print("-"*12)
    
            player = prev_player
            bot = prev_bot
        if (user == 2 and bot_decision == "Attack"):
            print("-"*12)
            print("ATTACK NEGEATED!!!!! ")
            print("-"*12)

            player = prev_player
            bot = prev_bot
            
        #Win condition
        if player["Health"] <= 0:
            print("BOT WIN")
            input("Please Enter to exit...")
            try:
                Screen.wrapper(demo)
            except TypeError:
                break
        elif bot["Health"] <= 0:
            print("PLAYER WIN")
            input("Please Enter to exit...")
            try:
                Screen.wrapper(demo)
            except TypeError:
                break
            #everything stay the same like the last turn before this was casted
def attack(attacker, victim):
    if attacker["Charge"] > 0:
        attacker["Charge"] -= 1
        if victim["Defense"] > 0:
            victim["Defense"] -= 1 
            # print("The attack hit the defense! Defense has been lowered.")
        else:
            victim["Health"] -= 1
            #print("The attack bypassed! Health has been lowered.")
    else:
        print("Not enough charge to attack!")


def block(caster):
    #MAXDEFENSE = 3
    if caster["Defense"] < 3:
        caster["Defense"] += 1
    else:
        print(f"Defense is already at maximum (3)!")

def charge(caster):
    caster["Charge"] += 1
    #Charge function

def special_move(attacker, victim):
    if attacker["Charge"] >= 3:
        attacker["Charge"] -= 3
        victim["Health"] -= 1
    else:
        print(f"Not enought charge require (4).")
func_action = [("Attack", attack), ("Block", block), ("Charge", charge)]
def bot_action(bot, player, actions):
    """Determines the bot's next action based on current state."""
    if bot["Charge"] > 0 and player["Health"] > 1:  # Attack if charged and player has health left
        number = random.randrange(1, 7)
        if number == 4:
            attack(bot, player)
            return "Attack"
        else:
            action_name, random_action = random.choice(func_action)
            if random_action in [block, charge]:
                random_action(bot)
            else:
                random_action(bot, player)
            return action_name

    elif bot["Charge"] == 0 and player["Defense"] > 0:  # Charge up if out of charges
        number = random.randrange(1, 7)
        if number == 3:
            charge(bot)
            return "Charge"
        else:
            action_name, random_action = random.choice(func_action)
            if random_action in [block, charge]:
                random_action(bot)
            else:
                random_action(bot, player)
            return action_name

    else:  # Default to defense
        number = random.randrange(1, 7)
        if number == 2:
            block(bot)
            return "Block"
        else:
            action_name, random_action = random.choice(func_action)
            if random_action in [block, charge]:
                random_action(bot)
            else:
                random_action(bot, player)
            return action_name
if __name__ == "__main__":
    main()