
#!/usr/bin/env python3
"""
PastCraft: Choose-Your-Ending Novel (interactive)
Author: ChatGPT for Jason
Description:
  Single-file interactive Python console experience based on the provided PastCraft story.
  - Presents prologues and assigns a playable character
  - Long narrative passages with choices that change the story path
  - Small minigames: timed QTE, number guessing, quick-typing challenge, and simple combat RNG
  - Mentions all requested characters and preserves story elements
Save this file and run with: python3 pastcraft_cyoa.py
"""

import random
import time
import textwrap
import threading
import sys
from queue import Queue, Empty

# ----------------------------- Utilities -----------------------------

def slowprint(text, delay=0.008, sep='\n'):
    """Nicely prints long paragraphs slowly (like reading a book)."""
    for line in textwrap.fill(text, width=80).split('\n'):
        print(line)
        time.sleep(delay * max(1, len(line)/40))
    print(sep, end='')

def choice_input(prompt, options):
    """Prompt user to choose from numbered options."""
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        ans = input("> ").strip()
        if ans.isdigit() and 1 <= int(ans) <= len(options):
            return int(ans)
        print("Please type the number of your choice.")

def timed_input(prompt, timeout):
    """Try to read input within timeout seconds. Returns None if timed out."""
    q = Queue()

    def worker():
        try:
            ans = input(prompt)
            q.put(ans)
        except Exception:
            q.put(None)

    t = threading.Thread(target=worker, daemon=True)
    t.start()
    try:
        return q.get(block=True, timeout=timeout)
    except Empty:
        return None

def press_any_key(prompt="Press Enter to continue..."):
    input(prompt)

# ----------------------------- Game Data -----------------------------

CHARACTERS = [
    "Jason_Hukom (the Phantom Menace)",
    "Nicho_Gaming (the chaotic schemer)",
    "Fatman / Fatterman (the cobblestone leader)",
    "Minebeater (the helper)",
    "LMW015 (the lucky miner)",
    "Hurikane (the slide warrior)",
    "GoodnessGracious (the loyal friend)",
    "Jordan (leader and builder)",
    "Gopnikkinator (the strategist)",
    "Faxion Warrior (the marksman -> later God)",
    "Master W (the quiet veteran)",
    "Beginner (the diamond hoarder)",
    "Deekwatson (the ally)",
    "Cocout 356z (the curious)",
    "BenzelSMP (the wrecking crew)",
    "PIG 123 (the masked chaos)"
]

# ----------------------------- Story Segments -----------------------------

PROLOGUE = """
IN THE BEGINNING, there were pixels. From those pixels rose the blocks.
Two original Gods created an overworld from a single block, and they played within it.
They named it Survival PastCraft Server. Players were summoned, towers built, graves dug,
and the world grew chaotic and alive. This is a tale of towers, wither wars, betrayals,
and the slow rise of legends: Jason_Hukom, Nicho_Gaming, Fatman, Minebeater, LMW015, Hurikane,
GoodnessGracious, Jordan, Gopnikkinator, Faxion Warrior, Master W, Beginner, and more.
"""

INTRO_NOTE = """
You will become one character from this world. You'll walk through long narrative
sections and be given choices that change the ending. Small minigames (timed and guessing)
decide the results of big battles like the Wither War and the Ender Dragon encounter.
Some endings are heroic, some are chaotic, some are tragic. Enjoy.
"""

# ----------------------------- Minigames -----------------------------

def minigame_guess_number(max_num=20, tries=4):
    """Classic number guessing."""
    target = random.randint(1, max_num)
    slowprint(f"A small gamble minigame starts: guess a number between 1 and {max_num}. You have {tries} tries.")
    for attempt in range(1, tries+1):
        ans = input(f"Try {attempt}/{tries}: ")
        if not ans.isdigit():
            print("Please type a number.")
            continue
        g = int(ans)
        if g == target:
            slowprint("Perfect! You guessed the number!")
            return True
        elif g < target:
            print("Too low.")
        else:
            print("Too high.")
    slowprint(f"You failed to guess it. The number was {target}.")
    return False

