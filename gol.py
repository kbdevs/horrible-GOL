import os
import time
os.system('clear')

game_array = [0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,
              0,0,1,1,0,0,0,0,0,
              0,0,1,1,0,0,0,0,0,
              0,0,0,0,1,1,0,0,0,
              0,0,0,0,1,1,0,0,0,
              0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0]

def render_game_state(game_array):
    visible_counter = 0
    for i in range(len(game_array)):
        if i % 9 == 0:
            print()
        if game_array[i] == 0:
            print("□", end=" ")
        else:
            visible_counter += 1
            print("■", end=" ")
    return visible_counter > 0

def game_logic(array):
    temp_array = array.copy()
    for index in range(len(array)):
        count = 0
        if index % 9 != 8 and index + 1 < len(array) and array[index + 1] == 1:
            count += 1
        if index % 9 != 0 and index - 1 >= 0 and array[index - 1] == 1:
            count += 1
        if index + 8 < len(array) and array[index + 8] == 1:
            count += 1
        if index + 9 < len(array) and array[index + 9] == 1:
            count += 1
        if index + 10 < len(array) and array[index + 10] == 1:
            count += 1
        if index - 8 >= 0 and array[index - 8] == 1:
            count += 1
        if index - 9 >= 0 and array[index - 9] == 1:
            count += 1
        if index - 10 >= 0 and array[index - 10] == 1:
            count += 1
        if array[index] == 0 and count >= 3:
            temp_array[index] = 1
        if array[index] == 1 and count <= 1:
            temp_array[index] = 0
        if array[index] == 1 and count >= 4:
            temp_array[index] = 0
        if array[index] == 1 and (count == 3 or count == 2):
            temp_array[index] = 1
    return temp_array

visible = True

while True:
    visible = render_game_state(game_array)
    game_array = game_logic(game_array)
    time.sleep(0.5)
    print("\n")
    if not visible:
        break

