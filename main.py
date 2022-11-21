# imports

import random

# GAME OPTIONS YOU RECEIVE IN GAME

Combat = {'Excalibur': 500, 'Wooden_Sword': 15, 'Obsidian_Sword': 35,
          'Diamond_Gauntlets': 30, 'Punch': 10}  # Setup dict. for all Shields, Swords, and Potions
Shields = {'Heroes_shield': 50, 'Bronze_Shield': 15, 'Diamond_Shield': 30, 'Obsidian_Shield': 35}
Potion = {'Blue_Heal': 50, 'Red_Heal': 40, 'Yellow_Heal': 30, 'Green_Heal': 20}

Fighting = {'Excalibur': 500, 'Wooden_Sword': 15, 'Obsidian_Sword': 35,
          'Diamond_Gauntlets': 30, 'Punch': 10}
Blocking = {'Heroes_shield': 50, 'Bronze_Shield': 15, 'Diamond_Shield': 30, 'Obsidian_Shield': 35}
Healing = {'Blue_Heal': 50, 'Red_Heal': 40, 'Yellow_Heal': 30, 'Green_Heal': 20}
Option = [Fighting, Healing, Blocking]  # list function for loots randomizer

# START UP OPTIONS

Your_Weapon = {'Excalibur': Combat['Excalibur'], 'Wooden_Sword': Combat['Wooden_Sword'], 'Punch': Combat['Punch']}
Your_Potion = {'Green_Heal': Potion['Green_Heal']}
Your_Shield = {'Bronze_Shield': Shields['Bronze_Shield']}
Your_Health = {'Hp': 3000}

# SETS UP INVENTORY

Fight = {'Weapon': Your_Weapon}
Heal = {'Potions': Your_Potion}
Block = {'Shield': Your_Shield}
Inventory = [Fight, Heal, Block]
USerP = ['Weapon', 'Heal', 'Shield', 'Inventory']
USer = ['Weapon', 'Heal', 'Shield']
W = ''
S = ''
reluctance = 0

# HEROES + RANDOMIZER HERO
Heroes = ('Heracles', 'Achilles', 'Beowulf', 'Sun_Wukong')  # Heroes (TUPLE) randomize
Picked_Hero = random.choice(Heroes)
Hname = Picked_Hero
Hp = ''
Slay = ''
Regen = ''
Protect = ''
Heart = 0
Arm = 0
Reg = ''
Prot = 0
if Picked_Hero == 'Heracles':
  Hp = 'Heracles_Hp'
  Slay = 'Bare_Hands'
  Regen = 'Potion'
  Protect = 'Immunity'
  Heart = 99900
  Arm = 40
  Reg = 40
  Prot = 30
elif Picked_Hero == 'Achilles':
  Hp = 'Achilles_hp'
  Slay = 'Spear_Thrust'
  Regen = 'Potion'
  Protect = 'Protects_heel'
  Heart = 99900
  Arm = 30
  Reg = 20
  Prot = 40
elif Picked_Hero == 'Beowulf':
  Hp = 'Beowulf_hp'
  Slay = 'Hrunting_Slash'
  Regen = 'Potion'
  Protect = 'Block'
  Heart = 99900
  Arm = 35
  Reg = 50
  Prot = 60
elif Picked_Hero == 'Sun_Wukong':
  Hp = 'Beowulf_hp'
  Slay = 'Staff_Smash'
  Regen = 'Potion'
  Protect = 'Staff_Block'
  Heart = 99900
  Arm = 20
  Reg = 30
  Prot = 50

# HEROES & SETUPS THE Hero CHOICES
Picked_Hero = {Hp: Heart, Slay: Arm, Regen: Reg, Protect: Prot}
H_1_C = ''

# DEMONS & SETUPS THE DEMON CHOICES
Mammon = {'Mammon_hp': 100, 'Punch': 10, 'Potion': 30, 'Parry': 15}
D_1_C = ''
Leviathan = {'Leviathan_hp': 250, 'Tail_Whip': 25, 'Potion': 40, 'Water_Shield': 80}
D_2_C = ''
Lucifer = {'Lucifer_hp': 500, 'Dragon_Claw': 50, 'Potion': 90, 'Overwhelming_Pride': 90}
D_3_C = ''
Satan = {'Satan_hp': 1000, 'Storm_Bringer': 100, 'Punch_OfDestruction': 0, 'Potion': 100, 'Grab':20}
D_4_C = ''

# LOOT RANDOMIZER

Loot_1 = random.choice(list(Option))
Loot_1_2 = random.choice(list(Loot_1))
Loot_1_2_3 = Loot_1[Loot_1_2]
del Loot_1[Loot_1_2]

Loot_2 = random.choice(list(Option))
Loot_2_2 = random.choice(list(Loot_2))
Loot_2_2_3 = Loot_2[Loot_2_2]
del Loot_2[Loot_2_2]

Loot_3 = random.choice(list(Option))
Loot_3_2 = random.choice(list(Loot_3))
Loot_3_2_3 = Loot_3[Loot_3_2]
del Loot_3[Loot_3_2]

Loot_4 = random.choice(list(random.choice(list(Option))))

# STARTING THE GAME (AUTO FOR THE FIRST ITERATION) // ENDING THE GAME

