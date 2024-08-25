from bs4 import BeautifulSoup

# Read the HTML file
with open("index.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Dictionary to store class names and their corresponding styles
styles_dict = {}

# Iterate over all elements with a 'class' attribute and inline styles
for element in soup.find_all(attrs={"class": True, "style": True}):
    class_name = element["class"][0]  # Get the first class name
    style = element["style"]  # Get the inline style

    # Add the style to the dictionary
    styles_dict[class_name] = style

    # Remove the inline style from the element
    del element["style"]

# Write the styles to a CSS file
with open("styles.css", "w") as css_file:
    for class_name, style in styles_dict.items():
        # Format the style content
        formatted_style = style.replace(";\n", ";\n    ")  # Add indentation
        css_file.write(f".{class_name} {{\n    {formatted_style}\n}}\n\n")

# Save the modified HTML file
with open("index.html", "w") as file:
    file.write(str(soup.prettify()))

print("CSS file generated and inline styles removed from HTML file!")