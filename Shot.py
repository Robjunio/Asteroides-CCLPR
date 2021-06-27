import pygame
import assets
from pygame.math import Vector2
from pygame.transform import rotozoom

class Shot():
    def __init__(self, bullet_speed, bullet_pos):
<<<<<<< HEAD
        super().__init__(bullet_speed, load_sprite("bullet"), bullet_speed)

def __init__(self):
    self.__init_pygame()
    self.screen = pygame.display.set_mode((800, 600))
    self.background = load_sprite("space", False)
    self.clock = pygame.time.Clock()

    self.asteroids = []
    self.bullets = []
    self.spaceship = SpaceShip((400, 300))

    for _ in range(6):
        while True:
            position.distance_to(self.sapceship.position)
            if (
                position.distance_to(self.spaceship.position)
                > self.MIN_ASTEROID_DISTANCE
            ):
                break

        self.asteroids.append(Asteroid(position))

def _get_game_objects(self):
    game_objects = [*self.asteroids, *self.bullets]

    if self.spaceship:
        game_objects.append(self.spaceship)

    return game_objects

def __init__(self, position, create_bullet_callback):
    self.create_bullet_callback = create_bullet_callback
    # Make a copy of the original UP vector
    self.direction = Vector2(UP)

    super().__init__(position, load_sprite("spaceship"), Vector2(0))

def shoot(self):
    bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
    bullet = Bullet(self.position, bullet_velocity)
    self.create_bullet_callback(bullet)

def __init__(self):
    self._init_pygame()
    self.screen = pygame.display.set_mode((800, 600))
    self.background = load_sprite("space", False)
    self.clock = pygame.time.Clock()

    self.asteroids = []
    self.bullets = []
    self.spaceship = Spaceship((400, 300), self.bullets.append)

    for _ in range(6):
        while True:
            position = get_random_position(self.screen)
            if (
                position.distance_to(self.spaceship.position)
                > self.MIN_ASTEROID_DISTANCE
            ):
                break

        self.asteroids.append(Asteroid(position))

def _handle_input(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            quit()
        elif (
            self.spaceship
            and event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
        ):
            self.spaceship.shoot()

    is_key_pressed = pygame.key.get_pressed()

    if self.spaceship:
        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()

def move(self, surface):
    self.position = self.position + self.velocity

def _process_game_logic(self):

    for game_object in self._get_game_objects():

        game_object.move(self.screen)


    if self.spaceship:

        for asteroid in self.asteroids:

            if asteroid.collides_with(self.spaceship):

                self.spaceship = None

                break


    for bullet in self.bullets[:]:

        if not self.screen.get_rect().collidepoint(bullet.position):

            self.bullets.remove(bullet)

def _process_game_logic(self):

    for game_object in self._get_game_objects():

        game_object.move(self.screen)


    if self.spaceship:

        for asteroid in self.asteroids:

            if asteroid.collides_with(self.spaceship):

                self.spaceship = None

                break


    for bullet in self.bullets[:]:

        for asteroid in self.asteroids[:]:

            if asteroid.collides_with(bullet):

                self.asteroids.remove(asteroid)

                self.bullets.remove(bullet)

                break


    for bullet in self.bullets[:]:

        if not self.screen.get_rect().collidepoint(bullet.position):
=======
        self.bullet_speed = bullet_speed
        self.bullet_pos = bullet_pos
        self.sprite = pygame.image.load("assets/bullet.png")
        self.radius = self.sprite.get_width() / 2
    
    def draw(self, surface):
        blit_position = self.bullet_pos - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)
    
    def move(self):
        self.bullet_pos += self.bullet_speed
>>>>>>> 35ea1a1f00e719fc443a9e9fcbe4bd697764d440

