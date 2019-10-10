height = float(input("Input your height in Inches: "))
weight = float(input("Input your weight in Pounds: "))
print("Your body mass index is: ", round(703 * (weight / (height * height)), 2))