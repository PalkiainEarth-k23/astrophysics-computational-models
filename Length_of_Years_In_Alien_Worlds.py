import math 
Planet= input("What is the name of the planet: ")
host_star = input("What is the name of the host star: ")
Distance = float(input(f"What the distance of {Planet} from {host_star} in AU: "))
Mass = float(input(f"What is the mass of the {host_star}: "))
Orbital_Time_in_Earth_yrs= math.sqrt(Distance * Distance*Distance/ Mass)
Orbital_Time_in_Days = Orbital_Time_in_Earth_yrs*365.25
print(f"Thus the Orbital time of {Planet} around the {host_star} is {Orbital_Time_in_Earth_yrs:.2f} Earth years or {Orbital_Time_in_Days:.2f} Earth Days")
