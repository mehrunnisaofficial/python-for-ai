import temp

celcius = float(input("Enter the cleclius degree: "))
print("\nFrom Celcius to farenhite\n")
farenhite = temp.ctf(celcius)
print(f"Answer = {celcius}° -> {farenhite}°")

farenhite2 = float(input("Enter the farenhite degree: "))
print("\nFrom farenhite to celcius\n")
celcius2 = temp.ftc(farenhite2)
print(f"Answer = {farenhite2}° -> {celcius2}°")
