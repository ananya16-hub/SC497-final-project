import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# ---------------------------------------------------------
# Instead of loading a CSV, we load a built‑in dataset
# ---------------------------------------------------------
def load_data():
    df = pd.DataFrame({
        "group": ["A", "A", "A", "B", "B", "B"],
        "value": [5, 7, 6, 10, 12, 11],
        "height": [60, 62, 61, 70, 72, 71]
    })
    print("\nLoaded built‑in sample dataset:")
    print(df.head())
    return df


def get_numeric_columns(df):
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        print("No numeric columns found in this dataset.")
    else:
        print("\nNumeric columns detected:")
        for i, col in enumerate(numeric_cols):
            print(f"{i+1}. {col}")
    return numeric_cols


def choose_column(columns, prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(columns):
                return columns[choice - 1]
            else:
                print("Please enter a valid number from the list.")
        except ValueError:
            print("Please enter a number.")


def run_ttest(df):
    print("\n=== Independent t-test ===")

    print("\nAvailable columns:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. {col}")
    group_col = choose_column(df.columns.tolist(), "Choose grouping (categorical) column (number): ")

    numeric_cols = get_numeric_columns(df)
    if not numeric_cols:
        return
    value_col = choose_column(numeric_cols, "Choose numeric outcome column (number): ")

    data = df[[group_col, value_col]].dropna()

    # FIXED: ensure Series, not DataFrame
    groups = data[group_col].astype(str).unique()

    if len(groups) != 2:
        print(f"\nSelected grouping column has {len(groups)} levels; t-test requires exactly 2.")
        return

    group1 = data[data[group_col] == groups[0]][value_col]
    group2 = data[data[group_col] == groups[1]][value_col]

    t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False)

    print("\n--- T-test Results ---")
    print(f"Groups: {groups[0]} vs {groups[1]}")
    print(f"t-statistic: {t_stat:.4f}")
    print(f"p-value: {p_val:.4g}")

    alpha = 0.05
    if p_val < alpha:
        print(f"\nInterpretation: p < {alpha}, so the difference is statistically significant.")
    else:
        print(f"\nInterpretation: p ≥ {alpha}, so the difference is NOT statistically significant.")

    print("\nGenerating boxplot...")
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=group_col, y=value_col, data=data)
    plt.title(f"{value_col} by {group_col}")
    plt.tight_layout()
    plt.show()


def run_correlation(df):
    print("\n=== Correlation Analysis ===")

    numeric_cols = get_numeric_columns(df)
    if len(numeric_cols) < 2:
        print("Need at least two numeric columns for correlation.")
        return

    x_col = choose_column(numeric_cols, "Choose X variable (number): ")
    y_col = choose_column(numeric_cols, "Choose Y variable (number): ")

    if x_col == y_col:
        print("Please choose two different variables.")
        return

    data = df[[x_col, y_col]].dropna()

    r_val, p_val = stats.pearsonr(data[x_col], data[y_col])

    print("\n--- Correlation Results ---")
    print(f"Variables: {x_col} and {y_col}")
    print(f"Pearson r: {r_val:.4f}")
    print(f"p-value: {p_val:.4g}")

    alpha = 0.05
    if p_val < alpha:
        print(f"\nInterpretation: p < {alpha}, so the correlation is statistically significant.")
    else:
        print(f"\nInterpretation: p ≥ {alpha}, so the correlation is NOT statistically significant.")

    print("\nGenerating scatterplot with regression line...")
    plt.figure(figsize=(6, 4))
    sns.regplot(x=x_col, y=y_col, data=data, line_kws={"color": "red"})
    plt.title(f"{y_col} vs {x_col}")
    plt.tight_layout()
    plt.show()


def main():
    print("=== BioStats Helper (Python Final Project) ===")

    # NO CSV. Just load built‑in data.
    df = load_data()

    while True:
        print("\nChoose an analysis:")
        print("1. Independent t-test (two groups)")
        print("2. Correlation (two numeric variables)")
        print("3. Quit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            run_ttest(df)
        elif choice == "2":
            run_correlation(df)
        elif choice == "3":
            print("Exiting BioStats Helper. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
