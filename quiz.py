score = 0
print("Quiz")

answer = input("1) what is harmonia's agent name? ")
if answer.lower().strip() == "echo":
    print("it's correct ")
    score += 1
else:
    print("the correct answer was Echo")

answer = int(input("7 * 8 ?"))
if answer == 56:
    print("it's correct")
    score += 1
else:
    print("the correct answer was 56")

answer = input("3) which one is a program on your own laptop? git or github")
if answer.lower().strip() == "git":
    print("it's correct ")
    score += 1
else:
    print("the correct answer was Echo")
    
print(f'your score is {score} / 3')
if score == 3:
    print("great, you are ready")
elif score >= 1:
    print("it was okay but try again")
else:
    print("no problem you will fix it")