#star.py
import random
import math
from .utils import stellarName

#Generates the stars stellar mass in solar mass units
def starMass(lowestSolarMass, highestSolarMass, roundedTo):
    return round(random.uniform(lowestSolarMass, highestSolarMass), roundedTo)

#Generates the stars stellar radius in stellar radii
def starRadius(starMassSolarMass, roundedTo):
    if starMassSolarMass > 1:
        return round(((696340 * (pow(starMassSolarMass, 0.6))) / 695700.099), roundedTo)
    else:
        return round(((696340 * (pow(starMassSolarMass, 0.8))) / 695700.099), roundedTo)

#Generates the stars temperature in kelvin
def starTemperature(starMassSolarMass, roundedTo):
    return round(5772 * pow(starMassSolarMass, 0.55), roundedTo)

#Generates the stars luminosity in bolometric luminosity
def starLuminosity(starMassSolarMass, roundedTo):
    if starMassSolarMass < 0.5:
        return round(starMassSolarMass ** 2.3, roundedTo)
    elif 0.5 <= starMassSolarMass < 10:
        return round(starMassSolarMass ** 3.5, roundedTo)
    else:
        return round(starMassSolarMass ** 4, roundedTo)

#Generates the stars lifespan in years
def starLifespan(starMassSolarMass, roundedTo):
    kgMassSun = 1.989e30
    sunLifetime = 10e9
    stellarMassKg = starMassSolarMass * kgMassSun
    lifetime = sunLifetime * (kgMassSun /  stellarMassKg) ** 2.5
    return int(lifetime)

#Generates the stars chromaticity in RGB
def starChromaticity(starMassSolarMass):
    if 0.08 < starMassSolarMass < 0.45:
        return {"R":"153","G":"180","B":"249"}
    elif 0.45 <= starMassSolarMass < 0.8:
        return {"R":"168","G":"191","B":"250"}
    elif 0.8 <= starMassSolarMass < 1.04:
        return {"R":"202","G":"211","B":"237"}
    elif 1.04 <= starMassSolarMass <1.4:
        return {"R":"242","G":"239","B":"248"}
    elif 1.4 <= starMassSolarMass < 2.1:
        return {"R":"250","G":"236","B":"226"}
    elif 2.1 <= starMassSolarMass < 16:
        return {"R":"240","G":"211","B":"179"}
    
def starType(starMassSolarMass):
    if 0.08 < starMassSolarMass < 0.45:
        return "M"
    elif 0.45 <= starMassSolarMass < 0.8:
        return "K"
    elif 0.8 <= starMassSolarMass < 1.04:
        return "G"
    elif 1.04 <= starMassSolarMass <1.4:
        return "F"
    elif 1.4 <= starMassSolarMass < 2.1:
        return "A"
    elif 2.1 <= starMassSolarMass < 16:
        return "B"
    elif 16 <= starMassSolarMass < 120:
        return "O"
    

class Star:
    def __init__(self):
        self.starMassSolarMass = starMass(0.08, 8.0, 3)
        self.starMassKilogram = self.starMassSolarMass*2000000000000000000000000000000
        self.starMassPound = self.starMassKilogram*2.20462
        self.starMassTonne = self.starMassKilogram/1000
        self.starRadiusSolarRadii = starRadius(self.starMassSolarMass, 3)
        self.starRadiusMeter = self.starRadiusSolarRadii*696000000
        self.starRadiusMile = self.starRadiusMeter/1609
        self.starRadiusKilometer = self.starRadiusMeter/1000
        self.starRadiusEarthRadius = self.starRadiusSolarRadii*109.1
        self.starRadiusAstronomicalUnit = self.starRadiusSolarRadii/215
        self.starDiameterSolarRadii = self.starRadiusSolarRadii*2
        self.starDiameterMeter = self.starRadiusMeter*2
        self.starDiameterMile = self.starRadiusMile*2
        self.starDiameterKilometer = self.starRadiusKilometer*2
        self.starDiameterEarthRadius = self.starRadiusEarthRadius*2
        self.starDiameterAstronomicalUnit = self.starRadiusAstronomicalUnit*2
        self.starTemperatureKelvin = starTemperature(self.starMassSolarMass, 3)
        self.starTemperatureCelsius = self.starTemperatureKelvin-273.15
        self.starTemperaturefahrenheit = (self.starTemperatureCelsius*9/5)+32
        self.starLuminositySolarLuminosity = starLuminosity(self.starMassSolarMass, 3)
        self.starLuminosityWatts = self.starLuminositySolarLuminosity*3.827e26
        self.starLuminosityJoules = self.starLuminosityWatts
        self.starLifespan = starLifespan(self.starMassSolarMass, 0)
        self.starChromaticityRGB = starChromaticity(self.starMassSolarMass)
        self.starName = stellarName()
        self.starType = starType(self.starMassSolarMass)
    
    def to_dict(self):
        return {
            "StarMassSolarMass": self.starMassSolarMass,
            "StarMassKilogram": self.starMassKilogram,
            "StarMassPound": self.starMassPound,
            "StarMassTonne": self.starMassTonne,
            "StarRadiusSolarRadii": self.starRadiusSolarRadii,
            "StarRadiusMeter": self.starRadiusMeter,
            "StarRadiusMile": self.starRadiusMile,
            "StarRadiusKilometer": self.starRadiusKilometer,
            "StarRadiusEarthRadius": self.starRadiusEarthRadius,
            "StarRadiusAstronomicalUnit": self.starRadiusAstronomicalUnit,
            "StarDiameterSolarRadii": self.starDiameterSolarRadii,
            "StarDiameterMeter": self.starDiameterMeter,
            "StarDiameterMile": self.starDiameterMile,
            "StarDiameterKilometer": self.starDiameterKilometer,
            "StarDiameterEarthRadius": self.starDiameterEarthRadius,
            "StarDiameterAstronomicalUnit": self.starDiameterAstronomicalUnit,
            "StarTemperatureKelvin": self.starTemperatureKelvin,
            "StarTemperatureCelsius": self.starTemperatureCelsius,
            "StarTemperaturefahrenheit": self.starTemperaturefahrenheit,
            "StarLuminositySolarLuminosity": self.starLuminositySolarLuminosity,
            "StarLuminosityWatts": self.starLuminosityWatts,
            "StarLuminosityJoules": self.starLuminosityJoules,
            "StarLifespan": self.starLifespan,
            "StarChromaticityRGB": self.starChromaticityRGB,
            "starName": self.starName,
            "starType": self.starType,
        }
