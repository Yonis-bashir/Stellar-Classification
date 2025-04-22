from datetime import datetime
import pandas as pd


# Placeholder data till jag lägger till csv filen för stjärnorna
data = {
    "Star Name": ["Placeholder A", "Placeholder B", "Placeholder C"],
    "Distance (ly)": [10.5, 22.0, 45.8],
    "Type": ["Main Sequence", "Red Giant", "White Dwarf"]
}
stars_df = pd.DataFrame(data)


birthday_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthday = datetime.strptime(birthday_input, "%Y-%m-%d")
today = datetime.now()


age_years = (today - birthday).days // 365
print(f"\nYou are approximately {age_years} years old.")


stars_df["Distance Difference"] = abs(stars_df["Distance (ly)"] - age_years)
matched_star = stars_df.sort_values("Distance Difference").iloc[0]


print("\n Your Birthday Star:")
print(f" Name: {matched_star['Star Name']}")
print(f" Distance: {matched_star['Distance (ly)']} light-years")
print(f" Type: {matched_star['Type']}")
print(f" The light from this star left around the year {birthday.year}.")
