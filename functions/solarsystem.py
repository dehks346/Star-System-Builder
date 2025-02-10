#solarsystem.py
import math
from .star import Star
from .planet import Planet
from .utils import stellarName, solarSystemHabitable
import random

def habitableZoneInner(starLuminositySolarLuminositys):
    return 0.95*starLuminositySolarLuminositys

def habitableZoneOuter(starLuminositySolarLuminositys):
    return 1.37*starLuminositySolarLuminositys

def orbitalInnerLimit(starRadiusSolarRadii):
    return 0.1*starRadiusSolarRadii
    
def orbitalOuterLimit(starMassSolarMass):
    return 2*(starMassSolarMass**(1/3))*100

def numberOfPlanets(orbitalInnerLimit, orbitalOuterLimit):
    baseNumber = round((math.log(orbitalOuterLimit) - math.log(orbitalInnerLimit)) / 1.2, 0)
    offset = random.randint(-2, 3)
    return max(1, min(12,round(baseNumber + offset, 0)))

def orbitalSpacing(orbitalInnerLimit, orbitalOuterLimit,numberOfPlanets):
    spacing = []
    if orbitalInnerLimit <= 0 or orbitalOuterLimit <= 0 or numberOfPlanets < 1:
        raise ValueError("Number of planets must be at least 1.")
    log_inner = math.log10(orbitalInnerLimit)
    log_outer = math.log10(orbitalOuterLimit)
    log_step = (log_outer - log_inner) / (numberOfPlanets + 1)
    
    for i in range(1, numberOfPlanets + 1):
        log_distance = log_inner + log_step * i
        spacing.append(10 ** log_distance)
    
    return spacing    
    



class SolarSystem:
    def __init__(self, star):
        self.star = star
        self.planets = []
        self.habitableZoneInnerAU = habitableZoneInner(self.star.starLuminositySolarLuminosity)
        self.habitableZoneOuterAU = habitableZoneOuter(self.star.starLuminositySolarLuminosity)
        self.orbitalInnerLimitAU = orbitalInnerLimit(self.star.starRadiusSolarRadii)
        self.orbitalOuterLimitAU = orbitalOuterLimit(self.star.starMassSolarMass)
        self.numberOfPlanets = int(numberOfPlanets(self.orbitalInnerLimitAU, self.orbitalOuterLimitAU))
        self.orbitalSpacing = orbitalSpacing(self.orbitalInnerLimitAU, self.orbitalOuterLimitAU, self.numberOfPlanets)
        self.systemName = stellarName()
        self.solarSystemHabitable = solarSystemHabitable
        
        for i in range(self.numberOfPlanets):
            planet = Planet(self, self.star)
            self.planets.append(planet)
        
    def to_dict(self):
        return {
            "habitableZoneInnerAU": self.habitableZoneInnerAU,
            "habitableZoneOuterAU": self.habitableZoneOuterAU,
            "orbitalInnerLimitAU": self.orbitalInnerLimitAU,
            "orbitalOuterLimitAU": self.orbitalOuterLimitAU,
            "numberOfPlanets": self.numberOfPlanets,
            "orbitalSpacing": self.orbitalSpacing,
            "systemName": self.systemName,
            "solarSystemHabitable": self.solarSystemHabitable,
        }