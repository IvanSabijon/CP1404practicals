NAME_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Beige": "#f5f5dc", "Black": "#000000",
                "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "Brown": "#a52a2a", "BurlyWood": "#deb887",
                "CadetBlue": "#5f9ea0", "Chocolate": "#d2691e"}


print(NAME_TO_CODE)
colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in NAME_TO_CODE:
        print(f"{colour_name} = {NAME_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name, enter a valid input")
    colour_name = input("Enter colour name: ")