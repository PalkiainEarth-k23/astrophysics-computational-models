import math
Name = input("What is the name of the planet: ")
Mass = float(input(f"What is the mass of{Name} in kg : "))
Radius = float(input(f"What is the radius of {Name} in meters: "))
Density = Mass/((4/3) *3.141*(Radius)*(Radius)*(Radius))
if Density<0:
    print(f"Wrong values have been entered for {Name} since density is always positive")
elif Density< 2000:
    print(f"{Name} is alow density planet and is likely a gaseous panet or a gas giant")
elif 6000>=Density>=2000:
    print(f"{Name} is likely a rocky planet like earth")
else:
    print(f"{Name} has an ultra dense core likeley made up of metals like iron")