from ursina import *

def setup_camera(target):
    camera.parent = target
    camera.position = (-3, 5, 10)  # Behind the plane
    camera.rotation_y = 180  # Rotate to face forward
    camera.rotation_x = 20 # Rotate to face down
    camera.fov = 80