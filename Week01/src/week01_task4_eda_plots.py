import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

CSV_PATH = "../data/cars.csv"
OUT_DIR = Path("../outputs")

df = pd.read_csv(CSV_PATH)

print("========== TASK 4: DATA EXPLORATION ==========")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("\nFirst 20 rows:\n")
print(df.head(20))

print("\nStatistical Summary:\n")
print(df.describe(include="all"))

OUT_DIR.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="HP", y="MPG")
plt.title("Scatter Plot: HP vs MPG")
plt.savefig(OUT_DIR / "scatter_HP_vs_MPG.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="MPG")
plt.title("Box Plot: MPG")
plt.savefig(OUT_DIR / "boxplot_MPG.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="HP")
plt.title("Box Plot: HP")
plt.savefig(OUT_DIR / "boxplot_HP.png", dpi=300, bbox_inches="tight")
plt.close()

print("\nSaved outputs:")
print(str(OUT_DIR / "scatter_HP_vs_MPG.png"))
print(str(OUT_DIR / "boxplot_MPG.png"))
print(str(OUT_DIR / "boxplot_HP.png"))
print("=============================================")
