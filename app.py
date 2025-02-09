#app.py
from functions.star import Star
from functions.solarsystem import SolarSystem
from functions.planet import Planet


def main():
    star = Star()
    solarSystem = SolarSystem(star)
    for planet in solarSystem.planets:
        print(planet)



if __name__ == "__main__":
    main()