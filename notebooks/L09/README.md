# L09 - NumPy & Pandas - notebooks

| File | Used on slide | What it contains |
|---|---|---|
| `L09_01_numpy_basics.ipynb` | import: open the toolbox, Meet the array, List vs array, Add 17% VAT, Two arrays item by item, Ask the array a question, Statistics in one word each, 2-D arrays in code, Average per student / per test, Try it!, Predict the output | `import numpy as np`, `np.sqrt`/`np.pi`, `np.array` of coffee prices, list `* 2` vs array `* 2`, VAT loop vs `prices * 1.17`, final grade `0.3 * homework + 0.7 * exam`, `prices > 12` and `prices[prices > 12]`, `np.mean/median/percentile/max`, 3x4 grades table: `shape`, `grades[1, 2]`, `max()`, `mean(axis=0/1)`; exercise cells for the Try it! tasks and the quiz `a[a > 15] - 10` |
| `L09_02_cat_filters.ipynb` | Load a real photo, Show the array as a picture, Filter 1-3, Photo filters are just math, Try it!, Predict the output | `from skimage import data; cat = data.chelsea()`, `cat.shape`, `cat[150, 170]`, `plt.imshow`, `255 - cat`, crop `cat[70:210, 110:350]`, `cat.mean(axis=2)` with `cmap="gray"`, `cat[::-1]`, `cat[:, ::-1]`, `cat // 2`, `gray > 100`; exercise cells (crop the nose, combine filters, change the threshold, upload your own photo); quiz `cat[0:100, 0:50].shape` |
| `L09_03_coffee_pandas.ipynb` | A DataFrame from a dictionary, Real data lives in CSV files, Read the CSV, One column = one array, Filter rows (lattes, expensive), Which drink is the most popular?, describe(), Try it!, Predict the output | `pd.DataFrame` from the `menu` dict, upload + `pd.read_csv("coffee_orders.csv")`, `head()`, column `sum/mean/median/quantile(0.9)`, `df[df["drink"] == "Latte"]`, `df[df["price"] >= 19]`, `value_counts()`, `describe()`; exercise cells (orders on Wednesday, average Tea rating, busiest day); quiz on `df[df["price"] < 17]` |
| `L09_04_bug_zoo.ipynb` | Bug Zoo: the forgotten import, Bug Zoo: file and column names | one cell per bug: `np` used before `import numpy as np`, `list * 1.17`, misspelled CSV file name (`FileNotFoundError`), `df["Price"]` (`KeyError`), each followed by a text cell with the fix |

## Data

| File | What it is |
|---|---|
| `data/coffee_orders.csv` | Made-up toy data for this course: 40 orders at a campus café (Sun-Thu), columns `day, drink, size, price, rating`. Students upload it to Colab before `read_csv`. |
