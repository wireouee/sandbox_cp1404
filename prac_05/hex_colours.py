color_dictionary = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a",
                    "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                    "Amaranth": "#e52b50", "Amber": "#ffbf00",
                    "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                    "AntiqueWhite1": "	#ffefdb", "AntiqueWhite2": "#eedfcc",
                    "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378"}
print("Enter a blank one could stop the loop")
color_name = input("Enter a color name: ").title()
while color_name != "":
    if color_name in color_dictionary:
        print("{}: {}".format(color_name, color_dictionary[color_name]))
    else:
        print("Invalid colour name")
    color_name = input("Enter a color name: ").title()
