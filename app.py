#app.py
from functions.star import Star
from functions.solarsystem import SolarSystem
from functions.planet import Planet
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)



def main():
    pass



@app.route("/")
def home():
    star = Star()
    solarSystem = SolarSystem(star)
    
    planets = [planet.to_dict() for planet in solarSystem.planets]
    print(planets[0])
    star_data = star.to_dict()
    solarSystem_data = solarSystem.to_dict()
    

    
    return render_template(
        "index.html",
        planet_data=planets,
        star=star_data,
        solarSystem=solarSystem_data
    )

if __name__ == "__main__":
    app.run(debug=True)