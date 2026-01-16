import time
import os

pokemon_original = [
    {"name": "Greninja", "evolution": 2, "gen": 6, "hp": 72, "type": "Water"},
    {"name": "Bulbasaur", "evolution": 0, "gen": 1, "hp": 45, "type": "Grass"},
    {"name": "Lucario", "evolution": 1, "gen": 4, "hp": 70, "type": "Fighting"},
    {"name": "Pikachu", "evolution": 1, "gen": 1, "hp": 35, "type": "Electric"},
    {"name": "Gardevoir", "evolution": 2, "gen": 3, "hp": 68, "type": "Psychic"},
    {"name": "Charmander", "evolution": 0, "gen": 1, "hp": 39, "type": "Fire"},
    {"name": "Froakie", "evolution": 0, "gen": 6, "hp": 41, "type": "Water"},
    {"name": "Ivysaur", "evolution": 1, "gen": 1, "hp": 60, "type": "Grass"},
    {"name": "Zoroark", "evolution": 1, "gen": 5, "hp": 60, "type": "Dark"},
    {"name": "Charizard", "evolution": 2, "gen": 1, "hp": 78, "type": "Fire"},
    {"name": "Riolu", "evolution": 0, "gen": 4, "hp": 40, "type": "Fighting"},
    {"name": "Empoleon", "evolution": 2, "gen": 4, "hp": 84, "type": "Water"},
    {"name": "Frogadier", "evolution": 1, "gen": 6, "hp": 54, "type": "Water"},
    {"name": "Blaziken", "evolution": 2, "gen": 3, "hp": 80, "type": "Fire"},
    {"name": "Eevee", "evolution": 0, "gen": 1, "hp": 55, "type": "Normal"},
    {"name": "Sylveon", "evolution": 1, "gen": 6, "hp": 95, "type": "Fairy"},
    {"name": "Tyranitar", "evolution": 2, "gen": 2, "hp": 100, "type": "Rock"},
    {"name": "Abra", "evolution": 0, "gen": 1, "hp": 25, "type": "Psychic"}
]
pokemon_type_order = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
]
# Type ranking dictionary
type_rank = {t: i for i, t in enumerate(pokemon_type_order)} # Should display as {'Normal': 0, 'Fire': 1, 'Water': 2, ... , 'Fairy': 17}
sorted_flag = 0
pokemon_sorted_by_evolution = []
pokemon_sorted_by_generation = []
pokemon_sorted_by_hp = []
pokemon_sorted_by_type = []
pokemon_sorted_by_name = []
pokemon_final_sorted_order = []
comp = [] # Records the number of comparisons for each sort
swaps = [] # Records the number of swaps for each sort 
iter = [] # Records the number of passes/iterations for each sort
dur = [] # Records the duration time for each sort

