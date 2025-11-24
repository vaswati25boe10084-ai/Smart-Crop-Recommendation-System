
# SMART CROP RECOMMENDATION SYSTEM  (Python Version)
# Converted from Prolog
# ------------------------------------------------------------

# Knowledge Base: same as Prolog facts
crops = [
    {"name": "rice",      "soil": "clay",  "season": "kharif", "min_rain": 100, "max_rain": 250, "min_ph": 5.0, "max_ph": 6.5},
    {"name": "wheat",     "soil": "loam",  "season": "rabi",   "min_rain": 50,  "max_rain": 120, "min_ph": 6.0, "max_ph": 7.5},
    {"name": "maize",     "soil": "loam",  "season": "kharif", "min_rain": 60,  "max_rain": 150, "min_ph": 5.5, "max_ph": 7.0},
    {"name": "bajra",     "soil": "sandy", "season": "kharif", "min_rain": 30,  "max_rain": 90,  "min_ph": 6.0, "max_ph": 7.5},
    {"name": "sugarcane", "soil": "clay",  "season": "annual", "min_rain": 150, "max_rain": 300, "min_ph": 6.0, "max_ph": 8.0},
    {"name": "cotton",    "soil": "black", "season": "kharif", "min_rain": 60,  "max_rain": 120, "min_ph": 5.5, "max_ph": 7.5},
    {"name": "groundnut", "soil": "sandy", "season": "kharif", "min_rain": 50,  "max_rain": 100, "min_ph": 6.0, "max_ph": 7.0},
    {"name": "chickpea",  "soil": "loam",  "season": "rabi",   "min_rain": 40,  "max_rain": 80,  "min_ph": 6.0, "max_ph": 8.0},
    {"name": "millets",   "soil": "sandy", "season": "kharif", "min_rain": 20,  "max_rain": 60,  "min_ph": 5.0, "max_ph": 8.0}
]


# ------------------------------------------------------------
# Rule: recommend crops based on soil, season, rainfall & pH
# ------------------------------------------------------------

def recommend_crop(soil, season, rainfall, ph):
    soil = soil.lower()
    season = season.lower()

    recommended = []

    for crop in crops:
        if (crop["soil"] == soil and
            crop["season"] == season and
            crop["min_rain"] <= rainfall <= crop["max_rain"] and
            crop["min_ph"] <= ph <= crop["max_ph"]):

            recommended.append(crop["name"])

    return recommended


# ------------------------------------------------------------
# Interactive Mode (similar to Prolog input menu)
# ------------------------------------------------------------

def main():
    print("\n========= SMART CROP RECOMMENDATION SYSTEM =========\n")

    soil = input("Enter soil type (clay/loam/sandy/black): ").strip().lower()
    season = input("Enter season (kharif/rabi/annual): ").strip().lower()
    rainfall = float(input("Enter rainfall (mm): "))
    ph = float(input("Enter soil pH: "))

    results = recommend_crop(soil, season, rainfall, ph)

    print("\nRecommended Crops:")
    if results:
        for r in results:
            print(f"- {r}")
    else:
        print("No suitable crops found.")

    print("\n====================================================\n")

if __name__ == "__main__":
    main()