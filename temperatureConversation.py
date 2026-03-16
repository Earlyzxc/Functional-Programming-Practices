#Using Lambda as Temporary Function
to_celsius             = lambda f: round((f - 32) * 5/9, 2)
to_fahrenheit          = lambda c: round((c * 9/5) + 32, 2)
to_kelvin              = lambda c: round(c + 273.15, 2)
to_celsius_from_kelvin = lambda k: round(k - 273.15, 2)

print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("Choose (1/2/3/4): ")
temp = float(input("Enter temperature: "))

if choice == "1":
    print(f"{temp}°F = {to_celsius(temp)}°C")
elif choice == "2":
    print(f"{temp}°C = {to_fahrenheit(temp)}°F")
elif choice == "3":
    print(f"{temp}°C = {to_kelvin(temp)}K")
elif choice == "4":
    print(f"{temp}K = {to_celsius_from_kelvin(temp)}°C")
else:
    print("Invalid choice!")
