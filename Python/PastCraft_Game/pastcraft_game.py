
#!/usr/bin/env python3
"""
SURVIVAL PASTCRAFT SERVER
A terminal-based pick-your-adventure game inspired by the user's PastCraft story.
Creator: Jason Christopher Hukom
Assistant: ChatGPT (GPT-5 Thinking mini)
"""

import os
import sys
import time
import random
from getpass import getpass

# Utility functions ---------------------------------------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.01):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def splash_loading():
    clear()
    title = "SURVIVAL PASTCRAFT SERVER"
    subtitle = "the game"
    print("="*60)
    print(title.center(60))
    print(subtitle.center(60))
    print("="*60)
    print()
    print("Loading", end='', flush=True)
    for i in range(20):
        print('.', end='', flush=True)
        time.sleep(0.06)
    print("\n")
    time.sleep(0.4)
    clear()

# Hidden input helper (user inputs won't echo) -------------------------------
def hidden_choice(prompt="> "):
    # getpass hides the input so "it won't show" on screen
    try:
        c = getpass(prompt)
    except Exception:
        # fallback
        c = input(prompt)
    return c.strip()

# Story building blocks -----------------------------------------------------
def print_header(chapter_title):
    print("\n" + "="*60)
    print(chapter_title.center(60))
    print("="*60 + "\n")

# Chapters' narratives stored so we can reprint after minigame clears ----------
NARRATIVES = {
    "creation": (
        "— IN THE BEGINNING, there were pixels. And from those pixels, rose the blocks. "
        "These blocks form the world of Minecraft. One by one, it started from the void, "
        "then a singular block appeared — the First Minecraft Block. Two original Gods descended "
        "and shaped an overworld.\n\n"
        "They created endless grasslands, forests, mountains and seas. Tired of repeating worlds, "
        "one God forged a new realm made for play and friendship: Survival PastCraft Server. "
        "Players arrived: Jason_Hukom, Nicho_Gaming, Fatman, Minebeater, LMW015 and more. "
        "A world of creation, rivalry, bonds and legend was born."
    ),
    "wither_war": (
        "— WITHER WAR\n\n"
        "Tensions rose as factions argued whether to challenge the Ender Dragon or the Wither first. "
        "The Wither was summoned in haste. The underground exploded, nations fell, heroes died, and new clans formed. "
        "Some were saved by divine intervention — a timeline split where Gods stepped in and erased catastrophe. "
        "From the ashes rose new alliances and a hardened resolve to finish what they began."
    ),
    "end_battle_united": (
        "— END BATTLE UNITED\n\n"
        "Leaders united under the banner of the United Bavariad Empire to finally face the Ender Dragon. "
        "Trials, mistakes and sacrifice marked the battle — beds exploded, players fell, and one arrow changed fate. "
        "Although victory came at cost, the Gods returned the Dragon Egg as a sign that the world would go on."
    ),
    "nipaliterra": (
        "— NIPALITERRA\n\n"
        "Nipaliterra rose as a republic built by founding members. Internal strife, theft, masked saboteurs and suspicion "
        "plagued the city. Walled perimeters and strict rules were born as citizens struggled to figure friend from foe. "
        "Legends grew as hidden identities and mysteries persisted."
    ),
    "faxion_arc": (
        "— A FORCE NOT MEANT TO BE RECKONED WITH\n\n"
        "Faxion Warrior ascends from legendary archer to a being with godlike power after surviving the void. "
        "His gift of power to others causes chaos when mortals misuse the divine. A tragic schism with Jason forms — "
        "a story of pride, power and the cost of giving everything to the world."
    )
}

