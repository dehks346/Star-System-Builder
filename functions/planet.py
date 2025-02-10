#planet.py
from .star import Star
from .utils import HabitableZoneUnit, stellarName
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
        return random.choice(["Rocky Planet", "Ocean Planet", "Super Earth"])
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
    else:
        return 1
        
def planetSurfaceGravity(planetMassKilogram, planetRadiusMeter, gravitationalConstant):
    return gravitationalConstant * planetMassKilogram / planetRadiusMeter**2
    
def planetTemperature(starLuminositySolarLuminosity, planetOrbitalDistanceMeter):
    if planetType == "Lava Planet":
        return random.uniform(1200, 3000)
    else:
        return ((starLuminositySolarLuminosity) / (16 * math.pi * 5.670374419e-8 * planetOrbitalDistanceMeter**2)) ** 0.25
    
def planetAtmosphereComposition(planetType):
    if planetType == "Lava Planet":
        return  ["CO2", "SO2", "H2O"]
    elif planetType == "Rocky Planet":
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
        
    #def planetSurfaceComposition():
    
def planetSurfaceWater(planetRadiusMeter, planetType, planetTemperatureKelvin):
        planetSurfaceAreaMeters = 4 * math.pi * planetRadiusMeter**2
        
        if planetType == "Lava Planet":
            return 0
        elif planetType == "Ocean Planet" and 273 <= planetTemperatureKelvin <= 373:
            waterPercentage = 0.75
        elif planetType == "Rocky Planet" and 273 <= planetTemperatureKelvin <= 373:
            waterPercentage = 0.3
        elif planetType == "Super Earth" and 273 <= planetTemperatureKelvin <= 373:
            waterPercentage = 0.4
        else:
            waterPercentage = 0.0
        
        return planetSurfaceAreaMeters * waterPercentage
        
    
    #def planetMoons():
    
def planetOrbitalPeriod(planetOrbitalPositionAU, starMassKilogram):
        semiMajorAxisMeters = planetOrbitalPositionAU * 149597870.7
        periodSeconds = math.sqrt(4 * math.pi**2 * semiMajorAxisMeters**3 / (gravitationalConstant * starMassKilogram))
        periodYears = periodSeconds / 31536000
        return periodYears
        
def planetDayLength(planetRadiusMeter, planetMassKilogram):
        if planetType == "Lava Planet":
            return random.uniform(0.5, 20)
        Inertia = (2/5) * planetMassKilogram * planetRadiusMeter**2
        
        omega = 2 * math.pi / 86400
        L = Inertia * omega
        
        dayLengthSeconds = (2 * math.pi * Inertia) / L
        return dayLengthSeconds / 3600
        
def planetAxialTilt(planetType):
        if planetType == "Lava Planet":
            return random.uniform(20, 90)
        elif planetType == "Rocky Planet" or "Ocean Planet" or "Desert Planet":
            return random.uniform(0, 30)
        elif planetType == "Gas Giant" or "Ice Giant" or "Mini Neptune":
            return random.uniform(0, 60)
        elif planetType == "Super Earth":
            return random.uniform(0, 90)
        elif planetType == "Brown Dwarf":
            return random.uniform(0, 90)
        
def planetPicutre(brownDwarf, desertPlanet, gasGiant, iceGiant, miniNeptune, oceanPlanet, rockyPlanet, superEarth, lavaPlanet, planetType):
    if planetType == "Brown Dwarf":
        return brownDwarf
    elif planetType == "Desert Planet":
        return desertPlanet
    elif planetType == "Gas Giant":
        return gasGiant
    elif planetType == "Ice Giant":
        return iceGiant
    elif planetType == "Mini Neptune":
        return miniNeptune
    elif planetType == "Ocean Planet":
        return oceanPlanet
    elif planetType == "Rocky Planet":
        return rockyPlanet
    elif planetType == "Super Earth":
        return superEarth
    elif planetType == "Lava Planet":
        return lavaPlanet
    

