from ursina import *

def setup_weather():
    DirectionalLight()
    ambient = AmbientLight(color=color.rgb(120,120,150))
    fog = Entity(model='quad', color=color.rgba(200, 200, 255, 100), scale=(100, 1), position=(0,5,0))

def apply_weather_effects(aircraft):
    gust = sin(time.time()) * 0.2
    aircraft.rotation_x += gust