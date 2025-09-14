Data Exploration, Analysis & Visualization
📌 Overview

This project explores a dataset using Pandas, performs basic statistical analysis, and creates visualizations with Matplotlib and Seaborn.

The dataset used here is the classic Iris dataset, a popular dataset for learning data analysis and visualization techniques.

🎯 Tasks Covered
Loading and Exploring  Dataset

Load dataset in CSV format (Iris dataset via sklearn.datasets.load_iris() was used here).

Display first few rows with .head().

Inspect data structure, types, and missing values.

Handle missing values (dropna or fillna).

✅ Basic Data Analysis

Compute statistics (mean, median, standard deviation) using .describe().

Group by categorical column (species) and compute mean values.

Identify interesting patterns (e.g., petal measurements are most distinct across species).

✅  Data Visualization

Created 4 different types of plots with proper titles, labels, and legends:

📈 Line Chart – Trend of cumulative petal length.

📊 Bar Chart – Average petal length per species.

📉 Histogram – Distribution of sepal width.

⚪ Scatter Plot – Sepal length vs. petal length (colored by species).

🛠️ Technologies Used

Python 3

Pandas → Data loading, cleaning, and analysis

Matplotlib → Plotting charts

Seaborn → Enhanced visualizations

Scikit-learn → Access to Iris dataset

🚀 How to Run the Project

Clone the repository:

git clone https://github.com/your-username/Data-Manipulation.git
cd python-week7-assignment


Install required libraries:

pip install pandas matplotlib seaborn scikit-learn


Run the script:

python week7_assignment.py


View results in the terminal and interactive charts (they will open in new windows).

📂 Project Structure
├── Data.py   # Main Python script
├── README.md             

📝 Observations & Insights

Petal features (length & width) provide the clearest separation between species.

Sepal features overlap more but still show patterns.

Virginica species generally has the largest petal measurements.