def minigame_qte(timeout=4.0):
    """Quick-time-event: press Enter within timeout to succeed."""
    slowprint("Quick-time event! Press Enter as quickly as you can when ready.")
    ans = timed_input("Get ready... press Enter NOW! ", timeout)
    if ans is None:
        slowprint("Too slow! You miss the moment.")
        return False
    slowprint("Nicely done — you hit the moment in time!")
    return True

def minigame_type_speed(text="PHANTOM", timeout=6):
    """Type-the-word challenge within timeout."""
    slowprint(f"Type this word exactly within {timeout} seconds: {text}")
    ans = timed_input("> ", timeout)
    if ans is None:
        slowprint("Time expired. Your fingers betrayed you.")
        return False
    if ans.strip() == text:
        slowprint("You typed it perfectly!")
        return True
    else:
        slowprint("Not exact. Close but not enough.")
        return False

# ----------------------------- Combat Systems -----------------------------

def simple_combat(enemy_name="Wither", player_power=10):
    """Simple probabilistic combat with a small interactive twist."""
    slowprint(f"A battle begins! Enemy: {enemy_name}. Your base power: {player_power}")
    enemy_hp = 20 + random.randint(0, 20)
    player_hp = 20 + random.randint(0, 10)
    slowprint(f"{enemy_name} HP: {enemy_hp} | Your HP: {player_hp}")
    turn = 1
    while enemy_hp > 0 and player_hp > 0 and turn <= 12:
        slowprint(f"--- Turn {turn} ---")
        choice = choice_input("Choose your action:", ["Slash / Attack", "Defend / Brace", "Attempt a risky special (minigame)"])
        if choice == 1:
            dmg = random.randint(3, player_power)
            enemy_hp -= dmg
            slowprint(f"You hit the {enemy_name} for {dmg} damage! Enemy HP now {max(0, enemy_hp)}")
        elif choice == 2:
            heal = random.randint(1, 4)
            player_hp += heal
            slowprint(f"You brace and find inner strength, restoring {heal} HP. Your HP now {player_hp}")
        else:
            slowprint("Special attempt! Complete a quick minigame to power it up.")
            ok = minigame_qte(timeout=3.5)
            if ok:
                dmg = random.randint(player_power, player_power + 10)
                enemy_hp -= dmg
                slowprint(f"Your special succeeds, dealing {dmg} damage! Enemy HP now {max(0, enemy_hp)}")
            else:
                backfire = random.randint(2, 6)
                player_hp -= backfire
                slowprint(f"The special backfires: you lose {backfire} HP. Your HP now {player_hp}")
        # enemy action
        if enemy_hp > 0:
            edmg = random.randint(2, 8)
            player_hp -= edmg
            slowprint(f"The {enemy_name} strikes you for {edmg} damage! Your HP: {max(0, player_hp)}")
        turn += 1
        if player_hp <= 0:
            break
    if enemy_hp <= 0 and player_hp > 0:
        slowprint(f"You defeated the {enemy_name}! Victory!")
        return True
    elif player_hp <= 0:
        slowprint("You were defeated in battle... but stories sometimes bend for the brave.")
        return False
    else:
        slowprint("The fight ends unresolved as events intervene.")
        return False

# ----------------------------- Story Paths -----------------------------

def prologue_scene(player):
    slowprint(PROLOGUE)
    slowprint(INTRO_NOTE)
    slowprint(f"You are playing as: {player}\n")
    press_any_key()