def main_menu():
    while True:
        clear_screen()
        print("\nPOKEDEX PROGRAM\n")
        print("(a) View original order of pokemons")
        print("(b) Sort and view the sorted pokemons")
        print("(c) View algorithm analysis")
        print("(Enter) Exit program\n")
        choice = input("Select an option: ")
        if choice == "a":
            display_pokemons("ORIGINAL ORDER", pokemon_original)
        elif choice == "b":
            sorting_pokemon()
        elif choice == "c":
            show_analysis()
        elif choice == "":
            print("\nExiting program", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            break
        else:
            invalid_choice()

def prompt_continue():
    print("\nPress the Enter key to go back...", end="")
    input()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def invalid_choice():
    print("\nInvalid choice. Please try again", end="")
    for _ in range(3):
        time.sleep(0.5)
        # Pause the terminal for 0.5 seconds
        print(".", end="", flush=True)
        # flush=True is used to push the dot from buffer to screen immediately
        # Because print() doesn't flush immediately by default, it needs to detect a newline(\n) or buffer full
    time.sleep(0.5)

def sorting_pokemon():
    # Intializing "global" variables for this function to access
    global sorted_flag, pokemon_sorted_by_evolution, pokemon_sorted_by_generation, pokemon_sorted_by_hp, pokemon_sorted_by_name, pokemon_sorted_by_type, pokemon_final_sorted_order
    while True:
        clear_screen()
        live_choice = 0 # 0 = no live demo, 1 = live demo
        print("\nSORTING OPTIONS\n")
        print("(a) No Live Demo of Bubble Sort")
        print("(b) Live Demo of Bubble Sort")
        print("(c) Final sorted order of Pokemons")
        print("(Enter) Go back to main menu\n")
        choice = input("Select an option: ")
        if choice == "a":
            break
        elif choice == "b":
            live_choice = 1
            break
        elif choice == "c":
            if len(pokemon_final_sorted_order) == 0:
                pokemon_final_sorted_order = sort_final_order()
            display_pokemons("FINAL ORDER", pokemon_final_sorted_order)
            continue
        elif choice == "":
            return
        else:
            invalid_choice()
    if live_choice == 0:
        if sorted_flag == 0:
            time_taken, pokemon_sorted_by_evolution = algo_dur_calc("evolution")
            dur.append(time_taken)
            time_taken, pokemon_sorted_by_generation = algo_dur_calc("gen")
            dur.append(time_taken)
            time_taken, pokemon_sorted_by_hp = algo_dur_calc("hp")
            dur.append(time_taken)
            time_taken, pokemon_sorted_by_type = algo_dur_calc("type")
            dur.append(time_taken)
            time_taken, pokemon_sorted_by_name = algo_dur_calc("name")
            dur.append(time_taken)
            sorted_flag = 1 # To indicate that sorting has been done
            print() # \n\n
    while True:
        clear_screen()
        print(f"\nBUBBLE SORT {'(NO LIVE DEMO)' if live_choice == 0 else '(LIVE DEMO)'}\n")
        # BUBBLE SORT (LIVE DEMO) live_choice == 1
        # BUBBLE SORT (NO LIVE DEMO) live_choice == 0
        print("View the sorted pokemons by:")
        print("(a) Evolution Stage (ascending)")
        print("(b) Generation (ascending)")
        print("(c) HP (lowest to highest)")
        print("(d) Pokemon Type")
        print("(e) Name (A-Z)")
        print("(Enter) Go back to main menu\n")
        choice = input("Select an option: ")
        # Nested "if-else" statements to check if user wants live demo or not
        if choice == "a":
            if live_choice == 0:
                display_pokemons("EVOLUTION STAGE", pokemon_sorted_by_evolution)
                continue
            else:
                live_bubble_sort(pokemon_original[:], "evolution")
                continue
        elif choice == "b":
            if live_choice == 0:
                display_pokemons("GENERATION", pokemon_sorted_by_generation)
                continue
            else:
                live_bubble_sort(pokemon_original[:], "gen")
                continue
        elif choice == "c":
            if live_choice == 0:
                display_pokemons("HP", pokemon_sorted_by_hp)
                continue
            else:
                live_bubble_sort(pokemon_original[:], "hp")
                continue
        elif choice == "d":
            if live_choice == 0:
                display_pokemons("TYPE", pokemon_sorted_by_type)
                continue
            else:
                live_bubble_sort(pokemon_original[:], "type")
                continue
        elif choice == "e":
            if live_choice == 0:
                display_pokemons("NAME", pokemon_sorted_by_name)
                continue
            else:
                live_bubble_sort(pokemon_original[:], "name")
                continue
        elif choice == "":
            return
        else:
            invalid_choice()

# Algorithm duration calculation function
def algo_dur_calc(which):
    durlist = []
    test = 1
    # Warm-up run
    bubble_sort_pokemon(which, test)
    # Bubble sort timing over 100 runs
    for _ in range(100):
        start = time.perf_counter()
        bubble_sort_pokemon(which, test)
        end = time.perf_counter()
        durlist.append(end - start)
    test = 0
    # Getting the average of duration of 100 runs
    avg_time = sum(durlist) / len(durlist)
    # One last run to save the comparisons, swaps, and iterations
    sorted_list = bubble_sort_pokemon(which, test)
    return avg_time, sorted_list

def bubble_sort_pokemon(which, being_tested):
    temp_list = pokemon_original[:]
    comp_count = 0
    swap_count = 0
    iter_count = 0
    n = len(temp_list)
    # Bubble sort algorithm
    for i in range(n):
        iter_count += 1
        swapped = False
        for j in range(0, n - i - 1):
            comp_count += 1
            left = type_rank[temp_list[j]["type"]] if which == "type" else temp_list[j][which]
            right = type_rank[temp_list[j+1]["type"]] if which == "type" else temp_list[j+1][which]
            # Longer version:
            # if which == "type":
            #     left = type_rank[temp_list[j]["type"]]
            #     right = type_rank[temp_list[j+1]["type"]]
            # else:
            #     left = temp_list[j][which]
            #     right = temp_list[j+1][which]
            if left > right:
                swap_count += 1
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                swapped = True
        if not swapped:
            break
    if being_tested == 0:
        comp.append(comp_count)
        swaps.append(swap_count)
        iter.append(iter_count)
        return temp_list
    return

def sort_final_order():
    # Category Order = ["evolution", "gen", "hp", "type", "name"]
    global pokemon_final_sorted_order
    temp_list = pokemon_original[:]
    n = len(temp_list)
    # Sorting the Final order
    for i in range(n):
        for j in range (0, n - i - 1):
            if temp_list[j]["evolution"] > temp_list[j+1]["evolution"]:
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
            elif temp_list[j]["evolution"] == temp_list[j+1]["evolution"]:
                if temp_list[j]["gen"] > temp_list[j+1]["gen"]:
                    temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                elif temp_list[j]["gen"] == temp_list[j+1]["gen"]:
                    if temp_list[j]["hp"] > temp_list[j+1]["hp"]:
                        temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                    elif temp_list[j]["hp"] == temp_list[j+1]["hp"]:
                        if type_rank[temp_list[j]["type"]] > type_rank[temp_list[j+1]["type"]]:
                            temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                        elif type_rank[temp_list[j]["type"]] == type_rank[temp_list[j+1]["type"]]:
                            if temp_list[j]["name"] > temp_list[j+1]["name"]:
                                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
    return temp_list

def display_pokemons(which, pokemon):
    label = "POKEDEX DATA BY" if which == "ORIGINAL ORDER" else "SORTED POKEDEX DATA BY"
    print(f"\n{label} {which}\n")
    print(f"{'Name':<12} {'Evol':<6} {'Gen':<4} {'HP':<4} {'Type'}")
    for p in pokemon:
        if which == "TYPE":
            print(f"{p['name']:<12} {p['evolution']:<6} {p['gen']:<4} {p['hp']:<4} {p['type'] } (rank {type_rank[p['type']]})")
        else:
            print(f"{p['name']:<12} {p['evolution']:<6} {p['gen']:<4} {p['hp']:<4} {p['type']}")
    prompt_continue()

def show_analysis():
    if sorted_flag == 0:
        print("Pokemons aren't sorted yet! Please sort them first via non-live demo to view analysis (Option b then Option a).")
        prompt_continue()
        return
    print("\nBUBBLE SORT: ALGORITHM ANALYSIS\n")
    print(f"{'Sort Type':<18} {'Comparisons':<13} {'Swaps':<7} {'Iterations':<11} {'Duration (Average of 100 runs)'}")
    sort_types = ["Evolution Stage", "Generation", "HP", "Pokemon Type", "Name"]
    for i in range(len(sort_types)):
        print(f"{sort_types[i]:<18} {comp[i]:<13} {swaps[i]:<7} {iter[i]:<11} {dur[i]:<.6f} seconds")
    avg_comp = sum(comp)/len(comp)
    avg_swaps = sum(swaps)/len(swaps)
    avg_iter = sum(iter)/len(iter)
    avg_dur = sum(dur)/len(dur)
    print(f"\nAverage Comparisons: {avg_comp:.2f}")
    print(f"Average Swaps: {avg_swaps:.2f}")
    print(f"Average Iterations/Passes: {avg_iter:.2f}")
    print(f"Average Duration: {avg_dur:.6f} seconds")
    prompt_continue()

def live_bubble_sort(temp_list, which):
    n = len(temp_list)
    comp_count = 0
    swap_count = 0
    iter_count= 0
    skip_demo = 0
    print(f"\nLIVE BUBBLE SORT BY POKEMONS' {which.upper()}")
    print("Left = j\nRight = j+1\n|✓| = sorted already (locked)")
    print("Starting the demo", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("")
    time.sleep(0.5)
    input("Press Enter to proceed...")
    # Bubble Sort Algorithm with live demo
    for i in range(n):
        iter_count += 1
        swapped = False
        for j in range(0, n - i - 1):
            comp_count += 1
            # Determine "left" and "right" values based on sorting criteria
            if which == "type":
                left = type_rank[temp_list[j]["type"]] # determining the rank of "type" based on type_rank dictionary (from pokemon_type_order list) (e.g., "Water" becomes 2, "Fire" becomes 1)
                right = type_rank[temp_list[j+1]["type"]]
                left_display = temp_list[j]["type"]
                right_display = temp_list[j+1]["type"]
            elif which == "name":
                left = temp_list[j]["name"] # string comparison for names instead of integers (e.g., "Pikachu" < "Bulbasaur")
                right = temp_list[j+1]["name"]
                left_display = left
                right_display = right
            else:
                left = temp_list[j][which] # integer comparison for other criteria (e.g., "evolution", "gen", "hp")
                right = temp_list[j+1][which]
                left_display = left
                right_display = right
            # Perform comparison and swaps if necessary
            if left > right:
                swap_count += 1
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                action = "swap"
                swapped = True
            else:
                action = "no swap"
            clear_screen()
            print(f"\n{'-'*15} COMPARISON {'-'*15}")
            if which == "type":
                print(f"(j)Left = {left_display} (rank {left}) > (j+1)Right = {right_display} (rank {right})\nAction → {action}\n")
            else:
                print(f"(j)Left = {left_display} > (j+1)Right = {right_display}\nAction → {action}\n")
            print("-" * 15 + " UPDATED LIST " + "-" * 15)
            if which == "name":
                print(f"{'Index':<7}{'j/j+1':<7} Name")
            else:
                print(f"{'Index':<7}{'j/j+1':<7} {which:<10} Name")
            for idx, p in enumerate(temp_list):
                marker = ""
                if idx == j:
                    marker = "j"
                elif idx == j + 1:
                    marker = "j+1"
                elif idx >= n - i:
                    marker = "|✓|"
                if which == "type": # display "type" on string data type (e.g., "Water", "Fire") instead of their integers
                    value = p["type"]
                elif which == "name": # display "name" on string data type (e.g., "Pikachu", "Bulbasaur") instead of their integers
                    value = p["name"]
                else:
                    value = p[which]
                # To prevent duplication of Name if which == name
                if which == "name":
                    print(f"{idx:<7}{marker:<7} {value:<10}")
                else:
                    print(f"{idx:<7}{marker:<7} {str(value):<10} {p['name']}")
            print("Comparison:", comp_count)
            print("Swaps:", swap_count)
            print("Pass (iteration):", iter_count)
            print("\"swapped\" status:", swapped)
            print("Remaining comparison before next pass:", n - i - j - 2)
            if skip_demo == 0:
                user_input = input("Enter (0) to skip the demo or simply press (Enter) to proceed...")
                if user_input == "0":
                    skip_demo = 1
        if not swapped:
            print("The 'swapped' status remained False during the entire pass.")
            print("Exiting the bubble sort", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            time.sleep(0.5)
            print("")
            break
    print("Sorting complete!")
    print(f"{'-' * 15} FINAL DETAILS OF THE BUBBLE SORT OF POKEMONS' {which.upper()} {'-' * 15}")
    print("Comparison:", comp_count)
    print("Swaps:", swap_count)
    print("Pass (iteration):", iter_count)
    prompt_continue()

main_menu()