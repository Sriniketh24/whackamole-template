import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_width, mole_height = mole_image.get_size()

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        grid_width = 640
        grid_height = 512
        square_size = 32
        rows = grid_height // square_size
        cols = grid_width // square_size

        mole_pos = (0, 0)

        def draw_grid():
            for row in range(rows + 1):  # +1 to draw the last line
                pygame.draw.line(screen, "black", (0, row * square_size), (grid_width, row * square_size))
            for col in range(cols + 1):  # +1 to draw the last line
                pygame.draw.line(screen, "black", (col * square_size, 0), (col * square_size, grid_height))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    mole_rect = pygame.Rect(mole_pos[0], mole_pos[1], square_size, square_size)
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        mole_pos = (random.randrange(0, cols) * square_size, random.randrange(0, rows) * square_size)

            screen.fill("light green")

            draw_grid()

            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))

            pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()