def town_drama(player):
    slowprint("PASTCRAFT 1.0 — Here Comes the Fire")
    slowprint("The town grows. Jason builds a tower, Nicho builds a wooden house, LMW015 digs mines. Fatman and Minebeater plan the Cobblestone Village and set rules: No Stealing, No Griefing, Family-Friendly.")
    slowprint("One day a hole appeared in Jason's wall and his secret barrel was empty. Suspicion falls on Nicho_Gaming.")
    slowprint("Jason confronts Nicho. A scuffle turns violent and Nicho is slain — but the Gods judge and respawn Nicho at spawnpoint. The tension doesn't end; trust is shaken.")
    slowprint("You see factions forming: Bavariad Empire, Czech Republic, Norde Clan, and Nipaliterra. Names like Fatterman, GoodnessGracious, Jordan, and Hurikane appear in every rumor.")
    choice = choice_input("What do you do?", [
        "Investigate Nicho secretly (sneak & minigame)",
        "Alliance with Bavariad: help organize defense",
        "Join Czech Republic and cause chaos to gain power"
    ])
    if choice == 1:
        slowprint("You follow Nicho under moonlight and find a trail of footprints leading to LMW015's mine...")
        ok = minigame_guess_number(max_num=12, tries=3)
        if ok:
            slowprint("You discovered evidence! LMW015 was framed by someone else. This revelation starts a new plot against PIG 123.")
            return "evidence_found"
        else:
            slowprint("You couldn't find proof. Everyone suspects you of creating drama. You lose some reputation.")
            return "failed_probe"
    elif choice == 2:
        slowprint("You help Bavariad set defenses. Fatterman and GoodnessGracious appreciate your help.")
        return "bavariad_help"
    else:
        slowprint("You join Czech Republic. You and Jordan build and recruit. Soon you become embroiled in civil war.")
        return "czech_joined"

def wither_war_scene(player, tag):
    slowprint("PASTCRAFT: WITHER WAR — They Came to Save Us")
    slowprint("Tensions rise: Nicho wants to kill the Ender Dragon, Fatman wants to kill the Wither first.")
    slowprint("Czech vs Bavariad. A Wither is summoned deep in the mines. The server trembles.")
    slowprint("Summoning happens. The Wither explodes. Many players die. The Gods intervene and sometimes fix the timeline.")
    slowprint("You gather allies: Jason_Hukom, LMW015, Jordan, Hurikane, GoodnessGracious, Faxion Warrior and more. It's a make-or-break battle.")
    # If player assisted Bavariad earlier, slight advantage
    base_power = 10 + (3 if tag == "bavariad_help" else 0)
    slowprint("Prepare for a dangerous minigame-combat hybrid to face the Wither. You will need skill and luck.")
    prepped = minigame_type_speed(text="WITHER", timeout=7)
    if prepped:
        slowprint("Your speed prepped you for the ritual; the Wither is vulnerable to quick strikes.")
    else:
        slowprint("You failed the typing ritual. The Wither is enraged.")
    won = simple_combat("Wither", player_power=base_power + (5 if prepped else 0))
    if won:
        slowprint("The Wither falls — but the world is scarred. Norde Clan forms, survivors rebuild, and the Gods smile upon those who survived.")
        return "wither_defeated"
    else:
        slowprint("Many perished. The timeline shudders. Yet legends are born from the ashes.")
        return "wither_failure"

def ender_dragon_scene(player, tag, prior_victory):
    slowprint("PASTCRAFT: END BATTLE UNITED — They Come to Destroy Us / They Come to Save Us")
    slowprint("After the Wither, factions unite (or stay fractured) to kill the Ender Dragon. Jason organizes United Bavariad Empire to finish the game.")
    slowprint("The raid to the End happens. Beds are used as explosives, and one fateful click can change everything.")
    slowprint("You and your group cross the End and confront the Dragon.")
    # A guessing minigame to help destroy crystals remotely
    slowprint("To fell the dragon faster, you can attempt a coordinated guess-number to break crystals.")
    teamwork_success = minigame_guess_number(max_num=15, tries=4)
    if teamwork_success or prior_victory == "wither_defeated":
        slowprint("The coordinated strikes weaken the dragon. During the final burst some players misclick and beds explode. The dragon dies.")
        # Randomly decide who gets the Dragon Egg
        egg_holder = random.choice(["Faxion Warrior", "LMW015", "Faxion accidentally (and heroically)")]
        slowprint(f"The Dragon dies. The sole Dragon Egg ends up in the hands of: {egg_holder}.")
        if egg_holder.startswith("Faxion"):
            slowprint("Faxion Warrior later rises to godlike power after surviving strange events. This creates tension with Jason who fears gods.")
        return "dragon_defeated"
    else:
        slowprint("The dragon proves too strong. The raid fails. Many are lost. The Gods return the Egg in some distant timeline.")
        return "dragon_failed"

