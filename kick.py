goal_commentary = [
    "What a screamer into the top corner!💥",
    "Keeper had no chance!⚽🔥",
    "An absolute beauty of a goal!",
    "He sends the keeper the wrong way!😎",
    "GOOOAAAALLLL! The crowd goes wild!🥳"
]

save_commentary = [
    "That’s a world-class save! 🧤",
    "Brilliant reflexes from the keeper!",
    "Denied! The wall stands tall! 🚧",
    "Incredible stop, what a moment!",
    "Keeper guessed it perfectly! ❌"
]
import random
import time

directions = ['up', 'down', 'left', 'right']
score = 0
max_score = 5

print("Welcome to Python Penalty Simulator - CyberSage V1.0 ⚽")
print("🧠 Created by Habib (The Ghost Analyst)\n")

# Choose game mode
print("Choose your role:")
print("1. 🧤 Keeper Mode (Save the shot)")
print("2. ⚽ Striker Mode (Score the goal)")
mode = input("Enter 1 or 2: ").strip()

if mode == "1":
    print("\n🧤 Keeper Mode Activated!")
    print("Save 5 shots to win!\n")

    while True:
        shot = random.choice(directions)
        guess = input(f"Which direction will you dive to save? {tuple(directions)}: ").lower()
        time.sleep(0.5)

        if guess == shot:
            print("Good job! What a save! 🧤⚽\n")
            score += 1
            print(random.choice(save_commentary))
        else:
            print(f"The player shot {shot}. You missed it!\n")

        print(f"Score: {score}/{max_score}\n")

        if score == max_score:
            print("🏆 Game Over: You’re the WALL! Congratulations!")
            break

elif mode == "2":
    print("\n⚽ Striker Mode Activated!")
    print("Score 5 goals to win!\n")

    while True:
        keeper = random.choice(directions)
        shot = input(f"Which direction do you shoot? {tuple(directions)}: ").lower()

        if shot not in directions:
            print("Invalid direction! Choose from up, down, left, or right.\n")
            continue

        time.sleep(0.5)

        if shot != keeper:
            print("GOAAALLL!!⚽🔥 \n")
            score += 1
            print(random.choice(goal_commentary))
        else:
            print(f"The keeper guessed {keeper} and saved it! 🧤\n")

        print(f"Score: {score}/{max_score}\n")

        if score == max_score:
            print("🏆 Game Over: You’re a goal-scoring machine! Well done!")
            break

else:
    print("Invalid input. Please restart the game and choose 1 or 2.")

