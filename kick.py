import random
import time

goal_commentary = [
    "What a screamer into the top corner! 💥",
    "Keeper had no chance! ⚽🔥",
    "An absolute beauty of a goal!",
    "He sends the keeper the wrong way! 😎",
    "GOOOAAAALLLL! The crowd goes wild! 🥳"
]

save_commentary = [
    "That’s a world-class save! 🧤",
    "Brilliant reflexes from the keeper!",
    "Denied! The wall stands tall! 🚧",
    "Incredible stop, what a moment!",
    "Keeper guessed it perfectly! ❌"
]

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
    print(f"Save {max_score} shots to win!\n")

    while True:
        shot = random.choice(directions)
        
        # Validate input
        guess = input(f"Which direction will you dive? {tuple(directions)}: ").lower()
        while guess not in directions:
            guess = input(f"Invalid! Choose from {tuple(directions)}: ").lower()

        time.sleep(0.5)

        if guess == shot:
            print(random.choice(save_commentary))
            score += 1
        else:
            print(f"The player shot {shot}. You missed it! ❌")

        print(f"Score: {score}/{max_score}\n")

        if score == max_score:
            print("\n🏆 GAME OVER: You’re the WALL! Congratulations! 🎉\n")
            break

elif mode == "2":
    print("\n⚽ Striker Mode Activated!")
    print(f"Score {max_score} goals to win!\n")

    while True:
        keeper = random.choice(directions)
        
        shot = input(f"Which direction do you shoot? {tuple(directions)}: ").lower()
        while shot not in directions:
            shot = input(f"Invalid! Choose from {tuple(directions)}: ").lower()

        time.sleep(0.5)

        if shot != keeper:
            print(random.choice(goal_commentary))
            score += 1
        else:
            print(f"The keeper guessed {keeper} and saved it! 🧤")

        print(f"Score: {score}/{max_score}\n")

        if score == max_score:
            print("\n🏆 GAME OVER: You’re a goal-scoring machine! Well done! 🎯\n")
            break

else:
    print("Invalid input. Please restart the game and choose 1 or 2.")
