import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def load_data(path):
    """Load a CSV file into a pandas DataFrame."""
    try:
        df = pd.read_csv(path)
        print("\nFile loaded successfully!\n")
        print("Preview of data:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


def get_numeric_columns(df):
    """Return a list of numeric column names."""
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        print("No numeric columns found in this dataset.")
    else:
        print("\nNumeric columns detected:")
        for i, col in enumerate(numeric_cols):
            print(f"{i+1}. {col}")
    return numeric_cols


def choose_column(columns, prompt):
    """Let the user choose a column from a list by index."""
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
    """Run an independent t-test on one numeric column split by a categorical column."""
    print("\n=== Independent t-test ===")

    # Choose grouping column (categorical-like)
    print("\nAvailable columns:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. {col}")
    group_col = choose_column(df.columns.tolist(), "Choose grouping (categorical) column (number): ")

    # Choose numeric column
    numeric_cols = get_numeric_columns(df)
    if not numeric_cols:
        return
    value_col = choose_column(numeric_cols, "Choose numeric outcome column (number): ")

    data = df[[group_col, value_col]].dropna()
    groups = data[group_col].unique()

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
        interp = (
            f"The p-value ({p_val:.4g}) is less than 0.05, "
            "suggesting a statistically significant difference between the two groups."
        )
    else:
        interp = (
            f"The p-value ({p_val:.4g}) is greater than 0.05, "
            "suggesting no statistically significant difference between the two groups."
        )

    print("\nInterpretation:")
    print(interp)

    # Boxplot
    print("\nGenerating boxplot...")
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=group_col, y=value_col, data=data)
    plt.title(f"{value_col} by {group_col}")
    plt.tight_layout()
    plt.show()


def run_correlation(df):
    """Run Pearson correlation between two numeric columns."""
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
        sig_text = "statistically significant"
    else:
        sig_text = "not statistically significant"

    if abs(r_val) < 0.2:
        strength = "very weak"
    elif abs(r_val) < 0.4:
        strength = "weak"
    elif abs(r_val) < 0.6:
        strength = "moderate"
    elif abs(r_val) < 0.8:
        strength = "strong"
    else:
        strength = "very strong"

    interp = (
        f"The correlation between {x_col} and {y_col} is {strength} "
        f"({r_val:.2f}), and the relationship is {sig_text} at the 0.05 level."
    )

    print("\nInterpretation:")
    print(interp)

    # Scatterplot with regression line
    print("\nGenerating scatterplot with regression line...")
    plt.figure(figsize=(6, 4))
    sns.regplot(x=x_col, y=y_col, data=data, line_kws={"color": "red"})
    plt.title(f"{y_col} vs {x_col}")
    plt.tight_layout()
    plt.show()


def main():
    print("=== BioStats Helper (Python Final Project) ===")
    path = input("Enter path to your CSV file: ").strip()

    df = load_data(path)
    if df is None:
        return

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