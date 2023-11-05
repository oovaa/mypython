import pandas as pd

clothes = pd.DataFrame(
    {
        "type": ["pants", "shirt", "shirt", "pants", "shirt", "pants"],
        "color": ["red", "blue", "green", "blue", "green", "red"],
        "price_usd": [20, 35, 50, 40, 100, 75],
        "mass_g": [125, 440, 680, 200, 395, 485],
    }
)

data = {
    "planet": [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ],
    "radius_km": [2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622],
    "moons": [0, 0, 1, 2, 80, 83, 27, 14],
}
df = pd.DataFrame(data)

moons_loc = df.loc[:, "moons"]
print("Using loc:")
print(moons_loc)

# Using iloc
moons_iloc = df.iloc[:, df.columns.get_loc("moons")]
print("\nUsing iloc:")
print(moons_iloc)

# print(clothes)
# print(df)
# mask = (df["moons"] > 20) & (df["moons"] != 80) & (df["radius_km"] >= 50000)
# print(df[mask])
