# Showcase notebooks (one showcase + one extra per course part)

Every notebook was executed top to bottom and is saved with its outputs. The matching slides are on Moodle.

## Part 1 Showcase (after Lecture 3)

| File | What it does | Needs |
|---|---|---|
| `S1_part1_recap.ipynb` | **Start here.** The summary of Part 1 as one story: Pip opens a café. Every concept from L01-L03 in lecture order (print, comments, variables, types, math, input, conversion, f-strings, if/else), each with a reminder, café examples and Try it, then a counter program that uses everything, the full Part 1 Bug Zoo, a quiz and a cheat sheet | L01-L03 only |
| `S1_solar_system.ipynb` | "AI builds a solar system": the prompt we gave a PyCharm AI assistant, planets on circles (animation), the Moon and labels (follow-up prompts), then real gravity (orbit closes after 1 year, simulated years match NASA's 88/225/365/687 days) | L01-L03; lists, loops, functions and plots appear early and are marked "just run it" |
| `S1_solar_system_pycharm.py` | The same circles animation (with Moon and labels) as one script: run it in PyCharm and a window opens | Python + matplotlib on your computer |
| `S1x_everyday_python.ipynb` | Python for everyday life: life in numbers, km/miles and NIS/USD converter (example rate), bill splitter with tip, dice roll and Magic 8-ball | L01-L03 only (+ `import random`) |

**Open in Colab:** go to colab.research.google.com, choose File > Upload notebook, pick the `.ipynb` file, then run the cells from top to bottom. Everything uses tools Colab already has (math, random, matplotlib).

## Part 2 Showcase (after Lecture 6)

| File | What it does | Needs |
|---|---|---|
| `S2_part2_recap.ipynb` | **Start here.** The summary of Part 2, continuing the café story: discount rules with `elif` / `and` / `or`, bits and gates, the menu and the queue as lists, regular customers as sets, slicing the orders, `while` / `for` / `break`, the five loop recipes, then counter program 2.0 (whole menu, many items until `done`), the Part 2 Bug Zoo, a quiz and a cheat sheet | L04-L06 only |
| `S2_random_dots.ipynb` | "Randomness you can see": one die 6,000 times and two dice 10,000 times (why 7 wins, exact 6-of-36 count with a loop inside a loop), pictures from random dots (uniform square, bell cloud, ring and smiley kept with `if` / `and` / `not`), histograms incl. bus waiting times, Monte Carlo estimate of pi with darts (plot, convergence, animation) | L04-L06: `if`, lists, `while`, `for`, `range`, loop recipes. `import random` (Lecture 9 idea) and plotting (Lecture 10) are marked "just run it". One optional NumPy cell is clearly marked |
| `S2x_physics_ball.ipynb` | Physics with loops: drop a ball from 100 m in tiny time steps (`while`), compare with t = sqrt(2h/g), try step sizes, bounce with 80% kept and count bounces, the same drop on Earth vs the Moon (plot + animation) | L04-L06 (+ plotting, "just run it") |

**Open in Colab:** go to colab.research.google.com, choose File > Upload notebook, pick the `.ipynb` file, then run the cells from top to bottom. Everything uses tools Colab already has (random, math, matplotlib, numpy). Both notebooks are seeded, so the numbers match the slides.

## Part 3 Showcase - Poker simulator (+ extra: secret messages)

| Notebook | What it does | Needs |
|---|---|---|
| `S3_part3_recap.ipynb` | **Start here.** The summary of Part 3: the counter program cut into functions (`return`, defaults, scope), the menu becomes a dictionary (refactor moment), counting with `get`, seating tables and the day's orders as a list of dicts, median and quantiles by hand, reading tracebacks and print debugging, testing an AI-written median, then counter program 3.0 with a daily report, the Part 3 Bug Zoo, a quiz and a cheat sheet | L07-L08 only |
| `S3_poker.ipynb` | Builds a 52-card deck with nested loops, names poker hands with functions + dictionaries (counts, sets, rank values), catches the A-2-3-4-5 bug with a mini test table, simulates 100,000 hands and compares them with the exact `math.comb` counts, simulates roulette (house edge 2.7%), and plays a two-player mini-game | L05-L08 (lists, sets, slicing, loops, functions, dictionaries, debugging). `random`/`math` imports (L09) and the matplotlib drawing code (L10) are marked "just run it" |
| `S3x_secret_messages.ipynb` | Caesar cipher with `encrypt`/`decrypt`, ROT13, brute-force breaking (all 26 shifts), letter-frequency breaking with a dictionary + bar chart, why 128-bit keys are safe, and a final message to crack | L05-L08. matplotlib (L10) only for the chart |

Open in Colab: go to colab.research.google.com, choose File > Upload notebook, and pick the `.ipynb` file (or open it from Google Drive / GitHub). Then Runtime > Run all. Nothing to install, no files to download.
Both notebooks are seeded (`random.seed(7)`), so the numbers match the slides. The full poker notebook runs in about 10 seconds.

## Part 4 Showcase (after Lecture 10)

| File | What it does | Needs |
|---|---|---|
| `S4_part4_recap.ipynb` | **Start here.** The summary of Part 4 and the whole course: NumPy (VAT in one line, filters, the hand-made median vs `np.median`, a 2-D sales table), Pip's logo as pixels, a week of orders in Pandas, line / bar / scatter / histogram, regression (iced coffee vs temperature), classification (hot or iced), clustering (kinds of customers), objects and methods, a mini final project in five steps, the Part 4 Bug Zoo, a quiz, a cheat sheet and the four-part journey | L09-L10 (data built inside, no upload needed) |
| `S4_digits_ai.ipynb` | "Teach a computer to see": the 1,797 handwritten 8x8 digits from `load_digits()` (gallery, one image as a table of numbers), a practice exam / real exam split, a ladder of three models with the same create-fit-predict recipe (k-nearest neighbours 98.2%, decision tree 85.8% with a readable 2-question tree, small neural network 96.0%), scoreboard, the best model's mistakes and a confusion matrix, more examples = better results, inside the network (3,760 knobs, loss curve, the 10 outputs), how the idea scales up, limits (shifted, inverted and noise images fool it) and "draw your own digit" | L01-L10, especially L09 (NumPy, images as arrays) and L10 (Matplotlib, scikit-learn). New scikit-learn tools (`train_test_split`, `DecisionTreeClassifier`, `MLPClassifier`, `ConfusionMatrixDisplay`) are explained where they are used |
| `S4x_monte_carlo_money.ipynb` | "Will my savings reach the goal?": a toy plan (1,000 NIS a month for 5 years, random monthly returns), mattress vs steady growth, one random future, 1,000 futures (50 drawn + median), histogram of endings, chance to reach 65,000 NIS, bad / typical / good luck percentiles, and a "what if" comparison of plans. Clearly labelled: toy model, made-up numbers, not financial advice | L06-L10: loops, functions, NumPy random and percentiles, Pandas table, Matplotlib |

**Open in Colab:** go to colab.research.google.com, choose File > Upload notebook, pick the `.ipynb` file, then Runtime > Run all. Everything uses tools Colab already has (numpy, pandas, matplotlib, scikit-learn). The digits ship with scikit-learn, so nothing is downloaded.
Both notebooks are seeded (`random_state=7`, `np.random.default_rng(7)`), so the numbers match the slides (checked with scikit-learn 1.9.1). The digits notebook runs in about 10 seconds.

