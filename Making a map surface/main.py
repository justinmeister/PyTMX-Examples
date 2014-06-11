import sys, os
import pygame as pg
import tilerender

pg.init()
fps_clock = pg.time.Clock()
main_surface = pg.display.set_mode((420, 420))
main_rect = main_surface.get_rect()

tmx_file = os.path.join(os.getcwd(), 'test.tmx')
tile_renderer = tilerender.Renderer(tmx_file)

map_surface = tile_renderer.make_map()
map_rect = map_surface.get_rect()

while True:
    main_surface.fill((0,0,0))
    main_surface.blit(map_surface, map_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
    fps_clock.tick(30)

