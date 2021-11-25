# Based on https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images

import os
import pygame


pygame.init()

SIZE = WIDTH, HEIGHT = 720, 480
BACKGROUND_COLOR = pygame.Color('black')
FPS = 100

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def load_images(path):
    """
    Loads all images in directory. The directory must only contain images.

    Args:
        path: The relative or absolute path to the directory to load images from.

    Returns:
        List of images.
    """
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images


class GameManager:

    def __init__(self, size, background_color, fps, sprites, player):
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.bg_color = background_color
        self.sprites = sprites
        self.player = player
        self.dt = fps / 1.e+3
        self.finish = False

    def run(self):
        self.sprites.update(self.dt)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.finish = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.move("right")
                elif event.key == pygame.K_LEFT:
                    self.player.move("left")
                elif event.key == pygame.K_DOWN:
                    self.player.move("down")
                elif event.key == pygame.K_UP:
                    self.player.move("up")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.player.move("stop_horizontal")
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    self.player.move("stop_vertical")


class AnimatedSprite(pygame.sprite.Sprite):
    size = (32, 32)  # This should match the size of the images.

    def __init__(self, position, images):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()


        self.rect = pygame.Rect(position, self.size)
        self.images = images
        self.images_right = images
        # Flipping every image.
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]
        self.images_up = [pygame.transform.rotate(image, -90) for image in images]
        self.images_down = [pygame.transform.rotate(image, 90) for image in images]
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def move(self, direction):
        if direction == "right":
            self.velocity.x = 4
        elif direction == "left":
            self.velocity.x = -4
        elif direction == "up":
            self.velocity.y = -4
        elif direction == "down":
            self.velocity.y = 4
        if direction == "stop_horizontal":
            self.velocity.x = 0
        elif direction == "stop_vertical":
            self.velocity.y = 0

    def update_time_dependent(self, dt):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """
        self._set_image_direction()

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        """
        Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).
        """
        self._set_image_direction()

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update(self, dt, dependence="time"):
        """This is the method that's being called when 'all_sprites.update(dt)' is called."""
        if dependence == "time":
            self.update_time_dependent(dt)
        elif dependence == "frame":
            self.update_frame_dependent()

    def _set_image_direction(self):
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left
        if self.velocity.y > 0:
            self.images = self.images_up
        elif self.velocity.y < 0:
            self.images = self.images_down


def main():
    images = load_images(path='./sprites')  # Make sure to provide the relative or full path to the images directory.
    player = AnimatedSprite(position=(100, 100), images=images)
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.
    game_provider = GameManager(SIZE, BACKGROUND_COLOR, FPS, all_sprites, player)

    while not game_provider.finish:

    #     dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_RIGHT:
    #                 player.velocity.x = 4
    #             elif event.key == pygame.K_LEFT:
    #                 player.velocity.x = -4
    #             elif event.key == pygame.K_DOWN:
    #                 player.velocity.y = 4
    #             elif event.key == pygame.K_UP:
    #                 player.velocity.y = -4
    #         elif event.type == pygame.KEYUP:
    #             if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
    #                 player.velocity.x = 0
    #             elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
    #                 player.velocity.y = 0
        game_provider.handle_event()
        game_provider.run()

        # all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).

        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
