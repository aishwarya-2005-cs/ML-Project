import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATA
# -------------------------------
print("📊 Loading dataset...")
df = pd.read_csv("Traffic.csv")

print(df.head())

# -------------------------------
# SIMPLE ANALYSIS
# -------------------------------
print("\n📈 Basic Info:")
print(df.info())

print("\n📊 Description:")
print(df.describe())

# -------------------------------
# VISUALIZATION
# -------------------------------
print("\n📊 Plotting data...")

plt.figure()
plt.bar(df['City'][:10], df['AverageTCI'][:10])
plt.xticks(rotation=45)
plt.title("Top 10 Cities - Traffic Index")
plt.ylabel("Average Traffic Index")
plt.show()

# -------------------------------
# TRAFFIC LEVEL CLASSIFICATION
# -------------------------------
def traffic_level(tci):
    if tci < 20:
        return "🟢 Low Traffic"
    elif tci < 40:
        return "🟡 Medium Traffic"
    else:
        return "🔴 High Traffic"

print("\n🚦 Traffic Levels:")

for i in range(5):
    city = df.iloc[i]['City']
    tci = df.iloc[i]['AverageTCI']
    print(city, "→", traffic_level(tci))

print("\n✅ Project Running Successfully!")