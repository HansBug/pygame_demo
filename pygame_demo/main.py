import asyncio
import sys

import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 500])
base_font = pygame.font.Font(None, 32)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


async def main():
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("white")

        pygame.draw.circle(screen, "blue", player_pos, 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        pygame.display.flip()
        # clock.tick(60)
        dt = clock.tick(60) / 1000
        await asyncio.sleep(0)


asyncio.run(main())
