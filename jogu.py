import math #imports math functions
lengthcube = float(input("What is the length of the cube?")) #put in the length of the cube
lengthtetra = float(input("What is the length of the tetrahedron?")) #put in the length of tetrahedron
volumecube = lengthcube**3 #multiplies the cubes lenght by itself three times
volumetetra = lengthcube**3/6*math.sqrt(2) #multiples the tetrahedrons lenght by 3, divdes it by 6 and then take the sqaure root of 2
print("The cubes volume is",volumecube,"cm3") #prints the cubes volume
print("The tetrahedrons volume is",volumetetra,"cm3") #prints the tetrahedrons volume