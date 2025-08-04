from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from aircraft import *
from environment import setup_environment
from camera_control import setup_camera
from instruments import setup_instruments, update_instruments
from weather import setup_weather, apply_weather_effects
from physics import apply_physics

app = Ursina()

#Load and play MP3 sound loop
background_music = Audio('main_sound.mp3', loop=True, autoplay=True)

plane = Aircraft()
enemy = Enemy(target=plane)
setup_environment()
setup_camera(plane)
instrument_panel = setup_instruments()
setup_weather()

def update():
    plane.update()
    enemy.update()
    apply_weather_effects(plane)
    apply_weather_effects(enemy)
    apply_physics(plane, throttle=100)
    update_instruments(instrument_panel, plane)

app.run()