print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

question_pool = {
    "What does CPU stand for? ": "central processing unit",
    "What does GPU stand for? ": "graphics processing unit",
    "What does RAM stand for? ": "random access memory",
    "What does PSU stand for? ": "power supply"
}


score = 0
for k, v in question_pool.items():
    print()
    answer = input(k)

    if answer.lower() == v:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(
    f"You got {score / len(question_pool) * 100}% of the questions right!")