# ----------------------------- Endings -----------------------------

def epilogue(player, path_tag, final_tag):
    slowprint("EPILOGUE — The End?")
    slowprint(f"You played as {player}. Your path: {path_tag} -> {final_tag}.")
    endings = {
        ("evidence_found", "wither_defeated"): "You became a famed investigator-hero, uncovering PIG 123 and restoring order. The gods nodded.",
        ("failed_probe", "wither_failure"): "Your suspicion cost you friends. You wandered, a haunted miner.",
        ("bavariad_help", "dragon_defeated"): "You helped unite the server and were hailed as a leader of the United Bavariad Empire.",
        ("czech_joined", "dragon_failed"): "Chaos reigned. Your republic rose and fell, tales of PIG 123 echoing forever.",
    }
    key = (path_tag, final_tag)
    slowprint(endings.get(key, "You lived a story that will be told around bonfires. Names like Jason_Hukom, Nicho_Gaming, Fatman, Fatterman, Minebeater, LMW015, Hurikane, GoodnessGracious, Jordan, Gopnikkinator, Faxion Warrior, Master W, Beginner, PIG 123, and many others will sing of your deeds."))
    slowprint("Some characters take strange turns: Faxion becomes a God in a timeline, Nipaliterra grows, and Norde Clan survives. The Gods sometimes intervene and sometimes merely watch.")
    slowprint("Thank you for playing PastCraft. The End... or a new beginning?")
    press_any_key("Press Enter to see secret epilogues...")
    # small secret random epilogues
    if random.random() < 0.25:
        slowprint("SECRET: A masked figure (PIG 123?) still wanders Nipaliterra, whispering 'Begin again'...")
    if random.random() < 0.15:
        slowprint("SECRET: Faxion, now godlike, leaves a Phantom Costume in Jason's lair as a gift...")
    slowprint("Credits: Story and characters by Jason (provided text). This adaptation by ChatGPT. Play again to unlock different endings.")

# ----------------------------- Main Flow -----------------------------

def main():
    random.seed()  # system random
    slowprint("=== PASTCRAFT: CHOOSE YOUR ENDING ===", delay=0.001)
    slowprint("Welcome to PastCraft — an interactive choose-your-ending novel.")
    # Choose or assign a character
    print("Choose who you want to be, or let the server pick for you:")
    for i, c in enumerate(CHARACTERS, 1):
        print(f"  {i}. {c}")
    print(f"  {len(CHARACTERS)+1}. Surprise me (random character)")
    while True:
        sel = input("> ").strip()
        if sel.isdigit():
            n = int(sel)
            if 1 <= n <= len(CHARACTERS):
                player = CHARACTERS[n-1]
                break
            elif n == len(CHARACTERS)+1:
                player = random.choice(CHARACTERS)
                break
        print("Please type a valid number from the list.")

    prologue_scene(player)
    path_tag = town_drama(player)
    final_tag = wither_war_scene(player, path_tag)
    final_tag2 = ender_dragon_scene(player, path_tag, final_tag)
    epilogue(player, path_tag, final_tag2)
    slowprint("End of script. Thank you for exploring PastCraft. Re-run to explore other branches.")

if __name__ == '__main__':
    main()