# Core gameplay logic --------------------------------------------------------
class GameState:
    def __init__(self):
        self.as_god = True
        self.chosen_players = []
        self.play_counts = {"Nicho_Gaming":0, "Faxion_Warrior":0}
        self.history = []

    def become_god(self):
        self.as_god = True

    def choose_players(self, pool, count=3):
        clear()
        print_header("CHOOSE THE FIRST PLAYERS")
        print("As a God you may select players who will live and carry the story forward.\n")
        for i, p in enumerate(pool,1):
            print(f"{i}. {p}")
        print("\nChoose by number. Your inputs are hidden so the choices won't show on-screen.")
        picks = []
        while len(picks) < count:
            sel = hidden_choice(f"Pick #{len(picks)+1}: ")
            if not sel.isdigit() or not (1 <= int(sel) <= len(pool)):
                print("Invalid choice. Try again.")
                continue
            name = pool[int(sel)-1]
            if name in picks:
                print("Already picked. Choose another.")
                continue
            picks.append(name)
            # track play counts for the special arc condition
            if name in self.play_counts:
                self.play_counts[name] += 1
        self.chosen_players = picks
        self.history.append(("god_pick", picks.copy()))
        print("\nPlayers chosen.  (Input was hidden.)")
        time.sleep(0.8)
        return picks

    def run_minigame(self, kind="guess"):
        # Warn user a minigame is coming
        print("\n--- MINIGAME COMING UP! ---")
        slow_print("Prepare yourself. Your input won't be echoed during the minigame.", 0.005)
        time.sleep(0.8)

        result = None
        if kind == "guess":
            # Number guess: hidden input and some randomized challenge
            target = random.randint(1, 10)
            attempts = 3
            slow_print("Guess the secret number between 1 and 10. You have 3 tries.", 0.005)
            for _ in range(attempts):
                guess = hidden_choice("Your guess: ")
                if not guess.isdigit():
                    # ignore invalid but consume attempt
                    continue
                if int(guess) == target:
                    result = True
                    break
            else:
                result = False
            # After minigame, clear the outputs but preserve narrative
            time.sleep(0.4)
            clear()
            return result
        elif kind == "rps":
            choices = ['rock','paper','scissors']
            slow_print("Rock-Paper-Scissors: best of one. Type rock/paper/scissors (input hidden).", 0.005)
            player = hidden_choice("Your move: ").lower()
            bot = random.choice(choices)
            if player not in choices:
                result = False
            elif player == bot:
                result = None  # tie
            elif (player == 'rock' and bot == 'scissors') or \
                 (player == 'paper' and bot == 'rock') or \
                 (player == 'scissors' and bot == 'paper'):
                result = True
            else:
                result = False
            time.sleep(0.4)
            clear()
            return result
        else:
            # simple math
            a, b = random.randint(1,9), random.randint(1,9)
            slow_print(f"Solve: {a} + {b} = ? (input hidden)", 0.005)
            ans = hidden_choice("Answer: ")
            try:
                result = (int(ans) == a+b)
            except:
                result = False
            time.sleep(0.4)
            clear()
            return result

# Chapters as functions ------------------------------------------------------
def chapter_creation(state: GameState):
    print_header("CREATION OF PASTCRAFT")
    slow_print(NARRATIVES["creation"] + "\n", 0.004)
    time.sleep(0.6)
    # Choose first players
    pool = ["Jason_Hukom", "Nicho_Gaming", "Fatman", "Minebeater", "LMW015", "Hurikane", "Jordan"]
    picks = state.choose_players(pool, count=3)
    slow_print(f"The God watches as {', '.join(picks)} begin their lives in PastCraft.", 0.004)
    state.history.append(("creation", picks))
    time.sleep(0.6)
    # short minigame then epilogue
    res = state.run_minigame("guess")
    if res:
        slow_print("The minigame succeeded. The early days are kind to your chosen players.", 0.004)
    else:
        slow_print("The minigame failed. Trials come early to PastCraft.", 0.004)
    time.sleep(0.6)
    print("\nEpilogue: The world grows. Nations begin to form.\n")
    time.sleep(1.0)
    state.become_god()

def chapter_wither_war(state: GameState):
    print_header("WITHER WAR")
    slow_print(NARRATIVES["wither_war"] + "\n", 0.004)
    time.sleep(0.6)
    # Choose champions to lead the fight
    pool = state.chosen_players + ["Jordan","Gopnikkinator","Faxion_Warrior","GoodnessGracious"]
    picks = state.choose_players(list(dict.fromkeys(pool)), count=3)
    slow_print(f"{', '.join(picks)} march into darkness to fight the Wither.", 0.004)
    state.history.append(("wither_war", picks))
    # Minigame for the battle
    res = state.run_minigame("rps")
    if res is True:
        slow_print("Victory! The Wither stumbles; nations survive.\n", 0.004)
    elif res is None:
        slow_print("A stalemate. The Wither retreats into legend.\n", 0.004)
    else:
        slow_print("The Wither breaks free, catastrophe forces a reset by the Gods.\n", 0.004)
    time.sleep(0.8)
    print("Epilogue: Timeline split. The players remember and worship the Gods.\n")
    state.become_god()

