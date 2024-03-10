import random
import time

# Left off adding the conditions for all the new moves to all of the movements -.-

class RandomNumber:
    def __init__(self):
        pass

    def create_random_number(self):
        return round(random.random() * 2)

    def create_random_number_for_attack(self):
        return round(random.random() * 5)

    def create_random_number_for_health(self, num):
        return round(random.random() * num)


class Player:
    def __init__(self, hp):
        self.hp = hp
        self.energy = 100
        


class Attacks:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Dodges:
    def __init__(self, name):
        self.name = name


dodge_left = Dodges('Dodges Left')
dodge_right = Dodges('Dodges Right')
dodge_low = Dodges('Dodges Low')


attack_left_hook = Attacks('Left Hook', 4)
attack_right_hook = Attacks('Right Hook', 5)
attack_straight = Attacks('Straight Punch', 3)
attack_left_kick = Attacks('Left Kick', 9)
attack_right_kick = Attacks('Right Kick', 7)
attack_low_kick = Attacks('Low Kick', 15)


class Battle:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.attacks = [attack_left_hook, attack_right_hook, attack_straight,
                        attack_left_kick, attack_left_kick, attack_low_kick]
        self.dodges = [dodge_left, dodge_right, dodge_low]
        self.round = 1

    def player_move_attack(self):
        self.round += 1
        player_one_move_attack = self.attacks[new_ran.create_random_number_for_attack(
        )]

        return player_one_move_attack

    def player_two_move_attack(self):
        self.round += 1
        print(self.round)
        player_two_move_attack = self.attacks[new_ran.create_random_number_for_attack(
        )]
        return player_two_move_attack

    def player_two_move_dodge(self):
        player_two_move = self.dodges[new_ran.create_random_number()]
        return player_two_move

    def player_one_move_dodge(self):
        player_one_move = self.dodges[new_ran.create_random_number()]
        return player_one_move
    def display_player_energy(self):
        print(f'Player Energy: {self.player_one.energy}')
    
    def player_one_move_condition_choice(self, player_one_move, player_two_move):
        def print_out_moves_and_HP_attack():
            print('\n')
            print(
                f'Player One throws a {player_one_move.name} enemy {player_two_move.name} taking {player_one_move.damage} damage.')
            print(f'Player Two Health: {self.player_two.hp}')
            print('\nChoose a Dodge')
        def print_out_moves_and_HP_dodge():
            print('\n')
            print(
                f'Player One throws a {player_one_move.name} enemy {player_two_move.name} taking evading damage.')
            print(f'Player Two Health: {self.player_two.hp}')
            print('\nChoose a Dodge')
            
        player_one_damage = player_one_move.damage
        player_two_move_name = player_two_move.name
        self.player_two.current_defense = player_two_move_name
        if player_one_move == self.attacks[0] and player_two_move_name == self.dodges[0].name:
            
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[0] and player_two_move_name == self.dodges[1].name:
            
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[0] and player_two_move_name == self.dodges[2].name:
            self.player_two.hp -= player_one_damage
            
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[1] and player_two_move_name == self.dodges[0].name:
            self.player_two.hp -= player_one_damage
            
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[1] and player_two_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[1] and player_two_move_name == self.dodges[2].name:
            self.player_two.hp -= player_one_damage
            
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[2] and player_two_move_name == self.dodges[0].name:
            self.player_two.hp -= player_one_damage
           
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[2] and player_two_move_name == self.dodges[1].name:
            self.player_two.hp -= player_one_damage
            
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[2] and player_two_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[3] and player_two_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[3] and player_two_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[3] and player_two_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[4] and player_two_move_name == self.dodges[0].name:
            self.player_two.hp -= player_one_damage
           
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[4] and player_two_move_name == self.dodges[1].name:
            self.player_two.hp -= player_one_damage
          
            print_out_moves_and_HP_attack()
        elif player_one_move == self.attacks[4] and player_two_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[5] and player_two_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[5] and player_two_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_one_move == self.attacks[5] and player_two_move_name == self.dodges[2].name:
            self.player_two.hp -= player_one_damage
           
            print_out_moves_and_HP_attack()

    def player_two_move_condition(self):
        def print_out_moves_and_HP_attack():
            print('\n')
            print(
                f'Player Two throws a {player_two_move.name} enemy {player_one_move.name} taking {player_two_move.damage} damage.')
            print(f'Player Two Health: {self.player_two.hp}')
            print('\nChoose a Dodge')
        def print_out_moves_and_HP_dodge():
            print('\n')
            print(
                f'Player Two throws a {player_two_move.name} enemy {player_one_move.name} taking evading damage.')
            print(f'Player One Health: {self.player_one.hp}')
            print('\nChoose a Dodge')
        player_two_move = self.player_two_move_attack()
        player_one_move = self.player_one_move_dodge()
        player_one_move_name = player_one_move.name
        self.player_one.current_defense = player_one_move_name
        player_two_damage = player_two_move.damage
        player_two_move_name = player_two_move.name
        self.player_two.current_defense = player_two_move_name
        if player_one_move == self.attacks[0] and player_two_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[0] and player_two_move_name == self.dodges[1].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[0] and player_two_move_name == self.dodges[2].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[1] and player_two_move_name == self.dodges[0].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[1] and player_two_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[1] and player_two_move_name == self.dodges[2].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[2] and player_two_move_name == self.dodges[0].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[2] and player_two_move_name == self.dodges[1].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[2] and player_two_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[3] and player_two_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[3] and player_two_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[3] and player_two_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[4] and player_two_move_name == self.dodges[0].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[4] and player_two_move_name == self.dodges[1].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[4] and player_two_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[5] and player_two_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[5] and player_two_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[5] and player_two_move_name == self.dodges[2].name:
            self.player_two.hp -= player_two_damage
            print_out_moves_and_HP_attack()
    def battle_display_round(self):
        print(f'Round: {self.round}')

    def player_two_move_condition_choice(self, player_one_move, player_two_move):
        def print_out_moves_and_HP_attack():
            print('\n')
            print(
                f'Player Two throws a {player_two_move.name} enemy {player_one_move.name} taking {player_two_move.damage} damage.')
            print(f'Player One Health: {self.player_one.hp}')
            print('\nChoose a Dodge')
        def print_out_moves_and_HP_dodge():
            print('\n')
            print(
                f'Player Two throws a {player_two_move.name} enemy {player_one_move.name} taking evading damage.')
            print(f'Player  One Health: {self.player_one.hp}')
            print('\nChoose a Dodge')
        player_two_damage = player_two_move.damage
        player_one_move_name = player_one_move.name
        self.player_one.current_defense = player_one_move_name
        if player_two_move == self.attacks[0] and player_one_move_name == self.dodges[0].name:
            self.player_one.current_defense = player_one_move_name
        elif player_two_move == self.attacks[0] and player_one_move_name == self.dodges[1].name:

            self.player_one.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[0] and player_one_move_name == self.dodges[2].name:

            self.player_one.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[1] and player_one_move_name == self.dodges[0].name:

            self.player_one.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[1] and player_one_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[1] and player_one_move_name == self.dodges[2].name:

            self.player_one.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[2] and player_one_move_name == self.dodges[0].name:

            self.player_one.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[2] and player_one_move_name == self.dodges[1].name:

            self.player_one.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[2] and player_one_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[3] and player_one_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[3] and player_one_move_name == self.dodges[1].name:

            self.player_one.hp -= player_two_damage
            print_out_moves_and_HP_attack()
        elif player_two_move == self.attacks[3] and player_one_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[4] and player_one_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[4] and player_one_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[4] and player_one_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[5] and player_one_move_name == self.dodges[0].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[5] and player_one_move_name == self.dodges[1].name:
            print_out_moves_and_HP_dodge()
        elif player_two_move == self.attacks[5] and player_one_move_name == self.dodges[2].name:
            print_out_moves_and_HP_dodge()
    
    def fight_enemy(self):
        self.round += 1
        if self.player_one.hp <= 0 or self.player_two.hp <= 0:
            return
        if self.player_one.hp > 0 or self.player_two.hp > 0:
            self.player_one_move_condition_choice(self.attacks[new_ran.create_random_number_for_attack()], self.dodges[new_ran.create_random_number()])
            self.player_two_move_condition()
        if self.player_one.hp <= 0:
            print('Player Two has won')
        elif self.player_two.hp <= 0:
            print('Player One has won.')
        self.battle_display_round()
        self.display_player_energy()
        self.fight_enemy()
    def use_energy(self, amount):
        self.player_one.energy -= amount


