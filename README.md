# SC497-final-project
<p align="center">
  <img src="https://img.shields.io/badge/python-3.11%2B-blue?logo=python&logoColor=white" alt="Python 3.11+"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"/>
  <img src="https://img.shields.io/badge/release-v1.0.0-orange" alt="Release v1.0.0"/>
  <img src="https://img.shields.io/badge/status-stable-brightgreen" alt="Status: Stable"/>
</p>

<h1 align="center">🧬 BioStats Helper v2.0</h1>

<p align="center">
  <em>A polished, professional statistical analysis tool built for SC497.</em><br/>
  Simulates realistic biological datasets &bull; Full suite of statistical analyses &bull; Beautiful visualizations &bull; Clean terminal UI
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Example Output](#-example-output)
- [Reproducibility](#-reproducibility)
- [Dependencies](#-dependencies)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Contributors](#-contributors)

---

## 🔬 Overview

**BioStats Helper v2.0** is a standalone Python application designed to help users explore statistical concepts without requiring external data files. It generates a realistic biological dataset and offers multiple analysis tools including t-tests, correlations, ANOVA, heatmaps, and more.

The application includes:

- 🎨 A polished ASCII banner and colorized UI
- 🧪 Realistic biological dataset generation
- 📊 Multiple statistical tests and visualizations
- 💾 Export options for results, plots, and datasets
- ❓ A help/about screen for quick reference

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Realistic Biological Dataset** | Includes systolic blood pressure, heart rate, and cholesterol for control and treatment groups |
| **Dataset Summary** | View descriptive statistics and missing value counts |
| **Independent t-test** | Compare two groups with visual boxplots |
| **Correlation Analysis** | Pearson correlation with regression plot |
| **Correlation Heatmap** | Visualize relationships between all numeric variables |
| **One-Way ANOVA** | Compare means across groups |
| **Save Plots** | Save visualizations as PNG files |
| **Export Results** | Save statistical outputs to timestamped text files |
| **View Raw Data** | Preview the first 10 rows |
| **Regenerate Dataset** | Create a fresh dataset at any time |
| **Help/About Screen** | Quick overview of features |

---

## 🛠️ Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/ananya16-hub/SC497-final-project.git
   cd SC497-final-project
   ```

2. **Ensure Python 3.11+ is installed:**

   ```bash
   python --version
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```

---

## 🚀 Usage

Run the application from the project root:

```bash
python src/biostats_helper.py
```

You'll be greeted with a colorized menu where you can select any analysis option by number. Results can be exported to the `results/` and `plots/` directories automatically.

---

## 📁 Project Structure

```
SC497-final-project/
├── src/
│   └── biostats_helper.py      # Main application
├── results/                     # Auto-created when exporting results
├── plots/                       # Auto-created when saving plots
├── screenshots/                 # Optional — for README visuals
├── README.md                    # You are here!
├── requirements.txt             # Python dependencies
├── pyproject.toml               # Project metadata
├── LICENSE                      # MIT License
└── .gitignore                   # Git ignore rules
```

---

## 📸 Screenshots

> _Add your own screenshots here to showcase the app in action!_

| Screenshot | Description |
|------------|-------------|
| ![Menu](screenshots/menu.png) | Main menu with colorized UI |
| ![t-test](screenshots/ttest.png) | Independent t-test with boxplot |
| ![Heatmap](screenshots/heatmap.png) | Correlation heatmap |
| ![Export](screenshots/export.png) | Exported results preview |

---

## 📋 Example Output

**Menu Options:**

```
 1. Dataset Summary
 2. Independent t-test
 3. Correlation Analysis
 4. Correlation Heatmap
 5. One-Way ANOVA
 6. Save Dataset to CSV
 7. View Raw Data
 8. Regenerate Dataset
 9. Help / About
10. Quit
```

**Sample Dataset Preview:**

```
   group  systolic_bp  heart_rate  cholesterol
0  Control       123.97       73.68       170.50
1  Control       118.89       77.14       205.74
2  Control       125.18       83.86       213.17
```

---

## 🔁 Reproducibility

This project is fully self-contained — no external data files are required:

1. The dataset is **generated programmatically** using `numpy` with realistic biological parameters.
2. All outputs (CSV, PNG plots, TXT results) are saved with **timestamps** for easy tracking.
3. Use **"Regenerate Dataset"** from the menu to create a fresh dataset for repeated analysis.
4. To reproduce exact results, set a random seed in the source code (see `biostats_helper.py`).

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computing and dataset generation |
| `matplotlib` | Static plot creation |
| `seaborn` | Statistical data visualization |
| `scipy` | Statistical tests (t-test, ANOVA, correlation) |

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- [ ] Add GUI or web interface (Streamlit)
- [ ] Add more statistical tests (paired t-test, regression)
- [ ] Add interactive plot controls
- [ ] Add user-uploaded CSV support

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Contributors

| Name | Role |
|------|------|
| **Ananya Sairanganthan** | Creator & Developer |

---

<p align="center">
  <strong>BioStats Helper v2.0</strong> is designed to demonstrate statistical analysis, data visualization, and Python application structure in a clean and professional way.<br/><br/>
  Made with ❤️ for SC497
</p>
