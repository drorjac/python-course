# L10 - Plots, ML & Wrap-up - notebooks

| File | Used on slide | What it contains |
|---|---|---|
| `L10_01_plots.ipynb` | Your first line plot, Always add a title and labels, Two lines on one plot, Bar chart, Scatter plot, Histogram, Try it!, Predict the plot | `import matplotlib.pyplot as plt`; exam-week sleep line plot (plain, then with `marker`, `title`, `xlabel`, `ylabel`); me vs Noa with `label` + `legend()`; bar chart of `df["drink"].value_counts()` from `coffee_orders.csv`; study hours vs grade `scatter`; `np.random.seed(0)` + `np.random.normal(72, 9, 300)` histogram; exercise cells (own data, orders per day bar chart, change `bins`); quiz `plt.plot([1, 2, 3], [3, 2, 1])` |
| `L10_02_first_ml.ipynb` | Regression: predict a grade, What did the model learn?, Careful: models don't know common sense, Classification in code, Clustering, Let's see the groups, Try it!, Predict the output | `LinearRegression` on hours (as `[[1], [2], ...]`) and grades, `predict([[7]])`, plot of dots + learned line, `predict([[30]])` (201!); `KNeighborsClassifier(n_neighbors=3)` on fruit `[weight, redness]` with apple/banana labels, `predict([[155, 7], [118, 3]])`; `KMeans(n_clusters=3, random_state=0).fit_predict` on `cafe_customers.csv` + `plt.scatter(..., c=groups)` before/after; exercise cells (0 and 10 hours, new fruit `[140, 5]`, `n_clusters` 2 and 4); quiz on the 3-point regression |
| `L10_03_project_starter.ipynb` | A mini project step 1 and step 2, Final project details | mini project: income per day from `coffee_orders.csv` with a loop + filter + `int(...sum())`, then `plt.bar(days, totals)` with title and label; an empty project template (question, load, explore, numbers, a small `Group` class, plots, conclusion) |
| `L10_04_bug_zoo.ipynb` | Bug Zoo: plotting bugs, Bug Zoo: the 2-D surprise | one cell per bug: x and y of different length in `plt.plot`, `plt.xlable` (`AttributeError`, Python suggests `'table'`), `LinearRegression().fit` with a 1-D list (`ValueError: Expected 2D array...`), each followed by a text cell with the fix |
| `debug_demo.py` | The debugger: pause the program, Step by step: watch the variables | a plain Python file for the IDE demo: `total_price` with `total = 0` inside the loop (prints 30, not 60); steps for a breakpoint and Step Over in the docstring |

## Data

| File | What it is |
|---|---|
| `data/coffee_orders.csv` | Same made-up café data as L09 (40 orders, columns `day, drink, size, price, rating`). |
| `data/cafe_customers.csv` | Made-up toy data for this course: 30 café customers, columns `visits` (per month) and `spend` (average ILS), built as three loose groups for the KMeans demo. |
