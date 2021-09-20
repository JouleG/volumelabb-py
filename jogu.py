import math #imports math functions

# option = int(input("1: Cube \n2: Tetrahedron"))
# while True:
#      if option == 1 or option == 2:
#          break
# if option == 1:
try:
    lengthcube = float(input("What is the length of the cube?")) #put in the length of the cube

except ValueError:
            while True:
                try:
                    lengthcube = float(input("Must be a valid number"))

                except ValueError:
                    pass
                else:
                    break
#if option == 2:
try:
        lengthtetra = float(input("What is the length of the tetrahedron?")) #put in the length of tetrahedron

except ValueError:
            while True:
                try:
                    lengthtetra = float(input("Must be a valid number"))

                except ValueError:
                    pass
                else:
                    break

volumecube = lengthcube**3 #multiplies the cubes lenght by itself three times
volumetetra = lengthtetra**3/6*math.sqrt(2) #multiples the tetrahedrons lenght by 3, divdes it by 6 and then take the sqaure root of 2

print("\nThe volume of the cube is",volumecube,"cm^3") #prints the cubes volume
print("\nThe tetrahedrons volume is",volumetetra,"cm^3") #prints the tetrahedrons volume