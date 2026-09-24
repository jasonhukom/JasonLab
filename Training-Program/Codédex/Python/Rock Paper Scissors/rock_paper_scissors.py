from random import randint

def main():
    print("""
================================
Rock Paper Scissors Lizard Spock
================================

1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
    """)
    question()


def cpu():
    return randint(1, 5)

def question():
    rock_paper_scissors_plus = {
        1: "✊",
        2: "✋",
        3: "✌️",
        4: "🦎",
        5: "🖖"
    }

    while True:
        try:
            user_input = int(input("Pick a number: "))    
            print(f"\nYou chose: {rock_paper_scissors_plus[user_input]}")
            cpu_input = cpu()
            print(f"CPU chose: {rock_paper_scissors_plus[cpu_input]}")
        except ValueError:
            break 
        except (IndexError, KeyError):
            pass
        else:
            user_input_in_string = ("rock" if user_input == 1 else 
            ("paper" if user_input == 2 else 
            ("scissors" if user_input == 3 else
            ("lizard" if user_input == 4 else
            ("spock" if user_input == 5 else KeyError)))))
            
            cpu_in_string = ("rock" if cpu_input == 1 else 
            ("paper" if cpu_input == 2 else 
            ("scissors" if cpu_input == 3 else
            ("lizard" if cpu_input == 4 else
            ("spock" if cpu_input == 5 else KeyError)))))

            print(rock_paper_scissors(user_input_in_string, cpu_in_string))
            

def rock_paper_scissors(input1, input2):
    tie = "\nIt's a tie!"
    win = "\nThe player won!"
    loose = "\nCPU won!"
    match input1:
        case "rock": 
            match input2:
                case "rock":
                    return tie
                case "paper":
                    return loose
                case "scissors":
                    return win
                case "lizard":
                    return win
                case "spock":
                    return loose
        case "paper":
            match input2:
                case "rock":
                    return win
                case "paper":
                    return tie
                case "scissors":
                    return loose
                case "lizard":
                    return loose
                case "spock":
                    return win
        case "scissors":
            match input2:
                case "rock":
                    return loose
                case "paper":
                    return win
                case "scissors":
                    return tie
                case "lizard":
                    return win
                case "spock":
                    return loose
        case "lizard":
            match input2:
                case "rock":
                    return loose
                case "paper":
                    return win
                case "scissors":
                    return loose
                case "lizard":
                    return tie
                case "spock":
                    return win
        case "spock":
            match input2:
                case "rock":
                    return win
                case "paper":
                    return loose
                case "scissors":
                    return win
                case "lizard":
                    return loose
                case "spock":
                    return tie

main()