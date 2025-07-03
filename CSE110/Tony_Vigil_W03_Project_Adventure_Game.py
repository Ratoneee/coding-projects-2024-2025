#I added a secret text prompt so if the user inputs 'secret' at the start it will print a picture of a dog. I also added so intead of input text I use a typeriter effect so the text slowly reveals its self for added immersion I added diffrent endings to the game so the player can get diffrent endings for their actions in the game.
import time


def typewriter(text, delay=0.05):
    #Simulate typewriter effect with a small delay between characters
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#dog art for secret text prompt
dog_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣏⡽⠷⠾⠭⠍⠉⣯⣿⣶⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⣿⣦⣴⣤⣀⠀⠉⣛⠹⣮⡇⣿⣿⢶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⣴⣿⡯⠟⠀⠈⢀⠀⠹⡄⠙⣷⣿⣿⠶⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣴⣿⡟⠀⣰⣬⣿⣾⠗⠀⠀⠐⢯⠛⣧⠀⢘⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡴⠀⠙⠉⠉⠈⠀⠀⠀⠀⠀⠀⣼⣶⠾⢾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠻⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣠⣿⠙⣄⠾⠿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⡿⠥⠀⠀⢀⣴⠀⠀⠀⠀⠀⣨⠀⠴⠋⠀⠘⠁⠀⣠⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⣿⣧⣤⣯⣿⡿⠋⠀⠀⠀⣤⠞⠀⠀⠀⠀⠀⠀⠀⠀⠟⠁⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⠛⠁⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢀⣴⠀⠀⠀⠀⠀⠀⠀⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠹⡦⠀⣀⣴⠏⠀⠀⠀⠀⠀⠀⠀⣀⣿⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⠀⠀⠀⠀⠀⠀⠀⠳⠖⠉⠀⠀⠀⠀⠀⠀⠀⠁⠀⣴⠟⠩⠀⢠⣿⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠿⠀⠁⠀⠀⢀⣸⡯⠙⢷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠃⠀⢸⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢖⠀⠀⠀⠀⠀⠀⠀⠐⠚⠉⠀⠀⠀⠀⡴⡋⠀⠀⠀⠀⣦⡏⠀⠀⠀⣾⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢪⡞⠁⠀⠀⠀⠀⠁⠀⠀⠀⣶⠏⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡦⡌⠳⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⣻⣹⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠋⠀⠀⠀⠀⠀⠀⢀⣾⠀⠀⠀⠀⣾⠀⠹⢿⣿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⣆⠀⠟⠀⠀⠀⠀⠀⡾⠃⠀⢠⡠⠀⢠⣾⣾⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠀⠀⠀⣰⣿⣀⠀⠀⠀⠀⢹⡤⡄⠀⠀⠀⠀⣸⣿⡀⣶⣶⣷⣶⣿⣿⣿⣿⡟⠁
⠀⠀⠀⠀⠀⠀⣀⡠⠶⠋⣸⣗⠀⠀⢀⣿⣻⣿⡦⠤⠤⠤⠿⣷⠇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
⠀⣀⡴⠖⠋⠉⠉⢀⣀⡴⣿⡏⠀⢀⣸⡟⠛⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀
⠘⢿⣷⣤⡤⠶⠚⠋⠁⢀⡟⠀⠀⣾⣿⣁⣀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⠴⢞⡿⠀⠀⢴⡿⠋⠉⠉⠉⠛⠲⠶⠤⣤⣿⠀⠀⢰⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣠⣶⡊⠉⢀⣠⠞⠁⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢸⣯⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠉⠻⠶⣶⡟⠃⡴⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣿⣄⣾⣄⡷⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠁⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⡁⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣏⡇⠀⡶⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⣇⣴⠷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """

def start_game():
    typewriter("Welcome to the game! Ready to begin?")
    print("--------------------------------------")
    response = input(">(YES/NO) ").strip().lower()
    typewriter(f"You said: {response}")

    if response == "yes":
        start_beach()
    elif response == "NO":
        typewriter("Maybe next time.")
        start_game()
    elif response == "secret":
        typewriter("You find a secret!")
        typewriter("here is a picture of a dog just for finding the secret. :D")
        print(dog_art)
        start_game()
    else:
        print("Invalid input! Please choose 'YES' or 'NO'.")
        start_game()
    print("--------------------------------------")

def start_beach():

    typewriter("You wake up on a beach to the sound of heavy waves and seagulls. What do you do?")
    typewriter("Choose one: (LOOK AROUND / LAY DOWN IN SAND / CRY)")
    choice = input("What will you do? ").strip().lower()

    if choice == "look around":
        print("-------------------------------------------------")
        look_around()
    elif choice == "lay down in sand":
        print("-------------------------------------------------")
        lay_down()
    elif choice == "cry":
        print("-------------------------------------------------")
        cry()
    else:
        print("Invalid input! Please choose 'LOOK AROUND', 'LAY DOWN IN SAND', or 'CRY'.")
        start_beach()

def look_around():

    typewriter("You look around and see a lighthouse that is about a mile from you up a hill with a forest around it.")
    typewriter("Choose one: (WALK TOWARDS THE LIGHTHOUSE / CHECK POCKETS / LAY IN THE SAND)")
    choice = input("What will you do? ").strip().lower()

    if choice == "walk towards the lighthouse":
        print("-------------------------------------------------")
        walk_to_lighthouse()
    elif choice == "check pockets":
        print("-------------------------------------------------")
        check_pockets()
    elif choice == "lay in the sand":
        lay_down()
    else:
        print("Invalid input! Please choose 'WALK TOWARDS THE LIGHTHOUSE' , 'CHECK POCKETS' or 'LAY IN THE SAND'.")
        print("-------------------------------------------------")
        look_around()

def lay_down():

    typewriter("you lay down in the sand you feel the sand slowly sucking you deeper into the earth.")
    typewriter("Choose one: (DO NOTHING / STAND UP)")
    choice = input("What will you do? ").strip().lower()

    if choice == "do nothing":
        typewriter("You do nothing as you close your eyes and feel the sand pull you into the earth before waking up in your bed in a cold sweat.")
        typewriter('(ending 5/5)')
        print("-------------------------------------------------")
        game_over()
    elif choice == "stand up":
        typewriter("You struggle to get up as the sand holds onto you but you manage to stand up.")
        print("-------------------------------------------------")
        start_beach()
    else:
        typewriter("Invalid input! Please choose 'DO NOTHING' or 'STAND UP'.")
        lay_down()

def cry():
    typewriter("you start to cry, after a minute a seagul swoops down to you and drops you a half eaten burger.")
    choice = input("what do you do? (EAT BURGER / LOOK AROUND / CRY EVEN MORE)").strip().lower()
    print("-------------------------------------------------")

    if choice == "eat burger":
        typewriter("you eat the burger but stuggle to eat as you think about where the burger came from and all the sand in the burger.")
        print("-------------------------------------------------")
        after_burger()
    elif choice == "look around":
        look_around()
    elif choice == "cry even more":
        cry_more()
    else:
        typewriter("Invalid input! Please choose 'EAT BURGER' , 'LOOK AROUND' 'CRY EVEN MORE'.")
        print("-------------------------------------------------")
        cry()

def after_burger():
    typewriter("after eating the burger feel full or energy and notice a lighthouse that is about a mile from you up a hill with a forest around it.")
    choice = input("what will you do? (WALK TO THE LIGTHOUSE / CHECK POCKETS / LAY DOWN IN THE SAND)").strip().lower()
    print("-------------------------------------------------")

    if choice == "walk to the ligthhouse":
        walk_to_lighthouse()
    elif choice == "check pockets":
        check_pockets()
    elif choice == "lay down in the sand":
        lay_down()
    else:
        typewriter("Invalid input! Please choose 'WALK TO THE LIGTHOUSE' , 'CHECK POCKETS' 'LAY DOWN IN THE SAND'.")
        print("-------------------------------------------------")
        after_burger()
    
def walk_to_lighthouse():
    typewriter("you start walking towards the lighthouse a feeling of uneasy growing after every step")
    choice = input("What do you do? (KEEP WALKING / SIT DOWN AND REST / TURN AROUND AND WALK BACK)").strip().lower()
    print("-------------------------------------------------")

    if choice == "keep walking":
        keep_walking()
    elif choice == "sit down and rest":
        resting()
    elif choice == "turn around and walk back":
        walk_back()
    else:
        typewriter("Invalid input! Please choose 'KEEP WALKING' , 'SIT DOWN AND REST' 'TURN AROUND AND WALK BACK'.")
        print("-------------------------------------------------")
        walk_to_lighthouse()

def check_pockets():
    typewriter("you check you pockets and find a compass but instead of pointing to north it points towards the lighthouse")
    choice = input("What do you do? (WALK TOWARDS LIGHT HOUSE / LAY IN THE SAND)").strip().lower()
    print("-------------------------------------------------")

    if choice == "walk towards the light house":
        walk_to_lighthouse()
    elif choice == "lay in the sand":
        lay_down()
    else:
        typewriter("Invalid input! Please choose 'WALK TOWARDS LIGHT HOUSE' or 'LAY IN THE SAND'.")
        print("-------------------------------------------------")
        check_pockets()

def cry_more():
    typewriter("after a while of crying you feel somthing behind you, you turn around and see a black fog growing closer towards you.")
    choice = input("What will you do? (WALK TOWARDS THE LIGHT HOUSE / CRY EVEN MORE)")
    print("-------------------------------------------------")

    if choice == "walk towards the light house":
        walk_to_lighthouse()
    elif choice == "cry even more":
        cry_even_more()
    else:
        typewriter("Invalid input! Please choose 'WALK TOWARDS LIGHT HOUSE' or 'CRY EVEN MORE'.")
        print("-------------------------------------------------")
        cry_more()

def keep_walking():
    typewriter("You keep walking up the hill finally getting to lighthouse main door")
    choice = input("What do you do? (OPEN THE DOOR AND WALK IN / SIT AND REST.)").strip().lower()

    if choice == "open the door and walk in":
        inside_lighthouse()
    elif choice == "sit and rest":
        sit_rest()
    else:
        typewriter("Invalid input! Please choose 'OPEN THE DOOR AND WALK IN' or 'SIT AND REST'.")
        print("-------------------------------------------------")
        keep_walking()
        
def sit_rest():
    typewriter("you sit on the concrete slab that is used as a door mat for the lighthouse you look up from the ground and see a black fog coming from the forest towards you")
    choice = input("What do you do? (GO INSIDE THE LIGHTHOUSE / RUN INTO THE FOG)").strip().lower()

    if choice == "go inside the lighthouse":
        inside_lighthouse()
    elif choice == "run into the fog":
        run_into_fog()
    else:
        typewriter("Invalid input! Please choose 'GO INSIDE THE LIGHTHOUSE' or 'RUN INTO THE FOG'.")
        print("-------------------------------------------------")
        sit_rest()

def resting():
    typewriter("You sit down on a rock and see a black fog coming from the forest behind you")
    choice = input("What do you do? (KEEP WALKING UP THE HILL / RUN INTO THE FOG)").strip().lower()

    if choice == "keep walking up the hill":
        keep_walking()
    elif choice == "run into the fog":
        run_into_fog()
    else:
        typewriter("Invalid input! Please choose 'KEEP WALKING UP THE HILL' , 'RUN INTO THE FOG' 'TURN AROUND AND WALK BACK'.")
        print("-------------------------------------------------")
        walk_to_lighthouse()

def walk_back():
    typewriter("You try and walk back to the beach but the path is blocked off by a black fog that is making its way towards you.")
    choice = input("What do you do? (KEEP WALKING UP THE HILL / RUN INTO THE FOG)").strip().lower()

    if choice == "keep walking up the hill":
        keep_walking()
    elif choice == "run into the fog":
        run_into_fog()
    else:
        typewriter("Invalid input! Please choose 'KEEP WALKING UP THE HILL' , 'RUN INTO THE FOG' 'TURN AROUND AND WALK BACK'.")
        print("-------------------------------------------------")
        walk_back()

def cry_even_more():
    typewriter("you cry even more as the black fog engulfs you, you wake up in your bed crying. (ENDING 1/5)")
    print("-------------------------------------------------")
    game_over()

def inside_lighthouse():
    typewriter("you open the door to the lighthouse you see a set of stairs spiraling up towards the top of the lighthouse.")
    choice = input("What do you do? (WALKING UP THE STAIRS / LOOK AROUND / TURN AROUND AND WALK OUT)").strip().lower()

    if choice == "walk up the stairs":
        up_stairs()
    elif choice == "look around":
        look_around_inside()
    elif choice == "walk out":
        typewriter("you walk out and a black fog engulfs you, you jolt awake in your bed feeling like you just hit the ground after falling from your dream.")
        print("-------------------------------------------------")
        game_over()
    else:
        typewriter("Invalid input! Please choose 'WALKING UP THE STAIRS' , 'LOOK AROUND' 'TURN AROUND AND WALK OUT'.")
        print("-------------------------------------------------")
        inside_lighthouse()

def run_into_fog():
    typewriter("You run into the black fog preparing for the worst, you run till you cant anymore. you open your eyes and see a white void of nothing, a text promt appears infront of you")
    print("-------------------------------------------------")
    typewriter("the computer text says")
    print("-------------------------------------------------")
    typewriter('"Player has breached simulation"')
    typewriter('"restarting in"')
    typewriter('"....3"')
    typewriter('"....2"')
    typewriter('"....1"')
    typewriter('"loading def start_game"')
    typewriter('(ENDING 2/5)')
    start_game()
    
def up_stairs():
    print("-------------------------------------------------")
    typewriter("You walk up the stairs once you get to the top, you look out towards the sea you close your eyes and smell the fresh open waters")
    typewriter("you hear a segal screech as a segal flies right into your face as you lose your footing you slip falling down towards the ground")
    typewriter("but right before you hit the earth you wake up jolting awake in your bed in a cold sweat breathing heavy you turn to your left and see a segal eyeing you down before flying off")
    typewriter('(ENDING 4/5)')
    game_over()

def look_around_inside():
    typewriter("You find a hatch under the stairs")
    choice = input("What do you do? (OPEN THE HATCH / WALK UP THE STAIRS)")

    if choice == "open the hatch":
        hatch()
    elif choice == "walk up the stairs":
        up_stairs()
    else:
        typewriter("Invalid input! Please choose 'OPEN THE HATCH' or 'WALK UP THE STAIRS'.")
        print("-------------------------------------------------")
        look_around_inside()

def hatch():
    typewriter("you open the hatch and climb down and see yourself sleeping before you can do somthing you wake up confused on what just happend")
    typewriter('(ENDING 3/5)')
    game_over()

def game_over():
    print("-------------------------------------------------")
    typewriter("game-over. thanks for playing! :D")
    print("-------------------------------------------------")
    typewriter("credits")
    typewriter("code by Tony Vigil")

def main():
    #Main function to start the game
    start_game()

if __name__ == "__main__":
    main()