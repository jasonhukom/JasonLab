def main():
    score = []
    subject = ["IPA", "Agama", "PPKn", "IPS", "Bahasa Indonesia", "Mandarin", "PJOK", "Matematika","Informatika","Bahasa Inggris","Art"]
    while True:
        try:
            name = str(input("Student name: "))
            break
        except ValueError:
            print("Your input is invalid, please input again\n")
    score = score_search(len(subject), subject)
    avg = average(score)
    text = toc(avg)
    print(f"Congratulation {name}!\nYou got a {avg}\n{text}")
    
def score_search(num, str):
    score_array = []
    i = 0
    while i < num:
        try:
            score_array.append(int(input(f"\nScore student {str[i]}: ")))
            i += 1
        except ValueError:
            print("Your input is invalid, please input again\n")
            i -= 1
    return score_array
    
def average(num):
    return sum(num) / len(num)
    
def toc(num):
    if num == 100:
        return "Amazing Work"
    elif num >= 90:
        return "Good Job"
    elif num >= 80:
        return "Nice Work"
    elif num >= 60:
        return "Try better next time"
    else:
        return "You did your best!"

if __name__ == "__main__":
    main()