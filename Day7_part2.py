# Here I have cheated :)
# GPT told me the answer...

import numpy as np

file_path = "input_day7.txt"

# read file
with open(file_path, "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]

ROWS = len(lines)
COLS = len(lines[0])
START_COL = lines[0].index("S")
START_ROW = 1

def count_paths_exact(lines):
    rows = len(lines)
    cols = len(lines[0])

    dp = np.zeros(cols, dtype=np.int64)
    dp[START_COL] = 1

    for r in range(START_ROW, rows):
        new = np.zeros(cols, dtype=np.int64)
        for c in range(cols):
            ways = dp[c]
            if ways == 0:
                continue

            cell = lines[r][c]
            if cell == ".":
                new[c] += ways
            elif cell == "^":
                if c > 0:
                    new[c - 1] += ways
                if c < cols - 1:
                    new[c + 1] += ways
            else:
                new[c] += ways

        dp = new

    return int(dp.sum())

print("rows:", ROWS, "cols:", COLS, "start_col:", START_COL)
print("Exact number of paths:", count_paths_exact(lines))