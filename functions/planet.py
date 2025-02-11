#planet.py
from .star import Star
from .utils import HabitableZoneUnit, stellarName
import random
import math


systemHabitable = False
gravitationalConstant = 6.67430e-11 
STEFAN_BOLTZMANN = 5.670374419e-8


def allocateOrbitalPosition(solarSystem):
    planet_count = len(solarSystem.planets)
    
    if planet_count >= len(solarSystem.orbitalSpacing):
        raise IndexError ("Not enough orbital slots")
    
    return solarSystem.orbitalSpacing[planet_count]
    
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
        
def planetSurfaceGravity(planetMassKilogram, planetRadiusMeter):
    return  ((6.674e-11)* planetMassKilogram) / planetRadiusMeter**2

def planetAlbedo(planetType):
    albedo_dict = {
        "Lava Planet": 0.15,  # Dark, absorbs heat
        "Rocky Planet": 0.3,   # Similar to Earth
        "Ocean Planet": 0.4,   # More reflective
        "Gas Giant": 0.5,      # Reflects clouds
        "Ice Planet": 0.7,    
        "Gas Giant": 0.7,        
        "Brown Dwarf": 0.9, 
    }
    return albedo_dict.get(planetType, 0.3)

def planetTemperature(starLuminosityWatts, planetOrbitalDistanceMeter):
    # Use the Stefan-Boltzmann law to calculate the equilibrium temperature of the planet.
    # Stefan-Boltzmann law: T^4 = L / (16 * pi * d^2 * sigma)
    # Where:
    #   T = equilibrium temperature of the planet (Kelvin)
    #   L = luminosity of the star (Watts)
    #   d = distance of the planet from the star (meters)
    #   sigma = Stefan-Boltzmann constant (W/m^2/K^4)

    # Calculate the flux at the planet's distance (energy received per unit area)
    flux = starLuminosityWatts / (4 * math.pi * (planetOrbitalDistanceMeter ** 2))

    # Calculate the equilibrium temperature in Kelvin using the flux
    temp_kelvin = (flux / STEFAN_BOLTZMANN) ** 0.25

    return (temp_kelvin - 80)
    
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
    

def planetDescription(planetType, planetTemperatureKelvin, planetSurfaceGravityEarthGravity, planetAxialTilt):
    description = ""
    if planetType == "Lava Planet":
        description = "The surface is mostly covered in molten lava. "
    elif planetType == "Rocky Planet":
        description = description + "The surface is primary made up of silicates, rocks and metals. There is natural formations like waterfall, mountains, and volcanoes."
    elif planetType == "Desert Planet":
        description = description + "It is very dry and arid. There is practically no precipitation with a very dry climate. Youll find sand dunes, canyons, and mesas around. "
    elif planetType == "Ocean Planet":
        description = description + "The surface is vast oceans of water and other fluids like hydrocarbons and ammonia. In colder areas youll find icebergs. "
    elif planetType == "Super Earth":
        description = description + "This planet is " + random.choice(["rocky ", "gaseous "])
    elif planetType == "Mini Neptune":
        description = description + "The surface is less dense than earths, it has a thick atmosphere of hydrogen and helium and a small rocky core. "
    elif planetType == "Ice Giant":
        description = description + "The planet is made up from a range of elements that are heavoer than hydrogen and helium, the atmosphere is thick."
    elif planetType == "Gas Giant":
        description = description + "This planet is made up from hydrogen and helium, it has a thick atmosphere and a small rocky core with no solid surface. "
    elif planetType == "Brown Dwarf":
        description = description + "A substellar object that is not massive enough to sustain nuclear fusion of ordinary hydrogen into helium in its core. "
    
    if planetTemperatureKelvin < 273:
        description = description + "The temperature is below freezing. "
    elif 273 <= planetTemperatureKelvin <= 373:
        description = description + "The temperature here is habitable. "
    elif planetTemperatureKelvin > 373:
        description = description + "The temperature is boiling hot, survival of life would be very difficult. "
    elif planetTemperatureKelvin > 1000:
        description = description + "The temperature is extremely hot, survival of life would be impossible. "
    
    if planetSurfaceGravityEarthGravity < 0.5:
        description = description + "The surface gravity is very low. "
    elif 0.5 <= planetSurfaceGravityEarthGravity <= 1.5:
        description = description + "The surface gravity is similar to earth. "
    elif planetSurfaceGravityEarthGravity > 1.5:
        description = description + "The surface gravity is very high. "
        
    if planetAxialTilt < 30:
        description = description + "The seaons are standard "
    elif 30 <= planetAxialTilt <= 60:
        description = description + "The seasons are extreme. "
    elif planetAxialTilt > 60:
        description = description + "The seasons are very extreme. "

    return description

def Habitable(orbitalSpacingList, habitableZoneInner, habitableZoneOuter):
        if habitableZoneInner < orbitalSpacingList < habitableZoneOuter:
            return True
        else:
            return False

class Planet:

        
        
    def __init__(self,solarSystem, star):
        self.solarSystem = solarSystem
        self.star = star
        
        self.planetOrbitalPositionAU = allocateOrbitalPosition(solarSystem)
        self.planetOrbitalPositionMeter = self.planetOrbitalPositionAU * 1.496e11
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
        self.planetSurfaceGravity = planetSurfaceGravity(self.planetMassKilogram, self.planetRadiusMeter)
        self.planetSurfaceGravityEarthGravity = self.planetSurfaceGravity/9.8
        self.planetTemperatureKelvin = planetTemperature(self.star.starLuminosityWatts, self.planetOrbitalPositionMeter)
        self.planetTemperatureCelsius = self.planetTemperatureKelvin - 273.15
        self.planetTemperatureFahrenheit = (self.planetTemperatureCelsius * 9/5) + 32
        self.planetAxialTilt = planetAxialTilt(self.planetType)
        self.planetPicutre = planetPicutre("/static/brownDwarf.png", "/static/desertPlanet.png", "/static/gasGiant.png", "/static/iceGiant.png", "/static/miniNeptune.png", "/static/oceanPlanet.png", "/static/rockyPlanet.png", "/static/superEarth.png", "/static/lavaPlanet.png",self.planetType)
        self.planetDescription = planetDescription(self.planetType, self.planetTemperatureKelvin, self.planetSurfaceGravityEarthGravity, self.planetAxialTilt)
        self.planetName = stellarName()
        self.planetHabitable = Habitable(self.planetOrbitalPositionAU, self.solarSystem.habitableZoneInnerAU, self.solarSystem.habitableZoneOuterAU)
        
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
            "planetAxialTilt": self.planetAxialTilt,
            "planetPicture": self.planetPicutre,
            "planetDescription": self.planetDescription,
            "planetName": self.planetName,
            "planetHabitable": self.planetHabitable,
        }
        
    
        