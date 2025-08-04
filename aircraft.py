from ursina import *

class Bullet(Entity):
    def __init__(self, position, direction):
        super().__init__(
            model='sphere',
            scale=0.05,
            color=color.yellow,
            position=position,
            collider='box'
        )
        self.direction = direction
        self.speed = 30
        self.life_timer = 1.5

    def update(self):
        self.position += self.direction * time.dt * self.speed
        self.life_timer -= time.dt
        if self.life_timer <= 0:
            destroy(self)

class Aircraft(Entity):
    def __init__(self):
        super().__init__(
            model=Entity(model='jet.glb'),
            scale=(1, 0.3, 2),
            position=(0, -1, 0),
            collider='box'
        )
        self.speed = 5
        self.rotation_speed = 60
        self.velocity_y = 0
        self.gravity = -2.8
        self.landed = False
        self.fire_rate = 0.2
        self.fire_timer = 0
        self.bullets_remaining = 1000000

        # HUD Elements
        self.altitude_display = Text(text='ALT: 0', position=(-0.85, 0.4), scale=1.5, color=color.green)
        self.speed_display = Text(text='SPD: 0', position=(-0.85, 0.3), scale=1.5, color=color.green)
        self.pitch_display = Text(text='PITCH: 0', position=(-0.85, 0.2), scale=1.5, color=color.green)
        self.compass_display = Text(text='HDG: 000°', position=(-0.85, 0.1), scale=1.5, color=color.green)
        self.lock_display = Text(text='LOCK: None', position=(-0.85, 0.0), scale=1.5, color=color.red)
        self.bullet_display = Text(text='AMMO: 100', position=(-0.85, -0.1), scale=1.5, color=color.green)
        self.crosshair = Entity(model='circle', color=color.green, scale=(0.01, 0.01), position=(0, 0), parent=camera.ui)

    def update(self):
        # Ground detection
        if self.y <= -1:
            self.y = -1
            self.velocity_y = 0
            self.landed = True
        else:
            self.landed = False

        # Forward motion
        if not self.landed:
            self.position += -self.forward * time.dt * self.speed

        # Rotation controls
        if held_keys['a']:
            self.rotation_y += self.rotation_speed * time.dt
        if held_keys['d']:
            self.rotation_y -= self.rotation_speed * time.dt
        if held_keys['w']:
            self.rotation_x -= self.rotation_speed * time.dt
        if held_keys['s']:
            self.rotation_x += self.rotation_speed * time.dt

        # HUD updates
        self.altitude_display.text = f'ALT: {round(self.y, 2)}'
        self.speed_display.text = f'SPD: {self.speed}'
        self.pitch_display.text = f'PITCH: {round(self.rotation_x, 2)}'
        heading = int(self.rotation_y % 360)
        self.compass_display.text = f'HDG: {heading:03d}°'
        self.lock_display.text = 'LOCK: Target' if held_keys['l'] else 'LOCK: None'
        self.bullet_display.text = f'AMMO: {self.bullets_remaining}'

        # Fire bullets from nose
        self.fire_timer -= time.dt
        if held_keys['space'] and self.fire_timer <= 0 and self.bullets_remaining > 0:
            nose_position = self.world_position + -self.forward * 1.2
            bullet = Bullet(position=nose_position, direction=-self.forward)
            self.fire_timer = self.fire_rate
            shoot_sound = Audio('gun.mp3', loop=False, autoplay=True)
            self.bullets_remaining -= 1

class Enemy(Entity):
    def __init__(self, target):
        super().__init__(
            model=Entity(model='jet.glb'),
            scale=(1, 0.3, 2),
            position=(5, 2, 20),
            collider='box'
        )
        self.target = target
        self.speed = 3
        self.fire_rate = 1.0
        self.fire_timer = 0

    def update(self):
        if self.target:
            # Move toward the player's aircraft
            direction = (self.target.world_position - self.world_position).normalized()
            self.position += direction * time.dt * self.speed

            # Rotate to face the player
            self.look_at(self.target)

            # Shoot occasionally
            self.fire_timer -= time.dt
            if self.fire_timer <= 0:
                bullet = Bullet(position=self.world_position + self.forward * 1.2, direction=self.forward)
                self.fire_timer = self.fire_rate

# Run the simulation
app = Ursina()
aircraft = Aircraft()
enemy = Enemy(target=aircraft)
app.run()