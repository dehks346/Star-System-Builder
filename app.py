#app.py
from functions.star import Star
from functions.solarsystem import SolarSystem, generateHabitableSystem
from functions.planet import Planet
import pandas as pd
from flask import Flask, render_template, send_file
import io

app = Flask(__name__)



def main():
    pass



@app.route("/")
def home():
    star = Star()
    solarSystem = generateHabitableSystem(star)
    
    global planets
    planets = [planet.to_dict() for planet in solarSystem.planets]
    print(planets[0])
    global star_data
    star_data= star.to_dict()
    global solarSystem_data
    solarSystem_data= solarSystem.to_dict()
    

    
    return render_template(
        "index.html",
        planet_data=planets,
        star=star_data,
        solarSystem=solarSystem_data
    )
    
@app.route('/download')
def download_file():
    # Generate text content
    file_content = str(solarSystem_data)
    file_content += str(star_data)
    file_content += str(planets)

    # Convert content to bytes
    byte_io = io.BytesIO(file_content.encode('utf-8'))
    byte_io.seek(0)

    # Send file as an attachment for download
    return send_file(byte_io, as_attachment=True, download_name="solar_system_data.txt", mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)