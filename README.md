# SC497-final-project
BioStats Helper v2.0

A polished, professional statistical analysis tool built for SC497. This project simulates a realistic biological dataset and provides a suite of statistical analyses, visualizations, and export features — all wrapped in a clean, user-friendly terminal interface.

Overview

BioStats Helper v2.0 is a standalone Python application designed to help users explore statistical concepts without requiring external data files. It generates a realistic biological dataset and offers multiple analysis tools including t-tests, correlations, ANOVA, heatmaps, and more.

The application includes:

A polished ASCII banner and colorized UI

Realistic biological dataset generation

Multiple statistical tests and visualizations

Export options for results, plots, and datasets

A help/about screen for quick reference

Features

Realistic Biological Dataset: Includes systolic blood pressure, heart rate, and cholesterol for control and treatment groups.

Dataset Summary: View descriptive statistics and missing value counts.

Independent t-test: Compare two groups with visual boxplots.

Correlation Analysis: Pearson correlation with regression plot.

Correlation Heatmap: Visualize relationships between all numeric variables.

One-Way ANOVA: Compare means across groups.

Save Dataset to CSV: Export the generated dataset.

Save Plots: Save visualizations as PNG files.

Export Results: Save statistical outputs to timestamped text files.

View Raw Data: Preview the first 10 rows.

Regenerate Dataset: Create a fresh dataset at any time.

Help/About Screen: Quick overview of features.

How to Run

Ensure Python 3.11+ is installed.

Install required dependencies:

pip install pandas numpy matplotlib seaborn scipy

Run the application:

python src/biostats_helper.py (or whatever you want honestly)

Project Structure

SC497-final-project/
│── src/
│     └── biostats_helper.py
│── results/            # auto-created when exporting results
│── plots/              # auto-created when saving plots
│── screenshots/        # optional, for README visuals
│── README.md
│── requirements.txt
│── pyproject.toml
│── .gitignore

Example Output

Menu

1. Dataset Summary
2. Independent t-test
3. Correlation Analysis
4. Correlation Heatmap
5. One-Way ANOVA
6. Save Dataset to CSV
7. View Raw Data
8. Regenerate Dataset
9. Help / About
0. Quit

Sample Dataset Preview

     group  systolic_bp  heart_rate  cholesterol
0  Control   123.97       73.68       170.50
1  Control   118.89       77.14       205.74
2  Control   125.18       83.86       213.17

Dependencies

pandas

numpy

matplotlib

seaborn

scipy

These can be installed via requirements.txt.

Future Improvements

Add GUI or web interface (Streamlit)

Add more statistical tests (paired t-test, regression)

Add interactive plot controls

Add user-uploaded CSV support

Credits

Created by Ananya Sairanganthan for SC497.

BioStats Helper v2.0 is designed to demonstrate statistical analysis, data visualization, and Python application structure in a clean and professional way.
