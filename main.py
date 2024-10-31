sideA = float(input("Enter the first side of the triangle: "))
sideB = float(input("Enter the second side of the triangle: "))
sideC = float(input("Enter the third side of the triangle: "))
  
if (sideA + sideC) > sideB and (sideB + sideC) > sideA and (sideA + sideB) > sideC:
    if sideA == sideB == sideC:
        print("The triangle is equilateral.")
    elif sideA == sideB or sideA == sideC or sideB == sideC:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The triangle is invalid.")