# Running program.
new_ran = RandomNumber()


class CondensedBattleFunctions:
    def __init__(self):
        pass

    def AttacksCondensedFightChoiceAttack(self, new_battle, user_move_choice):
        player_choice_attack = new_battle.attacks[user_move_choice]
        enemy_choice_dodge = new_battle.player_two_move_dodge()
        new_battle.player_one_move_condition_choice(
            player_choice_attack, enemy_choice_dodge)

    def DodgesCondensedFightChoiceDodges(self, new_battle, user_move_choice):
        player_choice_dodges = new_battle.dodges[user_move_choice - 1]
        enemy_choice_attack = new_battle.player_two_move_attack()
        new_battle.player_two_move_condition_choice(
            player_choice_dodges, enemy_choice_attack)
        print('\n')


new_condensed_battle_functions = CondensedBattleFunctions()


class BattleInterface:
    def __init__(self):
        self.battle_on_recursion = False
        self.battle_on_incremental = False
        self.battle_on_choice = False

    def print_out_moves_and_HP_attack(self, new_battle, index_of_attack):
        print('\n')
        print(
            f'Round: {new_battle.round}. Player One throws a {new_battle.attacks[index_of_attack].name} enemy {new_battle.player_two.current_defense} taking {new_battle.attacks[index_of_attack].damage} damage.')
        print(f'Player Two Health: {new_battle.player_two.hp}')
       

    def print_out_moves_and_HP_dodge(self, new_battle, index_of_attack):
        print(
            f'\nPlayer two throws a {new_battle.attacks[index_of_attack].name} enemy evades the attack.')
        print(f'Player One Health: {new_battle.player_one.hp}')
        print('\n')
    

    def initiate_battle_interface(self):
        new_player = Player(new_ran.create_random_number_for_health(200))
        new_player_two = Player(new_ran.create_random_number_for_health(200))
        new_battle = Battle(new_player, new_player_two)
        new_battle.fight_enemy()
    def battle_display_energy(self, new_battle):
        print(f'Player Energy: {new_battle.player_one.energy}')
    
    def start_battle_interface(self):
        self.battle_on_recursion = True
        while self.battle_on_recursion:
            move = input(
                "Type 'Recursion' to have whole fight simulated, or 'Fight' by choice: ")
            if move.lower() == 'recursion':
                self.initiate_battle_interface()
                break
            elif move.lower() == 'fight':
                self.battle_on_choice = True
                new_player = Player(
                    new_ran.create_random_number_for_health(50) + 50)
                new_player_two = Player(
                    new_ran.create_random_number_for_health(50) + 50)
                new_battle = Battle(new_player, new_player_two)

                while self.battle_on_choice:
                    if new_battle.player_one.hp <= 0 or new_battle.player_two.hp <= 0:
                        print('Fight has concluded')
                        self.battle_on_choice = False
                    print('Choose an Attack by the list number.')
                    print(f'Energy Cost. Lhook = 3, Rhook = 4. Spunch = 5. Lkick = 7. Rkick = 6. Lkick = 5')
                    user_move_choice = int(input(
                        '0 - Left Hook. 1 - Right Hook. 2 - Straight Punch. 3 - Left Kick. 4 - Right Kick. 5 - Low kick : '))
                    
                    print(user_move_choice)
                    if user_move_choice == 0:  # Attack
                        new_battle.use_energy(4)                   
                        print('\n')
                        new_battle.battle_display_round()
                        new_battle.display_player_energy()
                        new_condensed_battle_functions.AttacksCondensedFightChoiceAttack(
                            new_battle, user_move_choice)
                        user_move_choice = int(
                            input('1 - Left Dodge. 2 - Right Dodge. 3 - Low Dodge: '))
                        new_condensed_battle_functions.DodgesCondensedFightChoiceDodges(
                            new_battle, user_move_choice)
                    elif user_move_choice == 1:  # Attack
                        new_battle.use_energy(5)
                        print('\n')
                        new_battle.battle_display_round()
                        new_battle.display_player_energy()
                        new_condensed_battle_functions.AttacksCondensedFightChoiceAttack(
                            new_battle, user_move_choice)
                        user_move_choice = int(
                            input('1 - Left Dodge. 2 - Right Dodge. 3 - Low Dodge: '))
                        new_condensed_battle_functions.DodgesCondensedFightChoiceDodges(
                            new_battle, user_move_choice)
                    elif user_move_choice == 2:  # attack
                        new_battle.use_energy(5)
                        new_battle.display_player_energy()
                        print('\n')
                        new_battle.battle_display_round()
                        new_battle.display_player_energy()
                        new_condensed_battle_functions.AttacksCondensedFightChoiceAttack(
                            new_battle, user_move_choice)
                        user_move_choice = int(
                            input('1 - Left Dodge. 2 - Right Dodge. 3 - Low Dodge: '))
                        new_condensed_battle_functions.DodgesCondensedFightChoiceDodges(
                            new_battle, user_move_choice)
                    elif user_move_choice == 3:  # attack
                        new_battle.use_energy(7)
                    
                        print('\n')
                        new_battle.battle_display_round()
                        new_battle.display_player_energy()
                        new_condensed_battle_functions.AttacksCondensedFightChoiceAttack(
                            new_battle, user_move_choice)
                        user_move_choice = int(
                            input('1 - Left Dodge. 2 - Right Dodge. 3 - Low Dodge: '))
                        new_condensed_battle_functions.DodgesCondensedFightChoiceDodges(
                            new_battle, user_move_choice)
                    elif user_move_choice == 4:  # attack
                        new_battle.use_energy(6)
                    
                        print('\n')
                        new_battle.battle_display_round()
                        new_battle.display_player_energy()
                        new_condensed_battle_functions.AttacksCondensedFightChoiceAttack(
                            new_battle, user_move_choice)
                        user_move_choice = int(
                            input('1 - Left Dodge. 2 - Right Dodge. 3 - Low Dodge: '))
                        new_condensed_battle_functions.DodgesCondensedFightChoiceDodges(
                            new_battle, user_move_choice)
                    elif user_move_choice == 5:  # attack
                        new_battle.use_energy(5)
                        print('\n')
                        new_battle.battle_display_round()
                        new_battle.display_player_energy()
                        new_condensed_battle_functions.AttacksCondensedFightChoiceAttack(
                            new_battle, user_move_choice)


            else:
                print('Please Enter Recursion or Go.')


# Starting
new_battle_interface = BattleInterface()
new_battle_interface.start_battle_interface()