def chapter_end_battle(state: GameState):
    print_header("END BATTLE UNITED")
    slow_print(NARRATIVES["end_battle_united"] + "\n", 0.004)
    time.sleep(0.6)
    pool = ["Faxion_Warrior", "LMW015", "Jason_Hukom", "Gopnikkinator", "Faxion_Warrior", "Jordan"]
    picks = state.choose_players(list(dict.fromkeys(pool)), count=4)
    slow_print("They gather at the portal. One bed explodes, one arrow strikes true.\n", 0.004)
    state.history.append(("end_battle", picks))
    res = state.run_minigame("math")
    if res:
        slow_print("Against odds, the Dragon falls and an Egg remains.\n", 0.004)
    else:
        slow_print("The Dragon resists — but the Gods confer mercy and the Egg survives.\n", 0.004)
    time.sleep(0.8)
    print("Epilogue: Victory and loss entwined. The Gods return.\n")
    state.become_god()

def chapter_nipaliterra(state: GameState):
    print_header("NIPALITERRA")
    slow_print(NARRATIVES["nipaliterra"] + "\n", 0.004)
    time.sleep(0.6)
    pool = ["Beginner","Master_W","Jordan","Jason_Hukom","LMW015","PIG_123","Faxion_Warrior"]
    picks = state.choose_players(pool, count=3)
    slow_print(f"The city braces as {', '.join(picks)} navigate suspicion and ruin.\n", 0.004)
    state.history.append(("nipaliterra", picks))
    res = state.run_minigame("guess")
    if res:
        slow_print("An honest verdict helps calm the city... for now.\n", 0.004)
    else:
        slow_print("Chaos reigns; masked figures vanish into the night.\n", 0.004)
    time.sleep(0.6)
    state.become_god()

def chapter_faxion_arc(state: GameState):
    print_header("FAXION'S ASCENT")
    slow_print(NARRATIVES["faxion_arc"] + "\n", 0.004)
    time.sleep(0.6)
    # This arc unlocks only if Nicho or Faxion chosen 3 times total
    cond = (state.play_counts.get("Nicho_Gaming",0) >= 3) or (state.play_counts.get("Faxion_Warrior",0) >= 3)
    if not cond:
        slow_print("The forces which would fuel Faxion's ascension do not fully align in this timeline.\n", 0.004)
        return
    slow_print("Power surges. The world must decide whether to embrace or reject absolute gifts.\n", 0.004)
    picks = state.choose_players(["Faxion_Warrior","Nicho_Gaming","Jason_Hukom","LMW015"], count=2)
    state.history.append(("faxion_arc", picks))
    res = state.run_minigame("rps")
    if res:
        slow_print("Faxion resists hubris and chooses restraint.\n", 0.004)
    else:
        slow_print("Power corrupts; a schism forms and the world changes forever.\n", 0.004)
    time.sleep(0.6)
    state.become_god()

# Main menu and flow --------------------------------------------------------
def show_description():
    clear()
    print_header("DESCRIPTION")
    slow_print("SURVIVAL PASTCRAFT SERVER is a text-based adaptation of the PastCraft world. "
               "You will begin as a God, select early players, guide chapters, face minigames (hidden input), "
               "and shape endings. Some arcs require repeated character choice to unlock.\n", 0.006)
    input("\nPress Enter to return to menu...")

def main_game_loop():
    state = GameState()
    while True:
        clear()
        print("="*60)
        print("SURVIVAL PASTCRAFT SERVER".center(60))
        print("the game".center(60))
        print("="*60)
        print("\n1) START\n2) DESCRIPTION\n3) EXIT\n")
        choice = input("Select an option: ").strip()
        if choice == '1':
            # Start sequence
            splash_loading()
            # Start as God -> creation -> wither -> end battle -> nipaliterra -> optional faxion arc
            chapter_creation(state)
            chapter_wither_war(state)
            chapter_end_battle(state)
            chapter_nipaliterra(state)
            # Faxion arc only possibly if condition met
            chapter_faxion_arc(state)
            # Final summary / endings
            clear()
            print_header("FINAL EPILOGUE")
            slow_print("Your choices shaped PastCraft. History remembers the brave, the clever, and the foolish.", 0.006)
            slow_print("Play history (chronology of important events):", 0.002)
            for k,v in state.history:
                slow_print(f"- {k}: {v}", 0.002)
            slow_print("\nThank you for playing. You return to the realm above, once more a God.\n", 0.004)
            input("Press Enter to return to main menu...")
        elif choice == '2':
            show_description()
        elif choice == '3':
            clear()
            print("Exiting... Goodbye.")
            time.sleep(0.4)
            sys.exit(0)
        else:
            print("Invalid option. Try again.")
            time.sleep(0.6)

if __name__ == '__main__':
    try:
        main_game_loop()
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye.")