def planetDescription(planetType, planetTemperatureKelvin, planetSurfaceWater, planetAtmosphereComposition, planetSurfaceGravityEarthGravity, planetDayLength, planetOrbitalPeriod, planetAxialTilt, planetMassEarthMasses, planetRadiusEarthRadii):
    description = ""
    if planetType == "Lava Planet":
        description = description + "This planets surface is mostly or enitrely covered by molten lava, there is molten volcanoes that spew lava and vast magma oceans on the surface. "
    elif planetType == "Rocky Planet":
        description = description + "This planets surface is composed primarily of silicates, rocks or metals. It has a hard surface and a molten heavy metal core. On the surface youll find landforms like cliffs, valleys, volcanoes and craters. "
    elif planetType == "Desert Planet":
        description = description + "This planets surface is arid and very similar to a desert on earth. there is little to no natural precipitation and a very dry climate. "
    elif planetType == "Ocean Planet":
        description = description + "This planets surface is covered in water, the oceans are made from different fluids like lava, ammonia, or hydrocarbons . "
    elif planetType == "Super Earth":
        description = description + "This planet can be rocky or gaseous, it is larger than earth but smaller than a gas giant."
    elif planetType == "Mini Neptune":
        description = description + "This planet is gassy with a thick hydrogen-helium atmosphere, the planets density is lower than earths.. "
    elif planetType == "Ice Giant":
        description = description + "This planet is made up from elements heavier than hydrogen and helium, it has a thick atmosphere of water, ammonia and methane. "
    elif planetType == "Gas Giant":
        description = description + "This planet is made up from hydrogen and helium, it has a thick atmosphere and a small rocky core with no solid surface. "
    elif planetType == "Brown Dwarf":
        description = description + "This planet is a substellar object that is not massive enough to sustain nuclear fusion of ordinary hydrogen into helium in its core. "
    
    if planetTemperatureKelvin < 273:
        description = description + "The average temperature on this planet is below freezing. "
    elif 273 <= planetTemperatureKelvin <= 373:
        description = description + "The average temperature on this planet is between freezing and boiling. "
    elif planetTemperatureKelvin > 373:
        description = description + "The average temperature on this planet is above boiling. "
    elif planetTemperatureKelvin > 1000:
        description = description + "The average temperature on this planet is extremely hot. "
    
    if planetSurfaceWater > 0:
        description = description + "This planet has water on its surface. "
    elif planetSurfaceWater > 25:
        description = description + "This planet has a lot of water on its surface. "
    elif planetSurfaceWater > 50:
        description = description + "This planet is covered in water. "
    elif planetSurfaceWater > 75:
        description = description + "This planet is mostly water. "
    
    if planetAtmosphereComposition == ["CO2", "SO2", "H2O"]:
        description = description + "The atmosphere on this planet is composed of carbon dioxide, sulfur dioxide and water vapor. "
    elif planetAtmosphereComposition == ["CO2", "O2", "N2"]:
        description = description + "The atmosphere on this planet is composed of carbon dioxide, oxygen and nitrogen. "
    elif planetAtmosphereComposition == ["CO2", "O2"]:
        description = description + "The atmosphere on this planet is composed of carbon dioxide and oxygen. "
    elif planetAtmosphereComposition == ["H20", "O2", "N2"]:
        description = description + "The atmosphere on this planet is composed of water vapor, oxygen and nitrogen. "
    elif planetAtmosphereComposition == ["CO2", "N2", "O2"]:
        description = description + "The atmosphere on this planet is composed of carbon dioxide, nitrogen and oxygen. "
    elif planetAtmosphereComposition == ["H2", "He", "CH4"]:
        description = description + "The atmosphere on this planet is composed of hydrogen, helium and methane. "
    elif planetAtmosphereComposition == ["H20", "CH4", "NH3"]:
        description = description + "The atmosphere on this planet is composed of water vapor, methane and ammonia. "
    
    if planetSurfaceGravityEarthGravity < 0.5:
        description = description + "The surface gravity on this planet is very low. "
    elif 0.5 <= planetSurfaceGravityEarthGravity <= 1.5:
        description = description + "The surface gravity on this planet is similar to earth. "
    elif planetSurfaceGravityEarthGravity > 1.5:
        description = description + "The surface gravity on this planet is very high. "
    
    if planetDayLength < 24:
        description = description + "The day length on this planet is very short. "
    elif 24 <= planetDayLength <= 48:
        description = description + "The day length on this planet is similar to earth. "
    elif planetDayLength > 48:
        description = description + "The day length on this planet is very long. "
    
    if planetOrbitalPeriod < 365:
        description = description + "The orbital period on this planet is very short. "
    elif 365 <= planetOrbitalPeriod <= 730:
        description = description + "The orbital period on this planet is similar to earth. "
    elif planetOrbitalPeriod > 730:
        description = description + "The orbital period on this planet is very long. "
        
    if planetAxialTilt < 30:
        description = description + "The axial tilt on this planet is very low. "
    elif 30 <= planetAxialTilt <= 60:
        description = description + "The axial tilt on this planet is similar to earth. "
    elif planetAxialTilt > 60:
        description = description + "The axial tilt on this planet is very high. "
    
    if planetMassEarthMasses < 1:
        description = description + "The mass of this planet is very low. "
    elif 1 <= planetMassEarthMasses <= 5:
        description = description + "The mass of this planet is similar to earth. "
    elif planetMassEarthMasses > 5:
        description = description + "The mass of this planet is very high. "
    
    if planetRadiusEarthRadii < 1:
        description = description + "The radius of this planet is very low. "
    elif 1 <= planetRadiusEarthRadii <= 5:
        description = description + "The radius of this planet is similar to earth. "
    elif planetRadiusEarthRadii > 5:
        description = description + "The radius of this planet is very high. "
    
    return description

