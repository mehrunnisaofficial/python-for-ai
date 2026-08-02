# ==========================================================
# Area of a Rectangle
# ==========================================================

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

unit = input("Enter the unit (cm, m, ft, in): ").strip().lower()

area = length * breadth

print(f"The area of the rectangle is {area:,.2f} {unit}².")