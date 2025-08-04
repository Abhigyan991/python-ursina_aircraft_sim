from ursina import *

def setup_instruments():
    horizon = Entity(model='quad', color=color.light_gray, position=(0.6,-0.3), scale=(0.2, 0.2), texture='white_cube')
    altimeter = Text(text='ALT: 0000 ft', position=(0.5,-0.45), scale=1)
    speedometer = Text(text='SPD: 000 knots', position=(0.5,-0.5), scale=1)
    return {'horizon': horizon, 'altimeter': altimeter, 'speedometer': speedometer}

def update_instruments(panel, aircraft):
    panel['altimeter'].text = f"ALT: {int(aircraft.y * 100)} ft"
    panel['speedometer'].text = f"SPD: {int(aircraft.speed * 20)} knots"