import random
import datetime
import math

print("========================================")
print("       GEOMETRIC SHAPE CALCULATOR")
print("========================================")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")
print("5. Trapezium")
print("6. Parallelogram")
print("7. Cube")
print("8. Cuboid")
print("9. Cylinder")
print("10. Cone")
print("11. Sphere")
print("12. Hemisphere")
print("========================================")

shapes = ("Circle", "Rectangle", "Square", "Triangle",
          "Trapezium", "Parallelogram", "Cube", "Cuboid",
          "Cylinder", "Cone", "Sphere", "Hemisphere")
#




formulas = {
    "Circle": "Area = 3.14 * r * r",
    "Rectangle": "Area = l * b",
    "Square": "Area = s * s",
    "Triangle": "Area = 0.5 * b * h",
    "Trapezium": "Area = 0.5 * (a + b) * h",
    "Parallelogram": "Area = b * h",
    "Cube": "Volume = s * s * s",
    "Cuboid": "Volume = l * b * h",
    "Cylinder": "Volume = 3.14 * r * r * h",
    "Cone": "Volume = (3.14 * r * r * h) / 3",
    "Sphere": "Volume = (4 * 3.14 * r * r * r) / 3",
    "Hemisphere": "Volume = (2 * 3.14 * r * r * r) / 3"
}

history = []

shape_set = {
    "Circle", "Rectangle", "Square", "Triangle",
    "Trapezium", "Parallelogram", "Cube", "Cuboid",
    "Cylinder", "Cone", "Sphere", "Hemisphere"
}
random_number = random.randint(1, 12)

print("Random Shape Number:", random_number)
print("Random Shape Suggestion:", shapes[random_number - 1])
choice = int(input("Enter your choice: "))



current_time = datetime.datetime.now()

print("Date:", current_time.date())
print("Time:", current_time.strftime("%H:%M:%S"))


#----------------------------------------------------------------------------------------
#CIRCLE
#------------------------------------------------------------------------------------------
if choice == 1:
    #Take radius as input 
    r = float(input("Enter radius: "))
    #check wheather radius is positive
    if r > 0:

        #Calculate area of circle
        area = math.pi * r * r
        circumference = 2 * math.pi * r  # calculate the circumference 

        # Display results
        print("Shape = Circle")
        print("Area =", area)
        print("Circumference =", circumference)
# store calculation in history
        history.append(("Circle", area))

    else:
        print("Radius must be greater than 0")
         
  #======================================================================
  # rectangle
  # =====================================================================                                                                                                                                                                                                                                                                                                                                                                                                                      #====================================================================

elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))

    if l > 0 and b > 0:
        area = l * b
        perimeter = 2 * (l + b)

        print("Shape = Rectangle")
        print("Area =", area)
        print("Perimeter =", perimeter)

        history.append(("Rectangle", area))

    else:
        print("Length and breadth must be greater than 0")
#===========================================================================
#square
#=============================================================================
elif choice == 3:
    s = float(input("Enter side: "))

    if s > 0:
        area = s * s
        perimeter = 4 * s

        print("Shape = Square")
        print("Area =", area)
        print("Perimeter =", perimeter)

        history.append(("Square", area))

    else:
        print("Side must be greater than 0")

#========================================================================
# TRIANGLE
# =======================================================================        

elif choice == 4:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))

    if b > 0 and h > 0:
        area = 0.5 * b * h

        print("Shape = Triangle")
        print("Area =", area)

        history.append(("Triangle", area))

    else:
        print("Base and height must be greater than 0")

#===============================================================================
# TRAPEZIUM
# ============================================================================        

elif choice == 5:
    a = float(input("Enter first parallel side: "))
    b = float(input("Enter second parallel side: "))
    h = float(input("Enter height: "))

    if a > 0 and b > 0 and h > 0:
        area = 0.5 * (a + b) * h

        print("Shape = Trapezium")
        print("Area =", area)

        history.append(("Trapezium", area))

    else:
        print("All values must be greater than 0")

#==================================================================================
#PARALLELOGRAM
#================================================================================
elif choice == 6:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))

    if b > 0 and h > 0:
        area = b * h

        print("Shape = Parallelogram")
        print("Area =", area)

        history.append(("Parallelogram", area))

    else:
        print("Base and height must be greater than 0")

#======================================================================================
# CUBE
# ===================================================================================        

elif choice == 7:
    s = float(input("Enter side: "))

    if s > 0:
        volume = s * s * s
        surface_area = 6 * s * s

        print("Shape = Cube")
        print("Volume =", volume)
        print("Surface Area =", surface_area)

        history.append(("Cube", volume))

    else:
        print("Side must be greater than 0")

#======================================================================================
# CUBOID
# =====================================================================================        

elif choice == 8:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))

    if l > 0 and b > 0 and h > 0:
        volume = l * b * h
        surface_area = 2 * (l * b + b * h + h * l)

        print("Shape = Cuboid")
        print("Volume =", volume)
        print("Surface Area =", surface_area)

        history.append(("Cuboid", volume))

    else:
        print("All values must be greater than 0")
#===========================================================================================
#CYLINDER
#===========================================================================================
elif choice == 9:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    if r > 0 and h > 0:
        volume = math.pi * r * r * h
        curved_area = 2 * math.pi * r * h

        print("Shape = Cylinder")
        print("Volume =", volume)
        print("Curved Surface Area =", curved_area)

        history.append(("Cylinder", volume))

    else:
        print("Radius and height must be greater than 0")

#==========================================================================================
# CONE
# =========================================================================================        

elif choice == 10:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    if r > 0 and h > 0:
        volume = (math.pi * r * r * h) / 3

        slant_height = math.sqrt(r * r + h * h)

        print("Shape = Cone")
        print("Volume =", volume)
        print("Slant Height = ", slant_height)



        history.append(("Cone", volume))

    else:
        print("Radius and height must be greater than 0")
#===========================================================
#SPHERE
#===========================================================
elif choice == 11:
    r = float(input("Enter radius: "))

    if r > 0:
        volume = (4 * math.pi * r * r * r) / 3
        surface_area = 4 * math.pi * r * r

        print("Shape = Sphere")
        print("Volume =", volume)
        print("Surface Area =", surface_area)

        history.append(("Sphere", volume))

    else:
        print("Radius must be greater than 0")
#=============================================================
#HEMISPHERE
#=============================================================
elif choice == 12:
    r = float(input("Enter radius: "))

    if r > 0:
        volume = (2 * math.pi * r * r * r) / 3
        curved_area = 2 * math.pi * r * r

        print("Shape = Hemisphere")
        print("Volume =", volume)
        print("Curved Surface Area =", curved_area)

        history.append(("Hemisphere", volume))

    else:
        print("Radius must be greater than 0")
#==================================================================
#INVALID CHOICE 
#====================================================================
else:
    print("Invalid choice")
    print("Please select a number from 1 to 12")

print("========================================")

if choice >= 1 and choice <= 12:
    selected_shape = shapes[choice - 1]
    print("Selected Shape:", selected_shape)
    print("Formula:", formulas[selected_shape])

print("========================================")


random_number = random.randint(1, 100)
print("Random Number:",random_number)

print("Total Shapes:", len(shape_set))

print("Calculation History:")

if len(history) > 0:
    print(history)
else:
    print("No calculation was completed")

print("========================================")
print("Thank you for using the calculator")
print("========================================")


