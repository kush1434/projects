import random
import sys
map = [['-','-','-','-','-'],
       ['-','-','-','-','-'],
       ['-','-','-','-','-'],
       ['-','-','-','-','-'],
       ['-','-','-','-','-']]
def see_map():
    for row in map:
        for x in row:
            print(x,end='')
        print()
x_p = random.randint(0,4)
y_p = random.randint(0,4)
(map[y_p])[x_p] = 'P'
player_cords = [y_p,x_p]
def random_index(excluded_index,t_1 = None, t_2 = None, t_3 = None):
    while True:
        x = random.randint(0,4)
        y = random.randint(0,4)
        item = [y,x]
        if item != excluded_index and item != t_1 and item != t_2 and item != t_3:
            return item
trap_1 = random_index(player_cords)
trap_2 = random_index(player_cords,trap_1)
trap_3 = random_index(player_cords,trap_1,trap_2)
treasure = random_index(player_cords,trap_1, trap_2, trap_3)
def trap_encounter():
    return player_cords in [trap_1,trap_2,trap_3]
def treasure_encounter():
    return player_cords == treasure
def treasure_radar(current_position):
    distance = abs(current_position[0]-treasure[0]) + abs(current_position[1]-treasure[1])
    if distance == 1:
        return 'Very Hot'
    elif distance == 2:
        return 'Hot'
    elif distance == 3:
        return 'Warm'
    elif distance <= 4:
        return 'Cold'
def main():
    move_cnt = 0
    covered_cords = []
    while True:
        old_cords = player_cords.copy()
        see_map()
        player_direction = input('Enter where you would like your to move(left, right, down, up) or to exit(exit): ')
        try:
            if player_direction.lower() == 'left':
                if old_cords[1] == 0:
                    raise IndexError
                player_cords[1] -= 1
                if player_cords in covered_cords:
                    player_cords[1] += 1
                    raise Exception
                covered_cords.append(old_cords)
                (map[old_cords[0]])[old_cords[1]] = '-'
                (map[player_cords[0]])[player_cords[1]] = 'P'
                move_cnt += 1
            elif player_direction.lower() == 'right':
                if old_cords[1] == 4:
                    raise IndexError
                player_cords[1] +=1
                if player_cords in covered_cords:
                    player_cords[1] -=1
                    raise Exception
                covered_cords.append(old_cords)
                (map[old_cords[0]])[old_cords[1]] = '-'
                (map[player_cords[0]])[player_cords[1]] = 'P'
                move_cnt += 1
            elif player_direction.lower() == 'up':
                if old_cords[0] == 0:
                    raise IndexError
                player_cords[0] -= 1
                if player_cords in covered_cords:
                    player_cords[0] += 1
                    raise Exception
                covered_cords.append(old_cords)
                (map[old_cords[0]])[old_cords[1]] = '-'
                (map[player_cords[0]])[player_cords[1]] = 'P'
                move_cnt += 1
            elif player_direction.lower() == 'down':
                if old_cords[0] == 4:
                    raise IndexError
                player_cords[0] += 1
                if player_cords in covered_cords:
                    player_cords[0] -= 1
                    raise Exception
                covered_cords.append(old_cords)
                (map[old_cords[0]])[old_cords[1]] = '-'
                (map[player_cords[0]])[player_cords[1]] = 'P'
                move_cnt += 1
            elif player_direction.lower() == 'exit':
                print('Thank you for playing!')
                sys.exit()
            else:
                print()
                print('Invalid Direction. Try Again')
                print()
                continue
        except IndexError:
            print()
            print('Unable to move that direction. Try Again')
            print()
            continue
        except Exception:
            print()
            print('Position Already Covered. Please Choose Another.')
            print()
            continue
        if trap_encounter():
            see_map()
            print('You ran into a trap. Game Over.')
            print('Number of Moves Taken:',move_cnt)
            break
        elif treasure_encounter():
            see_map()
            print('You found the treasure. You Win!')
            print('Number of Moves Taken:',move_cnt)
            break
        print()
        print('Treasure Radar:',treasure_radar(player_cords))
        print()
if __name__ == "__main__":
    main()
