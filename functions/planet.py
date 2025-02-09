#planet.py
from .star import Star
from .utils import HabitableZoneUnit
import random
import math

gravitationalConstant = 6.67430e-11 

def allocateOrbitalPosition(solarSystem):
    planet_count = len(solarSystem.planets)
    
    if planet_count >= len(solarSystem.orbitalSpacing):
        raise IndexError ("Not enough orbital slots")
    
    return solarSystem.orbitalSpacing[planet_count]
    
def isHabitable(innerHabitableZoneAU, outerHabitableZoneAU, orbitalPosition):
    if int(innerHabitableZoneAU) < int(orbitalPosition) < int(outerHabitableZoneAU):
        return True
    else:
        return False
    
def planetType(HZU):
    if HZU < 0.2:
        return "Lava Planet"
    elif 0.2 < HZU < 0.8:
        return random.choice(["Rocky Planet", "Desert Planet"])
    elif 0.8 < HZU < 1.5:
        return random.choice(["Rocky Planet", "Ocean Planet", "Super-Earth"])
    elif 1.5 < HZU < 3:
        return random.choice(["Super Earth", "Mini Neptune"])
    elif 3 < HZU < 10:
        return random.choice(["Mini Neptune", "Ice Giant"])     
    elif 10 < HZU < 50:
        return random.choice(["Ice Giant", "Gas Giant"])  
    elif HZU > 50:
        return "Brown Dwarf"

    #calculated planet radius in earth radii
def planetRadius(planetType):
    if planetType == "Rocky Planet" or "Desert Planet" or "Ocean Planet":
        return random.uniform(0.5, 1.5)
    elif planetType == "Super Earth":
        return random.uniform(1.5,2.5)
    elif planetType == "Mini Neptune":
        return random.uniform(2.5, 4.0)
    elif planetType == "Ice Giant":
        return random.uniform(4.0,6.0)
    elif planetType == "Gas Giant":
        return random.uniform(6.0, 15.0)
    elif planetType == "Brown Dwarf":
        return random.uniform(13, 80)
    
    #Calculates planet mass in earth masses
def planetMass(planetType, planetRadiusEarthRadii):
    if planetType == "Rocky Planet":
        return  planetRadiusEarthRadii**3.7
    elif planetType == "Desert Planet":
        return  planetRadiusEarthRadii**3
    elif planetType == "Ocean Planet":
        return  planetRadiusEarthRadii**2.9
    elif planetType == "Super Earth":
        return  planetRadiusEarthRadii**3
    elif planetType == "Mini Neptune":
        return  1.7*planetRadiusEarthRadii**1.7
    elif planetType == "Ice Giant":
        return  1.2*planetRadiusEarthRadii**1.2
    elif planetType == "Gas Giant":
        return  0.76*planetRadiusEarthRadii**1.9
    elif planetType == "Brown Dwarf":
        return  50*planetRadiusEarthRadii**1.01
        
def planetSurfaceGravity(planetMassKilogram, planetRadiusMeter, gravitationalConstant):
    return gravitationalConstant * planetMassKilogram / planetRadiusMeter**2
    
def planetTemperature(starLuminositySolarLuminosity, planetOrbitalDistanceMeter):
    return ((starLuminositySolarLuminosity) / (16 * math.pi * 5.670374419e-8 * planetOrbitalDistanceMeter**2)) ** 0.25
    
def planetAtmosphereComposition(planetType):
    if planetType == "Rocky Planet":
        return  ["CO2", "O2", "N2"]
    elif planetType == "Desert Planet":
        return  ["CO2", "O2"]
    elif planetType == "Ocean Planet":
        return  ["H20", "O2", "N2"]
    elif planetType == "Super Earth":
        return  ["CO2", "N2", "O2"]
    elif planetType == "Mini Neptune":
        return  ["H2", "He", "CH4"]
    elif planetType == "Ice Giant":
        return  ["H20", "CH4", "NH3"]
    elif planetType == "Gas Giant":
        return  ["H2", "He", "CH4"]
    elif planetType == "Brown Dwarf":
        return  ["H", "He"]
        
    #def planetAtmosphericPressure():
        
    #def planetSurfaceComposition():
    
    #def planetSurfaceWater():
    
    #def planetMoons():
    
    #def planetOrbitalPeriod():
        
    #def planetDayLength():
        
    #def planetAxialTilt():

class Planet:
        
    def __init__(self,solarSystem, star):
        self.solarSystem = solarSystem
        self.star = star

        self.planetOrbitalPositionAU = allocateOrbitalPosition(solarSystem)
        self.HZU = HabitableZoneUnit(solarSystem.habitableZoneInnerAU, self.planetOrbitalPositionAU)
        self.planetType = planetType(self.HZU)
        self.planetRadiusEarthRadii = planetRadius(self.planetType)
        self.planetMassEarthMasses = planetMass(self.planetType, self.planetRadiusEarthRadii)
        #self.planetSurfaceGravity = planetSurfaceGravity(self.planetMassKilogram, self.planetRadiusMeter, gravitationalConstant)
        #convert gravity into earth units: surface gravity/9.8
        self.planetTemperatureKelvin = planetTemperature(self.star.starLuminositySolarLuminosity, self.planetOrbitalPositionAU)
    
    
    def __str__(self):
        return f"{self.planetType} at {self.planetOrbitalPositionAU} AU | Radius: {self.planetRadiusEarthRadii} Earth radii | Mass: {self.planetMassEarthMasses} Earth masses | Temp: {self.planetTemperatureKelvin:.2f} K"
        