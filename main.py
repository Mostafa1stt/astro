from player import *
from asteroid import *
from asteroidfield import *
import sys


def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    draw_able = pygame.sprite.Group()
    update_able = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    AsteroidField.containers = (update_able)
    Shot.containers = (update_able,draw_able,shots_group)
    Asteroid.containers = (asteroid_group, draw_able, update_able)
    Player.containers = (draw_able, update_able)

    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroidField_obj = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        update_able.update(dt)

        for obj in asteroid_group:
            if obj.collisions(player):
                print("Game over!")
                sys.exit()

        for obj in asteroid_group:
            for bullet in shots_group:
                if obj.collisions(bullet):
                    obj.split()
                    bullet.kill()

        screen.fill("black")
        for obj in draw_able:
            obj.draw(screen)

        pygame.display.flip()
        dt = (fps.tick(60))/1000


if __name__ == "__main__":
    main()
