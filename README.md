# ⚽ Python Penalty Simulator – CyberSage V1.0

A fun, interactive **penalty shootout game** written in Python.  
You can play as either:
- 🧤 **Keeper** – try to save 5 shots
- ⚽ **Striker** – try to score 5 goals

Created by **Habib (The Ghost Analyst)**.

---

## 🎮 How to Play

1. **Run the game** in your Python environment:
   ```bash
   python penalty_simulator.py
````

2. **Choose your role**:

   * `1` → Keeper Mode
   * `2` → Striker Mode
3. **Make your moves** by typing one of the four directions:

   ```
   up, down, left, right
   ```
4. First to **5 points** wins the game!

---

## 📂 Features

* Randomized directions for keeper/striker
* Fun, dynamic commentary for every goal/save
* Input validation for directions
* Win condition system (first to 5 points)
* Designed for beginner-friendly Python practice

---

## 🛠 Requirements

* **Python 3.x**
* Works in any terminal or IDE
* No external libraries required (uses `random` and `time` from Python's standard library)

---

## 🚀 How It Works

* **Random direction** is generated for either the keeper or the striker.
* Player guesses/shoots by entering a direction.
* If the guess matches (Keeper Mode) or differs (Striker Mode), a point is awarded.
* Commentary is chosen randomly from predefined lists.

---

## 📷 Example Gameplay

```
Welcome to Python Penalty Simulator - CyberSage V1.0 ⚽
🧠 Created by Habib (The Ghost Analyst)

Choose your role:
1. 🧤 Keeper Mode (Save the shot)
2. ⚽ Striker Mode (Score the goal)
Enter 1 or 2: 2

⚽ Striker Mode Activated!
Score 5 goals to win!

Which direction do you shoot? ('up', 'down', 'left', 'right'): up
GOAAALLL!! ⚽🔥 
Keeper had no chance! ⚽🔥
Score: 1/5
```

---

## 📜 License

This project is free to use for personal and educational purposes.
