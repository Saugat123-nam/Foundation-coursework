# ST4015CMD — Foundations of Computer Science
**Krish Adhikari (250487)**

Implements all three report tasks in Python:
- **Task 1** — Encoding schemes (ASCII, Base64, Hex, URL)
- **Task 2** — P vs NP seating arrangement (brute force + heuristic)
- **Task 3 & 4** — Normalized SQLite database + SQL operations

---

## Project Structure

```
project/
├── main.py               # Entry point — runs all tasks
├── src/
│   ├── encoding.py       # Task 1
│   ├── seating.py        # Task 2
│   └── database.py       # Task 3 & 4
├── db/                   # SQLite database (auto-generated)
├── .vscode/
│   ├── launch.json       # Run configs for VS Code
│   └── settings.json
├── Dockerfile
├── requirements.txt
└── .gitignore
```

---

## Run Locally (VS Code)

```bash
# 1. Open project in VS Code
code .

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 3. Run
python main.py
```

Or use the **Run and Debug** panel (F5) and select a configuration.

---

## Run with Docker

```bash
# Build
docker build -t st4015cmd .

# Run
docker run --rm st4015cmd
```

---

## Git Setup

```bash
git init
git add .
git commit -m "Initial commit: encoding, seating, database modules"

# Push to GitHub
git remote add origin https://github.com/<your-username>/st4015cmd.git
git push -u origin main
```
