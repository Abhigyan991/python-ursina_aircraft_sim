from ursina import *
from perlin_noise import PerlinNoise

def setup_environment():
    Sky()
    ground = Entity(
        model='plane',
        texture='grass',
        scale=(100, 1, 100),
        collider='box',
        y = -1
    )