Choice = 'y'
while Choice != 'n':


   # Dialogue
    # entering your name 
    name = input('\nOpening your eyes a portal meets before your feet. The purple voids never ending swirl makes you '
                 'weary.\nYou clench your fist. You know you can do this because your name is:', )
    print('\nLooking to your sides you are met with a group of heroes. {} is from the kingdom of the north. {} is '
          'from the kingdom of the south. {} is from the kingdom of the east. {} is from the kingdom of the '
          'west.'.format(Heroes[2], Heroes[0], Heroes[1], Heroes[3]))

  
    input('Press enter to continue')
  
    print('\nThe Heroes are surrounding a grave.')
    input('Press enter to continue')
  
    print('\nHeores please come with me')
    print('\n{} stands up and wipes his face. I will go with you adventurer {}. The demon world stands beyond this void and we need to do '
        'everything we can to save this world from there evil violence.'.format(Hname, name))
    print('\nThe other Heroes turn back around and continue staring at the grave.\n{}: They wont move lets go...'.format(Hname))
    input('Press enter to continue')

    print('\nThe Hero {} and the adventurer {} walk into the portal.'.format(Hname, name))
    input('Press enter to continue')

    print('\nLooking up to the sky you are met with a blackish-purple haze. The ground is dry with cracks going on till the horizon.')
    input('Press enter to continue')

    print('\nYou feel intimidated but you have to accomplish your missin of destroying this land, you take steps forward.')
    input('Press enter to continue')

    print('\nYou see a small building ahead.\nYou and the hero approach the building.')
    input('Press enter to continue')

    print('\nA shiver runs down your spine')
    input('Press enter to continue')
  
    print('\nDemon: Who dare comes forth into the demon outpost.\n{}: I am the Mighty Hero {} and the Adventurer {}. \nYou: We '
        'have come to destroy this place and this dimension of demons who dare threatens our beloved Earth.'.format(Hname, Hname, name))
    input('Press enter to continue')

    print('\nDemon: I will not let this happen as I am the Mammon the guardian of this outpost.\nFight.')
    while Mammon['Mammon_hp'] > 0:
        print('\nYour health is {}'.format(Your_Health['Hp']))
        print('Mammon Health is {}'.format(Mammon['Mammon_hp']))
        print('{} Health is {}\n'.format(Hname, Picked_Hero[Hp]))
        O_1 = input('{}>>'.format(USerP))
        print('\n')

        if (len(Your_Potion) == 0) and (O_1 == 'Heal'):
            O_1 = 'reset'

            # YOUR CHOICE OUTCOMES

        if O_1 == 'Weapon':
            W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            while W not in Your_Weapon:
                print('Enter one of the options')
                W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            print('\nYou use {} damage {}'.format(W, Your_Weapon[W]))
        elif O_1 == 'Shield':
            S = input('Which Shield would you like to use {}'.format(Your_Shield))
            while S not in Your_Shield:
                print('Enter one of the options')
                S = input('Which Shield would you like to use{}'.format(Your_Shield))
            print('\nyou use {} shield blocks {}'.format(S, Shields[S]))
        elif (O_1 == 'Heal') and (len(Your_Potion) > 0):
            P = input('Which Potion would you like to use {}'.format(Your_Potion))
            while P not in Your_Potion:
                print('Enter one of the options')
                P = input('Which Weapon would you like to use {}'.format(Your_Potion))
            print('\nYou use {} it heals {}'.format(P, Potion[P]))
            Your_Health['Hp'] += Your_Potion[P]
            del Your_Potion[P]
        elif O_1 == 'Inventory':
            print(Inventory)
        else:
            print('\nEnter one of the options that contain an item')

        # DEMON AI SETUP

        if (Mammon['Mammon_hp'] > 50) and (O_1 in USer):
            print('Mammon uses Punch damage {}'.format(Mammon['Punch']))
        elif (Mammon['Mammon_hp'] <= 20) and (O_1 in USer) and ('Potion' in Mammon):
            print('Mammon uses Heal it heals {}'.format(Mammon['Potion']))
            Mammon['Mammon_hp'] += Mammon['Potion']
            del Mammon['Potion']
        elif (Mammon['Mammon_hp'] <= 50) and (O_1 in USer):
            D_1_C = random.choice([Mammon['Punch'], Mammon['Parry']])
            if D_1_C == Mammon['Punch']:
                print('Mammon uses Punch damage {}'.format(Mammon['Punch']))
            elif D_1_C == Mammon['Parry']:
                print('Mammon uses Parry blocks {}'.format(Mammon['Parry']))

        # HERO AI SETUP
        if (Picked_Hero[Hp] <= 20) and (O_1 in USer) and (Regen in Picked_Hero):
            print('{} uses {} it heals {}'.format(Hname, Picked_Hero[Regen], Picked_Hero[Reg]))
            Picked_Hero[Hp] += Picked_Hero[Reg]
            del Picked_Hero[Regen]
        elif (O_1 in USer):
            H_1_C = random.choice([Picked_Hero[Slay], Picked_Hero[Protect]])
            if H_1_C == Picked_Hero[Slay]:
                print('{} uses {} damage {}'.format(Hname, Slay, Picked_Hero[Slay]))
            elif H_1_C == Picked_Hero[Protect]:
                print('{} uses {} it blocks {}'.format(Hname, Protect, Picked_Hero[Protect]))

        # ATTACK OPTION FOR DEMON

        if (D_1_C == Mammon['Punch'] or (Mammon['Mammon_hp'] > 50)) and (O_1 in USer):
            if O_1 != 'Shield' and H_1_C != Picked_Hero[Protect]:
                Your_Health['Hp'] -= Mammon['Punch']
                Picked_Hero[Hp] -= Mammon['Punch']
            elif O_1 != 'Shield' and H_1_C == Picked_Hero[Protect]:
              Your_Health['Hp'] -= Mammon['Punch']
              if Picked_Hero[Protect] >= Mammon['Punch']:  
                print('The {} blocks Mammons damage'.format(Hname))
              elif Picked_Hero[Protect] < Mammon['Punch']:
                Picked_Hero[Hp] -= ((Mammon['Punch'] - Picked_Hero[Protect]) / 2)
            elif O_1 == 'Shield' and H_1_C != Picked_Hero[Protect]:
              Your_Health['Hp'] -= Mammon['Punch']
              if Picked_Hero[Protect] >= Mammon['Punch']:  
                print('You block Mammons damage')
              elif Picked_Hero[Protect] < Mammon['Punch']:
                Picked_Hero[Hp] -= ((Mammon['Punch'] - Picked_Hero[Protect]) / 2)
            elif O_1 == 'Shield' and H_1_C == Picked_Hero[Protect]:
                if Your_Shield[S] >= Mammon['Punch'] and Picked_Hero[Protect] >= Mammon['Punch']: 
                    print('You and the Hero blocks Mammons damage')
                elif Your_Shield[S] < Mammon['Punch'] and Picked_Hero[Protect] >= Mammon['Punch']:
                    Your_Health['Hp'] -= ((Mammon['Punch'] - Your_Shield[S]) / 2)
                    print('{} was able to block Mammons damage'.format(Hname))
                elif Your_Shield[S] >= Mammon['Punch'] and Picked_Hero[Protect] < Mammon['Punch']:
                  Picked_Hero[Hp] -= ((Mammon['Punch'] - Picked_Hero[Protect]) / 2)
                  print('You were able to block Mammons damage')
                elif Your_Shield[S] < Mammon['Punch'] and Picked_Hero[Protect] >= Mammon['Punch']:
                  Your_Health['Hp'] -= ((Mammon['Punch'] - Your_Shield[S]) / 2)
                  Picked_Hero[Hp] -= ((Mammon['Punch'] - Picked_Hero[Protect]) / 2)

            # ATTACK OPTIONS FOR YOU
        if O_1 == 'Weapon':
            if (D_1_C == Mammon['Punch'] or Mammon['Mammon_hp'] > 0) and (O_1 in USer):
                Mammon['Mammon_hp'] -= Your_Weapon[W]
            elif D_1_C == Mammon['Parry']:
                if Mammon['Parry'] < Your_Weapon[W]:
                    Mammon['Mammon_hp'] -= Your_Weapon[W] - Mammon['Parry']
                elif Mammon['Parry'] >= Your_Weapon[W]:
                    print('Mammon negated your attack')
                  
            #  ATTACK OPTION FOR HERO
        if H_1_C == Picked_Hero[Slay] and (O_1 in USer):
            if (D_1_C == Mammon['Punch'] or Mammon['Mammon_hp'] > 0):
                Mammon['Mammon_hp'] -= Picked_Hero[Slay]
            elif D_1_C == Mammon['Parry']:
                if Mammon['Parry'] < Picked_Hero[Slay]:
                    Mammon['Mammon_hp'] -= Picked_Hero[Slay] - Mammon['Parry']
                elif Mammon['Parry'] >= Picked_Hero[Slay]:
                    print('Mammon negated the Heroes attack')


            # SHIELDS FOR ALL

        if O_1 == 'Shield' and D_1_C == Mammon['Parry'] and H_1_C == Picked_Hero[Protect]:
            print('Nothing happened')

        # GAME OVER

    if Your_Health['Hp'] <= 0:
        print('\nyour health is now {}, you have died'.format(Your_Health['Hp']))
        break
    elif Mammon['Mammon_hp'] <= 0:
        print('\nMammon: I can not believe you killed me.')
        print('You have defeated Mammon')
        # LOOT

    if Loot_1 == Fighting:
        Your_Weapon[Loot_1_2] = Loot_1_2_3
    elif Loot_1 == Healing:
        Your_Potion[Loot_1_2] = Loot_1_2_3
    elif Loot_1 == Blocking:
        Your_Shield[Loot_1_2] = Loot_1_2_3

      # Destruction prompt (user based)

    print('\nYou think to yourself "I want to destroy" ')
    Destroy_1 = input('Shall you destroy Mammons Outpost(y, n)?')
    while Destroy_1 != 'y' and Destroy_1!= 'n': 
      print('\nEnter an option')
      Destroy_1 = input('Shall you destroy Mammon Outpost?(y, n)')
    if Destroy_1 == 'y':
      reluctance += 1
      print('\nYou use your punch to knocking down the columns that hold the building ')
      print('The building crumbles down')
      input('Press enter to continue')
      print('\nYou leave the mess of a building and continue on you journey')
    elif Destroy_1 == 'n':
        print('You leave Mammon hideout alone and continue on your journey.')

       # Destruction prompt cont.
  
    print('\nOn the way out of the outpost in the ruckage of the battle field you see an object portruding. You pick it up.\n You have now gained {}'.format(Loot_1_2))
    input('Press enter to continue')

    print('\n{}:congradulations adventurer on your first defeat.'.format(Hname))
    print('A long path leads to a mountain')
    print('You: Lets continue our path to our next demon')
    input('Press enter to continue')

    print('\nClimming up the mountains the blackish-purple haze burdens your vision. You keep climbing')
    input('Press enter to continue')

    print('\nYou and {} have now reached the summit of the mountain. An ocean of water and clouds are infront of you.'.format(Hname))
    input('Press enter to continue')

    print('\n{}: lets take a rest here for now. An hour passes.'.format(Hname))
    input('Press enter to continue')

    print('\nYou see somthing out of the corner of your eye.\nYou: {} look as you point towards the water. {} turns around.\n{}: Nothing is there. \nNothing is there.\nThe hero {} turns back to you.'.format(Hname, Hname, Hname, Hname))
    input('Press enter to continue')

    print('\nYou: there again.\n{} turns around. A body of a long creature is exiting and re-entering the water.'.format(Hname))
    print('Demon: Who sits on this shore, you look mortal.\nYou: we have come to defeat you and destroy the underworld')
    print('Demon: Lets see you try for I am Leviathan.\nFight')
    input('Press enter to continue')

    while Leviathan['Leviathan_hp'] > 0:
        print('\nYour health is {}'.format(Your_Health['Hp']))
        print('Leviathan Health is {}'.format(Leviathan['Leviathan_hp']))
        print('{} Health is {}\n'.format(Hname, Picked_Hero[Hp]))
        O_2 = input('{}>>'.format(USerP))
        print('\n')
        if (len(Your_Potion) == 0) and (O_2 == 'Heal'):
            O_2 = 'reset'

            # YOUR CHOICE OUTCOMES

        if O_2 == 'Weapon':
            W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            while W not in Your_Weapon:
                print('Enter one of the options')
                W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            print('You use {} damage {}'.format(W, Your_Weapon[W]))
        elif O_2 == 'Shield':
            S = input('Which Shield would you like to use {}'.format(Your_Shield))
            while S not in Your_Shield:
                print('Enter one of the options')
                S = input('Which Shield would you like to use{}'.format(Your_Shield))
            print('you use {} shield blocks {}'.format(S, Shields[S]))
        elif (O_2 == 'Heal') and (len(Your_Potion) > 0):
            P = input('Which Potion would you like to use {}'.format(Your_Potion))
            while P not in Your_Potion:
                print('Enter one of the options')
                P = input('Which Weapon would you like to use {}'.format(Your_Potion))
            print('You use {} it heals {}'.format(P, Potion[P]))
            Your_Health['Hp'] += Your_Potion[P]
            del Your_Potion[P]
        elif O_2 == 'Inventory':
            print(Inventory)
        else:
            print('\nEnter one of the options that contain an item')

        # DEMON AI SETUP

        if (Leviathan['Leviathan_hp'] > 50) and (O_2 in USer):
            print('Leviathan uses Tail_Whip damage {}'.format(Leviathan['Tail_Whip']))
        elif (Leviathan['Leviathan_hp'] <= 20) and (O_2 in USer) and ('Potion' in Leviathan):
            print('Leviathan uses Heal it heals {}'.format(Leviathan['Potion']))
            Leviathan['Leviathan_hp'] += Leviathan['Potion']
            del Leviathan['Potion']
        elif (Leviathan['Leviathan_hp'] <= 50) and (O_2 in USer):
            D_2_C = random.choice([Leviathan['Tail_Whip'], Leviathan['Water_Shield']])
            if D_2_C == Leviathan['Tail_Whip']:
                print('Leviathan uses Tail_Whip damage {}'.format(Leviathan['Tail_Whip']))
            elif D_2_C == Leviathan['Water_Shield']:
                print('Leviathan uses Water_Shield blocks {}'.format(Leviathan['Water_Shield']))

        # HERO AI SETUP
        if (Picked_Hero[Hp] <= 20) and (O_2 in USer) and (Regen in Picked_Hero):
            print('Picked_Hero uses {} it heals {}'.format(Picked_Hero[Regen], Picked_Hero[Reg]))
            Picked_Hero[Hp] += Picked_Hero[Reg]
            del Picked_Hero[Regen]
        elif (O_2 in USer):
            H_1_C = random.choice([Picked_Hero[Slay], Picked_Hero[Protect]])
            if H_1_C == Picked_Hero[Slay]:
                print('Picked_Hero uses {} damage {}'.format(Slay, Picked_Hero[Slay]))
            elif H_1_C == Picked_Hero[Protect]:
                print('Picked_Hero uses {} it blocks {}'.format(Protect, Picked_Hero[Protect]))

        # ATTACK OPTION FOR DEMON

        if D_2_C == Leviathan['Tail_Whip'] or (Leviathan['Leviathan_hp'] > 50) and (O_2 in USer):
            if O_2 != 'Shield' and H_1_C != Picked_Hero[Protect]:
                Your_Health['Hp'] -= Leviathan['Tail_Whip']
                Picked_Hero[Hp] -= Leviathan['Tail_Whip']
            elif O_2 != 'Shield' and H_1_C == Picked_Hero[Protect]:
              Your_Health['Hp'] -= Leviathan['Tail_Whip']
              if Picked_Hero[Protect] >= Leviathan['Tail_Whip']:  
                print('The {} blocks Leviathans damage'.format(Hname))
              elif Picked_Hero[Protect] < Leviathan['Tail_Whip']:
                Picked_Hero[Hp] -= ((Leviathan['Tail_Whip'] - Picked_Hero[Protect]) / 2)
            elif O_2 == 'Shield' and H_1_C != Picked_Hero[Protect]:
              Your_Health['Hp'] -= Leviathan['Tail_Whip']
              if Picked_Hero[Protect] >= Leviathan['Tail_Whip']:  
                print('You block Leviathans damage')
              elif Picked_Hero[Protect] < Leviathan['Tail_Whip']:
                Picked_Hero[Hp] -= ((Leviathan['Tail_Whip'] - Picked_Hero[Protect]) / 2)
            elif O_2 == 'Shield' and H_1_C == Picked_Hero[Protect]:
                if Your_Shield[S] >= Leviathan['Tail_Whip'] and Picked_Hero[Protect] >= Leviathan['Tail_Whip']: 
                    print('You and the Hero blocks Leviathans damage')
                elif Your_Shield[S] < Leviathan['Tail_Whip'] and Picked_Hero[Protect] >= Leviathan['Tail_Whip']:
                    Your_Health['Hp'] -= ((Leviathan['Tail_Whip'] - Your_Shield[S]) / 2)
                    print('{} was able to block Leviathans damage'.format(Hname))
                elif Your_Shield[S] >= Leviathan['Tail_Whip'] and Picked_Hero[Protect] < Leviathan['Tail_Whip']:
                  Picked_Hero[Hp] -= ((Leviathan['Tail_Whip'] - Picked_Hero[Protect]) / 2)
                  print('You were able to block Leviathans damage')
                elif Your_Shield[S] < Leviathan['Tail_Whip'] and Picked_Hero[Protect] >= Leviathan['Tail_Whip']:
                  Your_Health['Hp'] -= ((Leviathan['Tail_Whip'] - Your_Shield[S]) / 2)
                  Picked_Hero[Hp] -= ((Leviathan['Tail_Whip'] - Picked_Hero[Protect]) / 2)

            # ATTACK OPTIONS FOR YOU
        if O_2 == 'Weapon':
            if (D_2_C == Leviathan['Tail_Whip'] or Leviathan['Leviathan_hp'] > 0) and (O_2 in USer):
                Leviathan['Leviathan_hp'] -= Your_Weapon[W]
            elif D_2_C == Leviathan['Water_Shield']:
                if Leviathan['Water_Shield'] < Your_Weapon[W]:
                    Leviathan['Leviathan_hp'] -= Your_Weapon[W] - Leviathan['Water_Shield']
                elif Leviathan['Water_Shield'] >= Your_Weapon[W]:
                    print('Leviathan negated your attack')
                  
            #  ATTACK OPTION FOR HERO
        if H_1_C == Picked_Hero[Slay] and (O_2 in USer):
            if (D_2_C == Leviathan['Tail_Whip'] or Leviathan['Leviathan_hp'] > 0):
                Leviathan['Leviathan_hp'] -= Picked_Hero[Slay]
            elif D_2_C == Leviathan['Water_Shield']:
                if Leviathan['Water_Shield'] < Picked_Hero[Slay]:
                    Leviathan['Leviathan_hp'] -= Picked_Hero[Slay] - Leviathan['Water_Shield']
                elif Leviathan['Water_Shield'] >= Picked_Hero[Slay]:
                    print('Leviathan negated the Heroes attack')


            # SHIELDS FOR ALL

        if O_2 == 'Shield' and D_2_C == Leviathan['Water_Shield'] and H_1_C == Picked_Hero[Protect]:
            print('Nothing happened')

        # GAME OVER

    if Your_Health['Hp'] <= 0:
        print('your health is now {}, you have died'.format(Your_Health['Hp']))
        break
    elif Leviathan['Leviathan_hp'] <= 0:
      print('\nLeviathan: I can not believe you killed me.')
      print('You have defeated Leviathon')

    if Loot_2 == Combat:
        Your_Weapon[Loot_2_2] = Loot_2_2_3
    elif Loot_2 == Potion:
        Your_Potion[Loot_2_2] = Loot_2_2_3
    elif Loot_2 == Potion:
        Your_Shield[Loot_2_2] = Loot_2_2_3

  #  Destruction prompt cont.
    print('\nYou think to yourself "I want to destroy" ')
    Destroy_2 = input('Shall you destroy Leviathans hideout(y, n)?')
    while Destroy_2 != 'y' and Destroy_2!= 'n': 
      print('\nEnter an option')
      Destroy_2 = input('Shall you destroy Leviathans hideout?(y, n)')
    if Destroy_2 == 'y':
      reluctance += 1
      print('You use your punch to create a hole on the side of the mountain which leads the water to flow out until it is empty')
      print('The building crumbles down')
      input('Press enter to continue')
      print('\nYou leave the mess of the ocean and continue on you journey')
    elif Destroy_2 == 'n':
        print('You leave Leviathans ocean alone and continue on your journey.')

    print('\nOn the way out of the mountains in the ruckage of the battle field you see an object portruding. You pick it up.\n You have now gained {}'.format(Loot_2_2))
    input('Press enter to continue')

    print('\n{}: Congradulaitons you have defeated leviathan'.format(Hname))
    input('Press enter to continue')

    print('\nAnother path leads down to the horizon. You follow this path.\nContinuing down this path you see a hole')
    input('Press enter to continue')

    print('\n{}: lets enter I have heard of a demon who likes to have his castle underground. He is the devil of pride.'.format(Hname))
    input('Press enter to continue')

    print('\nYou and {} enter the hole. Your hands slip on the surface you roll down into a slide.\nYou turn right-left-Right again.'.format(Hname))
    input('Press enter to continue')

    print('\nYou land on a giant red cusion.')
    input('Press enter to continue')
    
    print('\nA demon stands in front of you.\nDemon: ooooh what do we have here two fresh meals for me, pointing at the hero you look delicious.\nHe then looks at you.\nDemon: you however are not perfect so I will let one of my underlings have you')
    input('Press enter to continue')

    print('\nDemon: let us have a fight though, I will beat you for I am Lucifer.')
    input('Press enter to continue')
      
    while Lucifer['Lucifer_hp'] > 0:
        print('\nYour health is {}'.format(Your_Health['Hp']))
        print('Lucifer Health is {}'.format(Lucifer['Lucifer_hp']))
        print('{} Health is {}\n'.format(Hname, Picked_Hero[Hp]))
        O_3 = input('{}>>'.format(USerP))
        print('\n')
        if (len(Your_Potion) == 0) and (O_3 == 'Heal'):
            O_3 = 'reset'

            # YOUR CHOICE OUTCOMES

        if O_3 == 'Weapon':
            W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            while W not in Your_Weapon:
                print('Enter one of the options')
                W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            print('You use {} damage {}'.format(W, Your_Weapon[W]))
        elif O_3 == 'Shield':
            S = input('Which Shield would you like to use {}'.format(Your_Shield))
            while S not in Your_Shield:
                print('Enter one of the options')
                S = input('Which Shield would you like to use{}'.format(Your_Shield))
            print('you use {} shield blocks {}'.format(S, Shields[S]))
        elif (O_3 == 'Heal') and (len(Your_Potion) > 0):
            P = input('Which Potion would you like to use {}'.format(Your_Potion))
            while P not in Your_Potion:
                print('Enter one of the options')
                P = input('Which Weapon would you like to use {}'.format(Your_Potion))
            print('You use {} it heals {}'.format(P, Potion[P]))
            Your_Health['Hp'] += Your_Potion[P]
            del Your_Potion[P]
        elif O_3 == 'Inventory':
            print(Inventory)
        else:
            print('\nEnter one of the options that contain an item')

        # DEMON AI SETUP

        if (Lucifer['Lucifer_hp'] > 250) and (O_3 in USer):
            print('Lucifer uses Dragon_Claw damage {}'.format(Lucifer['Dragon_Claw']))
        elif (Lucifer['Lucifer_hp'] <= 200) and (O_3 in USer) and ('Potion' in Lucifer):
            print('Lucifer uses Heal it heals {}'.format(Lucifer['Potion']))
            Lucifer['Lucifer_hp'] += Lucifer['Potion']
            del Lucifer['Potion']
        elif (Lucifer['Lucifer_hp'] <= 250) and (O_3 in USer):
            D_3_C = random.choice([Lucifer['Dragon_Claw'], Lucifer['Overwhelming_Pride']])
            if D_3_C == Lucifer['Dragon_Claw']:
                print('Lucifer uses Dragon_Claw damage {}'.format(Lucifer['Dragon_Claw']))
            elif D_3_C == Lucifer['Overwhelming_Pride']:
                print('Lucifer uses Overwhelming_Pride blocks {}'.format(Lucifer['Overwhelming_Pride']))

        # HERO AI SETUP
        if (Picked_Hero[Hp] <= 20) and (O_3 in USer) and (Regen in Picked_Hero):
            print('Picked_Hero uses {} it heals {}'.format(Picked_Hero[Regen], Picked_Hero[Reg]))
            Picked_Hero[Hp] += Picked_Hero[Reg]
            del Picked_Hero[Regen]
        elif (O_3 in USer):
            H_1_C = random.choice([Picked_Hero[Slay], Picked_Hero[Protect]])
            if H_1_C == Picked_Hero[Slay]:
                print('Picked_Hero uses {} damage {}'.format(Slay, Picked_Hero[Slay]))
            elif H_1_C == Picked_Hero[Protect]:
                print('Picked_Hero uses {} it blocks {}'.format(Protect, Picked_Hero[Protect]))

        # ATTACK OPTION FOR DEMON

        if (D_3_C == Lucifer['Dragon_Claw'] or (Lucifer['Lucifer_hp'] > 250)) and (O_3 in USer):
            if O_3 != 'Shield' and H_1_C != Picked_Hero[Protect]:
                Your_Health['Hp'] -= Lucifer['Dragon_Claw']
                Picked_Hero[Hp] -= Lucifer['Dragon_Claw']
            elif O_3 != 'Shield' and H_1_C == Picked_Hero[Protect]:
                Your_Health['Hp'] -= Lucifer['Dragon_Claw']
                if Picked_Hero[Protect] >= Lucifer['Dragon_Claw']:  
                    print('The {} blocks Lucifers damage'.format(Hname))
                elif Picked_Hero[Protect] < Lucifer['Dragon_Claw']:
                    Picked_Hero[Hp] -= ((Lucifer['Dragon_Claw'] - Picked_Hero[Protect]) / 2)
            elif O_3 == 'Shield' and H_1_C != Picked_Hero[Protect]:
                Your_Health['Hp'] -= Lucifer['Dragon_Claw']
                if Picked_Hero[Protect] >= Lucifer['Dragon_Claw']:  
                    print('You block Lucifers damage')
                elif Picked_Hero[Protect] < Lucifer['Dragon_Claw']:
                    Picked_Hero[Hp] -= ((Lucifer['Dragon_Claw'] - Picked_Hero[Protect]) / 2)
            elif O_3 == 'Shield' and H_1_C == Picked_Hero[Protect]:
                if Your_Shield[S] >= Lucifer['Dragon_Claw'] and Picked_Hero[Protect] >= Lucifer['Dragon_Claw']: 
                    print('You and the Hero blocks Lucifers damage')
                elif Your_Shield[S] < Lucifer['Dragon_Claw'] and Picked_Hero[Protect] >= Lucifer['Dragon_Claw']:
                    Your_Health['Hp'] -= ((Lucifer['Dragon_Claw'] - Your_Shield[S]) / 2)
                    print('{} was able to block Lucifers damage'.format(Hname))
                elif Your_Shield[S] >= Lucifer['Dragon_Claw'] and Picked_Hero[Protect] < Lucifer['Dragon_Claw']:
                    Picked_Hero[Hp] -= ((Lucifer['Dragon_Claw'] - Picked_Hero[Protect]) / 2)
                    print('You were able to block Lucifers damage')
                elif Your_Shield[S] < Lucifer['Dragon_Claw'] and Picked_Hero[Protect] >= Lucifer['Dragon_Claw']:
                    Your_Health['Hp'] -= ((Lucifer['Dragon_Claw'] - Your_Shield[S]) / 2)
                    Picked_Hero[Hp] -= ((Lucifer['Dragon_Claw'] - Picked_Hero[Protect]) / 2)

            # ATTACK OPTIONS FOR YOU
        if O_3 == 'Weapon':
            if (D_3_C == Lucifer['Dragon_Claw'] or Lucifer['Lucifer_hp'] > 0) and (O_3 in USer):
                Lucifer['Lucifer_hp'] -= Your_Weapon[W]
            elif D_3_C == Lucifer['Overwhelming_Pride']:
                if Lucifer['Overwhelming_Pride'] < Your_Weapon[W]:
                    Lucifer['Lucifer_hp'] -= Your_Weapon[W] - Lucifer['Overwhelming_Pride']
                elif Lucifer['Overwhelming_Pride'] >= Your_Weapon[W]:
                    print('Lucifer negated your attack')
                  
            #  ATTACK OPTION FOR HERO
        if H_1_C == Picked_Hero[Slay] and (O_3 in USer):
            if (D_3_C == Lucifer['Dragon_Claw'] or Lucifer['Lucifer_hp'] > 0):
                Lucifer['Lucifer_hp'] -= Picked_Hero[Slay]
            elif D_3_C == Lucifer['Overwhelming_Pride']:
                if Lucifer['Overwhelming_Pride'] < Picked_Hero[Slay]:
                    Lucifer['Lucifer_hp'] -= Picked_Hero[Slay] - Lucifer['Overwhelming_Pride']
                elif Lucifer['Overwhelming_Pride'] >= Picked_Hero[Slay]:
                    print('Lucifer negated the Heroes attack')


            # SHIELDS FOR ALL

        if O_3 == 'Shield' and D_3_C == Lucifer['Overwhelming_Pride'] and H_1_C == Picked_Hero[Protect]:
            print('Nothing happened')

        # GAME OVER

    if Your_Health['Hp'] <= 0:
        print('your health is now {}, you have died'.format(Your_Health['Hp']))
        break
    elif Lucifer['Lucifer_hp'] <= 0:
        print('\nLucifer: I can not believe you killed me.')
        print('You have defeated Lucifer')

        #YOU OBTAIN A LOOT ITEM

    if Loot_3 == Combat:
        Your_Weapon[Loot_3_2] = Loot_3_2_3
    elif Loot_3 == Potion:
        Your_Potion[Loot_3_2] = Loot_3_2_3
    elif Loot_3 == Potion:
        Your_Shield[Loot_3_2] = Loot_3_2_3
      
    print('\nYou think to yourself "I want to destroy" ')
    Destroy_3 = input('Shall you destroy Lucifers hideout(y, n)?')
    while Destroy_3 != 'y' and Destroy_3!= 'n': 
      print('\nEnter an option')
      Destroy_3 = input('Shall you destroy Lucifers hideout?(y, n)')
    if Destroy_3 == 'y':
      reluctance += 1
      print('You use your punch to knock down the columns that hold the building ')
      print('The building crumbles down')
      input('Press enter to continue')
      print('\nYou leave the mess of a building and continue on you journey')
    elif Destroy_3 == 'n':
        print('You leave Lucifers hideout alone and continue on your journey.')

    print('\nOn the way out of the mountains in the ruckage of the battle field you see an object portruding. You pick it up.\n You have now gained {}'.format(Loot_3_2))
    input('Press enter to continue')
      
    print('\n{}: Congradulations {} on defeating Lucifer. We have been a long way from the begging of our journey. We have one last boss and is the worst of them all. \nHis name is Satan. This is hard on me but there was once a Shield Hero who perished by Satan.\nIn a last effort he was able to lock the castle up with Satan so he could never exit again until another hero opens the door.'.format(Hname, name))
    input('Press enter to continue')
  
    print('\n{} reaches for the door an object is holding the door shut. {} grabs the item to let the door opens.'.format(Hname, Hname))
    print('\n{}: here hopefully youll be able to make some use out of it'.format(Hname))
    input('Press enter to continue')
  
    if Loot_4 in Combat:
        Your_Weapon[Loot_4] = Combat[Loot_4]
    elif Loot_4 in Shields:
        Your_Shield[Loot_4] = Shields[Loot_4]
    elif Loot_4 in Potion:
        Your_Potion[Loot_4] = Potion[Loot_4]

    print('\nYou now obtain the item {}'.format(Loot_4))
    input('Press enter to continue')
    print('\nThe castle rumbles... "the ground rumbles"')
    input('\nPress enter to continue')
    print('\nThe doors swing open')
    input('Press enter to continue')
    print('\nDemon: Finally someone has freed me of my imprisonment. I can now destroy my objective of destroying Earth as my name is Satan.')
    input('Press enter to continue')
    print('\n{}: We have come to destroy you before you can destroy earth.\nSatan: No one has done it before and no one will do it now'.format(Hname))
    input('Press enter to continue')
  
    while Satan['Satan_hp'] > 0:
        D_4_C = ''
        print('\nYour health is {}'.format(Your_Health['Hp']))
        print('Satan Health is {}'.format(Satan['Satan_hp']))
        print('{} Health is {}\n'.format(Hname, Picked_Hero[Hp]))
        O_4 = input('{}>>'.format(USerP))
        print('\n')
        if (len(Your_Potion) == 0) and (O_4 == 'Heal'):
            O_4 = 'reset'

            # YOUR CHOICE OUTCOMES

        if O_4 == 'Weapon':
            W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            while W not in Your_Weapon:
                print('Enter one of the options')
                W = input('Which Weapon would you like to use{}'.format(Your_Weapon))
            print('You use {} damage {}'.format(W, Your_Weapon[W]))
        elif O_4 == 'Shield':
            S = input('Which Shield would you like to use {}'.format(Your_Shield))
            while S not in Your_Shield:
                print('Enter one of the options')
                S = input('Which Shield would you like to use{}'.format(Your_Shield))
            print('you use {} shield blocks {}'.format(S, Shields[S]))
        elif (O_4 == 'Heal') and (len(Your_Potion) > 0):
            P = input('Which Potion would you like to use {}'.format(Your_Potion))
            while P not in Your_Potion:
                print('Enter one of the options')
                P = input('Which Weapon would you like to use {}'.format(Your_Potion))
            print('You use {} it heals {}'.format(P, Potion[P]))
            Your_Health['Hp'] += Your_Potion[P]
            del Your_Potion[P]
        elif O_4 == 'Inventory':
            print(Inventory)
        else:
            print('\nEnter one of the options that contain an item')

        # DEMON AI SETUP

        if ((Satan['Satan_hp'] > 500) and ('Punch_OfDestruction' in Satan)) and (O_4 in USer):
          D_4_C = 'Punch_OfDestruction'      
        elif (Satan['Satan_hp'] > 500) and (O_4 in USer):
            print('Satan uses Storm_Bringer damage {}'.format(Satan['Storm_Bringer']))
        elif (Satan['Satan_hp'] <= 400) and (O_4 in USer) and ('Potion' in Satan):
            print('Satan uses Heal it heals {}'.format(Satan['Potion']))
            Satan['Satan_hp'] += Satan['Potion']
            del Satan['Potion']
        elif (Satan['Satan_hp'] <= 500) and (O_4 in USer):
            D_4_C = random.choice([Satan['Storm_Bringer'], Satan['Grab']])
            if D_4_C == Satan['Storm_Bringer']:
                print('Satan uses Storm_Bringer damage {}'.format(Satan['Storm_Bringer']))
            elif D_4_C == Satan['Grab']:
                print('Satan uses Grab blocks {}'.format(Satan['Grab']))

        # HERO AI SETUP
        if (Picked_Hero[Hp] <= 20) and (O_4 in USer) and (Regen in Picked_Hero):
            print('Picked_Hero uses {} it heals {}'.format(Picked_Hero[Regen], Picked_Hero[Reg]))
            Picked_Hero[Hp] += Picked_Hero[Reg]
            del Picked_Hero[Regen]
        elif (O_4 in USer):
            H_1_C = random.choice([Picked_Hero[Slay], Picked_Hero[Protect]])
            if H_1_C == Picked_Hero[Slay]:
                print('Picked_Hero uses {} damage {}'.format(Slay, Picked_Hero[Slay]))
            elif H_1_C == Picked_Hero[Protect]:
                print('Picked_Hero uses {} it blocks {}'.format(Protect, Picked_Hero[Protect]))

        # ATTACK OPTION FOR DEMON
            if D_4_C == 'Punch_OfDestruction' and (O_4 in USer):
                del  Satan[D_4_C]
                if O_4 == 'Weapon' and H_1_C:
                  del Your_Weapon[W]
                  print('{} has now been destroyed and no longer usable'.format(W))
                elif O_4 == 'Shield':
                  del Your_Shield[S]
                  print('{} has now been destroyed and no longer usable'.format(S))
                elif O_4 == 'Potion':
                  print('Punch_OfDestruction is uselss against a potion')
            else:
                if (D_4_C == Satan['Storm_Bringer'] or (Satan['Satan_hp'] > 500)) and (O_4 in USer):
                    if O_4 != 'Shield' and H_1_C != Picked_Hero[Protect]:
                        Your_Health['Hp'] -= Satan['Storm_Bringer']
                        Picked_Hero[Hp] -= Satan['Storm_Bringer']
                    elif O_4 != 'Shield' and H_1_C == Picked_Hero[Protect]:
                      Your_Health['Hp'] -= Satan['Storm_Bringer']
                      if Picked_Hero[Protect] >= Satan['Storm_Bringer']:  
                        print('The {} blocks Satans damage'.format(Hname))
                      elif Picked_Hero[Protect] < Satan['Storm_Bringer']:
                        Picked_Hero[Hp] -= ((Satan['Storm_Bringer'] - Picked_Hero[Protect]) / 2)
                    elif O_4 == 'Shield' and H_1_C != Picked_Hero[Protect]:
                      Your_Health['Hp'] -= Satan['Storm_Bringer']
                      if Picked_Hero[Protect] >= Satan['Storm_Bringer']:  
                        print('You block Satans damage')
                      elif Picked_Hero[Protect] < Satan['Storm_Bringer']:
                        Picked_Hero[Hp] -= ((Satan['Storm_Bringer'] - Picked_Hero[Protect]) / 2)
                    elif O_4 == 'Shield' and H_1_C == Picked_Hero[Protect]:
                        if Your_Shield[S] >= Satan['Storm_Bringer'] and Picked_Hero[Protect] >= Satan['Storm_Bringer']: 
                            print('You and the Hero blocks Satans damage')
                        elif Your_Shield[S] < Satan['Storm_Bringer'] and Picked_Hero[Protect] >= Satan['Storm_Bringer']:
                            Your_Health['Hp'] -= ((Satan['Storm_Bringer'] - Your_Shield[S]) / 2)
                            print('{} was able to block Satans damage'.format(Hname))
                        elif Your_Shield[S] >= Satan['Storm_Bringer'] and Picked_Hero[Protect] < Satan['Storm_Bringer']:
                          Picked_Hero[Hp] -= ((Satan['Storm_Bringer'] - Picked_Hero[Protect]) / 2)
                          print('You were able to block Satans damage')
                        elif Your_Shield[S] < Satan['Storm_Bringer'] and Picked_Hero[Protect] >= Satan['Storm_Bringer']:
                          Your_Health['Hp'] -= ((Satan['Storm_Bringer'] - Your_Shield[S]) / 2)
                          Picked_Hero[Hp] -= ((Satan['Storm_Bringer'] - Picked_Hero[Protect]) / 2)
    
                    # ATTACK OPTIONS FOR YOU
                if O_4 == 'Weapon':
                    if (D_4_C == Satan['Storm_Bringer'] or Satan['Satan_hp'] > 0) and (O_4 in USer):
                        Satan['Satan_hp'] -= Your_Weapon[W]
                    elif D_4_C == Satan['Grab']:
                        if Satan['Grab'] < Your_Weapon[W]:
                            Satan['Satan_hp'] -= Your_Weapon[W] - Satan['Grab']
                        elif Satan['Grab'] >= Your_Weapon[W]:
                            print('Satan negated your attack')
                          
                    #  ATTACK OPTION FOR HERO
                if H_1_C == Picked_Hero[Slay] and (O_4 in USer):
                    if (D_4_C == Satan['Storm_Bringer'] or Satan['Satan_hp'] > 0):
                        Satan['Satan_hp'] -= Picked_Hero[Slay]
                    elif D_4_C == Satan['Grab']:
                        if Satan['Grab'] < Picked_Hero[Slay]:
                            Satan['Satan_hp'] -= Picked_Hero[Slay] - Satan['Grab']
                        elif Satan['Grab'] >= Picked_Hero[Slay]:
                            print('Satan negated the Heroes attack')


            # SHIELDS FOR ALL

        if O_4 == 'Shield' and D_4_C == Satan['Grab'] and H_1_C == Picked_Hero[Protect]:
            print('Nothing happened')

        # GAME OVER

    if Your_Health['Hp'] <= 0:
        print('your health is now {}, you have died'.format(Your_Health['Hp']))
        break
    elif Satan['Satan_hp'] <= 0:
        print('\nSatan: I can not believe you killed me.')
        print('You have defeated Satan')


      #print that doub curse when he dies
    print('\nSatan: you are now cursed!!! ... its the affect of killing me. How do you feel?')
    input('Press enter to continue')
    print('\nPerhaps it raises a slight level of concern.... Eugh.\n{}: that was the last of him, Adventurer {} are you ok?'.format(Hname, name))
    input('Press enter to continue')
  
      # good ending
    
    if reluctance >= 2:
      print('\nYou feel like your going to throw up. You stop. You realize your goal DESTROY THE UNDERWORLD. You snap out of it.\nYou: I am ok.')
      input('Press enter to continue')
      
      print('\nYou and your companion return from traversing through the underworld.\n{}: we got our revenge for the Shield Hero. I do not know why it is raining.\n(In fact it was not raining)'.format(Hname))
      input('Press enter to continue')
      
      print('\nThe sun goes over the mountains and below the horizon. You fall asleep from the long journey.')
      input('Press enter to continue')
      
      print('\nYou wake up. Walk outside and see the sun in the sky again.\{} thank you again Adventurer {} you have saved the Earth'.format(Hname, name)) 
      input('Press enter to continue')
      
      print('\nYou: your welcome however there is still more for me to do. There are still evil spirits that roam the land.\n{}: again I can thank you enough and good luck on your next journey'.format(Hname))
      input('Press enter to continue')
      print('\nYou chose the Good Ending')
        # Bad Ending
    elif reluctance < 2: 
      print('\n{} Hey something does not feel right... I need to clense more. There should be no more heroes. Something is burning in me internally. Nothing deserves to live.'.format(Hname))
      input('Press enter to continue')
      
      print('\n ... ')
      input('Press enter to continue')
      
      print('\nyou are now on the eve of destruction... ')
      input('Press enter to continue')
      
      print('\nThis curse now takes a toll of your sanity. I Just killed Satan, but, but, I must become a DEE--MMM--OOOOOOO--NN.')
      input('Press enter to continue')
      
      print('\nAs this new found excitement grows your inner demons take control. You feel the urge to harm others to fuel your insatiable blood lust. You murder {}. What is next?'.format(Hname))
      input('Press enter to continue')

      print('\nTh--e Ear--thhhhhhhsss is next')
      input('Press enter to continue')

      print('\n')
      input('Press enter to continue')
      
      print('\nYou chose the bad ending')
      input('Press enter to continue')

    Choice = input('\nGame Over.\nWould You like to play again?(y, n)')
    