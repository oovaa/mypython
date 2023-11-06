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


def categorize_planet(moons):
    if moons == 0:
        return "No"
    elif 1 <= moons <= 10:
        return "Few"
    else:
        return "Many"


# df["moon_category"] = df["moons"].apply(categorize_planet)
# df["newrds"] = (df["radius_km"] > 8000) | (df["moon_category"] == "No")

# grouped = df.groupby("moons").mean()

# print(grouped)

clothes = pd.DataFrame(
    {
        "type": ["pants", "shirt", "shirt", "pants", "shirt", "pants"],
        "color": ["red", "blue", "green", "blue", "green", "red"],
        "price_usd": [20, 35, 50, 40, 100, 75],
        "mass_g": [125, 440, 680, 200, 395, 485],
    }
)


grouped = clothes.groupby('type')
grouped.mean()


# df = df[df["newrds"] == True]
# Display the updated DataFrame
# print(df[["planet", "moons", "moon_category"]])

# df.drop("moon_category", axis=1, inplace=True)
# df.drop(7, axis=0, inplace=True)

# moons_loc = df.loc[1, ["radius_km", "planet"]]
# print("Using loc:")
# print(moons_loc)

# # Using iloc
# moons_iloc = df.iloc[4:6, :2]
# print("\nUsing iloc:")
# print(moons_iloc)

# print(clothes)
# print(df)
# mask = (df["moons"] > 20) & (df["moons"] != 80) & (df["radius_km"] >= 50000)
# print(df[mask])
