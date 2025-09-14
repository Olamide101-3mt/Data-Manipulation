import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

def main():
    print("=== Python Week 7 Assignment ===\n")

    # ==============================
    # Task 1: Load and Explore Dataset
    # ==============================
    print("Task 1: Loading and Exploring the Dataset...\n")

    try:
        # Load the Iris dataset from sklearn
        iris = load_iris(as_frame=True)
        df = iris.frame

        # Display first few rows
        print("First 5 rows of the dataset:")
        print(df.head(), "\n")

        # Explore data structure
        print("Data types:")
        print(df.dtypes, "\n")

        print("Missing values:")
        print(df.isnull().sum(), "\n")

        # Clean dataset (Iris dataset has no missing values, but example shown)
        df = df.dropna()  # or df.fillna(method="ffill")

    except FileNotFoundError:
        print("Error: The dataset file was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # ==============================
    # Task 2: Basic Data Analysis
    # ==============================
    print("Task 2: Basic Data Analysis...\n")

    # Compute statistics
    print("Summary statistics:")
    print(df.describe(), "\n")

    # Group by species and compute mean of numerical columns
    print("Mean values grouped by species:")
    print(df.groupby("target").mean(), "\n")

    # Identify patterns
    print("Observation: Sepal length and width vary across species, "
          "Petal measurements are most distinct.\n")

    # ==============================
    # Task 3: Data Visualization
    # ==============================
    print("Task 3: Creating Visualizations...\n")
    sns.set(style="whitegrid")

    # Line chart (example: cumulative petal length over rows)
    plt.figure(figsize=(8, 5))
    df["petal length (cm)"].cumsum().plot(kind="line", color="blue")
    plt.title("Cumulative Petal Length Trend")
    plt.xlabel("Index")
    plt.ylabel("Cumulative Petal Length (cm)")
    plt.show()

    # Bar chart: average petal length per species
    plt.figure(figsize=(8, 5))
    sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean")
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species (0=Setosa, 1=Versicolor, 2=Virginica)")
    plt.ylabel("Petal Length (cm)")
    plt.show()

    # Histogram: sepal width
    plt.figure(figsize=(8, 5))
    plt.hist(df["sepal width (cm)"], bins=15, color="green", edgecolor="black")
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot: sepal length vs petal length
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="sepal length (cm)", y="petal length (cm)",
                    hue="target", data=df, palette="deep")
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()

    print("✅ Assignment completed successfully!")

if __name__ == "__main__":
    main()
