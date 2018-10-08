class Character:
    def __init__(self, charattrdict):
        self.charclass = charattrdict["charclass"]


def calc_hsm(charattrdict):
    charattrdict["health"] = int((charattrdict["strength"] + 2 * charattrdict["vitality"]) / 3)
    charattrdict["stamina"] = round((charattrdict["agility"] + charattrdict["vitality"]) / 2)
    if charattrdict["magic"] > 0:
        charattrdict["mana"] = int((charattrdict["intelligence"] + 2 * charattrdict["magic"]) / 3)
    else:
        charattrdict["mana"] = 0

    return charattrdict


def print_menu(state, charattrdict):
    if state == 'start':
        print("\n1. Start New Game")
        print("2. Quit Game")
        selection = input("Please enter a number: ")
        if selection == '1':
            state = 'charselect'
        elif selection == '2':
            state = 'quit'
        else:
            print("Invalid selection, please try again.")

    if state == 'charselect':
        print("\n1. Play as a fighter")
        print("2. Play as a thief")
        print("3. Play as a magic user")
        selection = input("Please enter a number: ")
        if selection == '1':
            charattrdict["charclass"] = 'Fighter'
            charattrdict["strength"] = 25
            charattrdict["intelligence"] = 10
            charattrdict["agility"] = 15
            charattrdict["vitality"] = 15
            charattrdict["luck"] = 10
            charattrdict["magic"] = 0
            charattrdict["weapon use"] = 20
            charattrdict["parry"] = 15
            charattrdict["dodge"] = 10
            charattrdict["stealth"] = 0
            charattrdict["pick locks"] = 0
            charattrdict["throwing"] = 10
            charattrdict["climbing"] = 0
            charattrdict = calc_hsm(charattrdict)
            state = 'skillselect'
        elif selection == '2':
            charattrdict["charclass"] = 'Thief'
            charattrdict["strength"] = 10
            charattrdict["intelligence"] = 15
            charattrdict["agility"] = 25
            charattrdict["vitality"] = 10
            charattrdict["luck"] = 10
            charattrdict["magic"] = 0
            charattrdict["weapon use"] = 10
            charattrdict["parry"] = 0
            charattrdict["dodge"] = 5
            charattrdict["stealth"] = 10
            charattrdict["pick locks"] = 10
            charattrdict["throwing"] = 5
            charattrdict["climbing"] = 5
            charattrdict = calc_hsm(charattrdict)
            state = 'skillselect'
        elif selection == '3':
            charattrdict["charclass"] = 'Magic User'
            charattrdict["strength"] = 10
            charattrdict["intelligence"] = 25
            charattrdict["agility"] = 15
            charattrdict["vitality"] = 15
            charattrdict["luck"] = 10
            charattrdict["magic"] = 25
            charattrdict["weapon use"] = 10
            charattrdict["parry"] = 0
            charattrdict["dodge"] = 15
            charattrdict["stealth"] = 0
            charattrdict["pick locks"] = 0
            charattrdict["throwing"] = 0
            charattrdict["climbing"] = 0
            charattrdict = calc_hsm(charattrdict)
            state = 'skillselect'
        else:
            print("Invalid selection, please try again.")

    if state == 'skillselect':
        points = 50
        while points > 0:
            print("\nYou have the following skills:")
            for key, value in charattrdict.items():
                if key is not "charclass" and key is not "name":
                    print(key, value)
            print("\nYou have " + str(points) + " points left.")
            print("Note that 15 points will be spent to raise a skill from an initial 0 to a score of 5.")
            selection = ''
            while selection not in charattrdict.keys():
                selection = input("Please enter the name of a skill to add to: ")
            if charattrdict[selection] > 0:
                charattrdict[selection] += 5
                points -= 5
            if charattrdict[selection] == 0:
                charattrdict[selection] += 5
                points -= 15
            charattrdict = calc_hsm(charattrdict)
        state = 'nameselect'

    if state == 'nameselect':
        charattrdict["name"] = input("\nPlease enter a name for you character: ")
        state = 'play'

    if state == 'quit':
        print("Goodbye.")
        exit()

    return state, charattrdict


def endless_battle(charattrdict):
    pass


if __name__ == '__main__':
    state = 'start'
    charattrdict = {}

    while state != 'play':
        state, charattrdict = print_menu(state, charattrdict)

    while True:
        endless_battle(charattrdict)
