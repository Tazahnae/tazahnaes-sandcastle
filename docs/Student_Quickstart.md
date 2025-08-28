# 🎯 How to Complete Python Level 1 (STEAMforME)

Welcome to **Tazahnae’s SandCastle**! Follow this guide to complete Level 1 and earn your badge.  
You can work **entirely in the browser** (no installs), or work locally if you want.

---

## 🔗 Where do I start?

1) If your teacher gave you a **Classroom assignment link**, use that URL:  
   **Assignment URL:** <PASTE-CLASSROOM-URL-HERE>

2) If you’re using the template directly, open this repo and click **Use this template**:  
   **Template URL:** <https://github.com/Tazahnae/tazahnaes-sandcastle>  
   Name your copy, then click **Create repository from template**.

---

## 🛣️ Choose Your Path

### Path A — Edit on GitHub (No Installs) ✅
Best for beginners. Everything happens in the website.

1. Open your repo on GitHub.
2. Go to `python/level1/hello_01.py`
3. Click the ✏️ **pencil** to edit.
4. Read the instructions at the top of the file, write your code.
5. Scroll down → add a short commit message → **Commit changes**.
6. Repeat for the other files:  
   - `python/level1/variables_02.py`  
   - `python/level1/loops_03.py`  
   - `python/level1/functions_04.py`

**How do I know if I passed?**  
- Open the **Actions** tab or your Pull Request → look for a ✅ (tests passed) or ❌ (fix and try again).  
- If you don’t see Actions, ask your teacher to enable it (it’s already set up in this template).

### Path B — Work Locally (Optional, Advanced)
Use this if you want to run tests on your computer.

**Requirements:** Git + Python 3.10+ + (optional) Node for web track.

1. Clone your repo:
   ```bash
   git clone git@github.com:<your-username>/<your-repo>.git
   cd <your-repo>
	
python3 -m venv .venv
source .venv/bin/activate
pip install -r python/level1/requirements.txt

pytest python/level1/tests -q

git add .
git commit -m "solve: completed exercise"
git push

📦 Step 3: What’s in Level 1?
	•	python/level1/INTRO.md — overview + prompts + examples
	•	hello_01.py — Say Hello
	•	variables_02.py — Variables & Add
	•	loops_03.py — Loops & Lists
	•	functions_04.py — Is Even?
	•	Tests are in python/level1/tests/ (you don’t edit these)

⸻

📤 Step 4: How to Submit
	1.	Create a Pull Request titled:
Completed Level 1 – Python
	2.	In your PR description, paste your badge:![Loops Ninja](https://img.shields.io/badge/Python-Loops%20Ninja-blue)
	3.	Wait for teacher review (and the ✅ from tests).

⸻

🔑 Understanding Git Commands

Here are the 3 most important commands you’ll see:
	•	git commit -m "message"
Saves a snapshot of your work with a short message.
Think: “Save Game” with a description of what you changed.
	•	git push
Uploads your commits from your computer to GitHub (your online repo).
Think: “Send my saved progress to the cloud.”
	•	git pull
Downloads any new commits from GitHub to your computer.
Think: “Update my game with the latest changes.”

⸻
🧰 Common Gotchas
	•	I don’t see the ✏️ pencil.
You might not have permission. Make sure you’re in your copy of the repo (not the template), or fork it.
	•	“pytest: command not found” locally.
You didn’t activate the venv. Run:source .venv/bin/activate
	•	Imports failing.
Run tests from the repo root, not inside python/level1/tests/.
	•	I forgot my repo URL.
It’s on your GitHub profile under Repositories.

⸻

🏅 Badge

After Level 1 tests pass, paste this in your README or PR:PYTHON LOOPS NINJA
Good luck & have fun! 🎉
