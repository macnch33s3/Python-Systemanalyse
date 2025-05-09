# SystemAnalyse

**SystemAnalyse** is a Python tool for collecting, analyzing, and visualizing system performance data using [Pandas](https://pandas.pydata.org/). Used in the Modul MOSIM for analyzing csv-data, all organized in structured DataFrames.

## 🔧 Features

- Collect, read csv
- Organize and process data with **Pandas**
- Perform advanced analysis (filtering, grouping, time series, etc.)
- Export to CSV, Excel, or JSON
- Optional visualization with Matplotlib or Seaborn

## 📦 Installation

```bash
git clone https://github.com/yourusername/SystemAnalyse.git
cd SystemAnalyse
pip install -r requirements.txt
```

## 🐍 Requirements

```bash
pandas
psutil
matplotlib  # optional for visualization
seaborn     # optional
```

## 📁 Project Structure

```bash
SystemAnalyse/
├── systemanalyse/
│   ├── __init__.py
│   ├── collect.py         # Data collection using psutil
│   └── analysis.py        # Analysis functions using Pandas
├── tests/
│   └── test_collect.py
├── requirements.txt
└── README.md
```