class Planet:
        
    def __init__(self,solarSystem, star):
        self.solarSystem = solarSystem
        self.star = star
        
        self.planetOrbitalPositionAU = allocateOrbitalPosition(solarSystem)
        self.HZU = HabitableZoneUnit(solarSystem.habitableZoneInnerAU, self.planetOrbitalPositionAU)
        self.planetType = planetType(self.HZU)
        self.planetRadiusEarthRadii = planetRadius(self.planetType)
        self.planetRadiusSolarRadii = self.planetRadiusEarthRadii * 6371 / 695700
        self.planetRadiusMeter = self.planetRadiusSolarRadii * 695700000
        self.planetRadiusMile = self.planetRadiusMeter / 1609
        self.planetRadiusKilometer = self.planetRadiusMeter / 1000
        self.planetRadiusAstronomicalUnits = self.planetRadiusMeter / 149597870.7
        self.planetDiameterEarthRadii = self.planetRadiusEarthRadii * 2
        self.planetDiamterSolarRadii = self.planetRadiusSolarRadii * 2
        self.planetDiameterMeter = self.planetRadiusMeter * 2
        self.planetDiameterKilometer = self.planetRadiusKilometer * 2
        self.planetDiameterAstronomicalUnits = self.planetRadiusAstronomicalUnits * 2
        self.planetMassEarthMasses = planetMass(self.planetType, self.planetRadiusEarthRadii)
        self.planetMassKilogram = self.planetMassEarthMasses * 5.972e24
        self.planetMassPound = self.planetMassKilogram * 2.20462
        self.planetMassTonne = self.planetMassKilogram / 1000
        self.planetSurfaceGravity = planetSurfaceGravity(self.planetMassKilogram, self.planetRadiusMeter, gravitationalConstant)
        self.planetSurfaceGravityEarthGravity = self.planetSurfaceGravity/9.8
        self.planetTemperatureKelvin = planetTemperature(self.star.starLuminositySolarLuminosity, self.planetOrbitalPositionAU)
        self.planetTemperatureCelsius = self.planetTemperatureKelvin - 273.15
        self.planetTemperatureFahrenheit = (self.planetTemperatureCelsius * 9/5) + 32
        self.planetAtmosphereComposition = planetAtmosphereComposition(self.planetType)
        self.planetSurfaceGravity = planetSurfaceGravity(self.planetMassKilogram, self.planetRadiusMeter, gravitationalConstant)
        self.planetAxialTilt = planetAxialTilt(self.planetType)
        self.planetOrbitalPeriod = planetOrbitalPeriod(self.planetOrbitalPositionAU, self.star.starMassKilogram)
        self.planetDayLength = planetDayLength(self.planetRadiusMeter, self.planetMassKilogram)
        self.planetSurfaceWater = planetSurfaceWater(self.planetRadiusMeter, self.planetType, self.planetTemperatureKelvin)
        self.planetPicutre = planetPicutre("/static/brownDwarf.jpg", "/static/desertPlanet.jpg", "/static/gasGiant.jpg", "/static/iceGiant.jpg", "/static/miniNeptune.jpg", "/static/oceanPlanet.jpg", "/static/rockyPlanet.jpg", "/static/superEarth.jpg", "/static/lavaPlanet.jpg",self.planetType)
        self.planetDescription = planetDescription(self.planetType, self.planetTemperatureKelvin, self.planetSurfaceWater, self.planetAtmosphereComposition, self.planetSurfaceGravityEarthGravity, self.planetDayLength, self.planetOrbitalPeriod, self.planetAxialTilt, self.planetMassEarthMasses, self.planetRadiusEarthRadii)
        self.planetName = stellarName()
        
    def to_dict(self):
        return {
            "solarSystem": self.solarSystem,
            "star": self.star,
            "planetOrbitalPositionAU": self.planetOrbitalPositionAU,
            "HZU": self.HZU,
            "planetType": self.planetType,
            "planetRadiusEarthRadii": self.planetRadiusEarthRadii,
            "planetRadiusSolarRadii": self.planetRadiusSolarRadii,
            "planetRadiusMeter": self.planetRadiusMeter,
            "planetRadiusMile": self.planetRadiusMile,
            "planetRadiusKilometer": self.planetRadiusKilometer,
            "planetRadiusAstronomicalUnits": self.planetRadiusAstronomicalUnits,
            "planetDiameterEarthRadii": self.planetDiameterEarthRadii,
            "planetDiamterSolarRadii": self.planetDiamterSolarRadii,
            "planetDiameterMeter": self.planetDiameterMeter,
            "planetDiameterKilometer": self.planetDiameterKilometer,
            "planetDiameterAstronomicalUnits": self.planetDiameterAstronomicalUnits,
            "planetMassEarthMasses": self.planetMassEarthMasses,
            "planetMassKilogram": self.planetMassKilogram,
            "planetMassPound": self.planetMassPound,
            "planetMassTonne": self.planetMassTonne,
            "planetSurfaceGravity": self.planetSurfaceGravity,
            "planetSurfaceGravityEarthGravity": self.planetSurfaceGravityEarthGravity,
            "planetTemperatureKelvin": self.planetTemperatureKelvin,
            "planetTemperatureCelsius": self.planetTemperatureCelsius,
            "planetTemperatureFahrenheit": self.planetTemperatureFahrenheit,
            "planetAtmosphereComposition": self.planetAtmosphereComposition,
            "planetAxialTilt": self.planetAxialTilt,
            "planetOrbitalPeriod": self.planetOrbitalPeriod,
            "planetDayLength": self.planetDayLength,
            "planetSurfaceWater": self.planetSurfaceWater, 
            "planetPicture": self.planetPicutre,
            "planetDescription": self.planetDescription,
            "planetName": self.planetName,
        }
        
    
        