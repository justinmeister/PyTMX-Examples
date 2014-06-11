import sys, os
import pygame as pg
import tilerender

"""Initialize pygame, create a clock, create the window
with a surface to blit the map onto."""
pg.init()
fps_clock = pg.time.Clock()
main_surface = pg.display.set_mode((420, 420))
main_rect = main_surface.get_rect()


"""Load the tmx file from the current directory,
create the tile_renderer object and load the tmx
file."""
tmx_file = os.path.join(os.getcwd(), 'test.tmx')
tile_renderer = tilerender.Renderer(tmx_file)


"""Create the map surface using the make_map()
method.  Used to blit onto the main_surface."""
map_surface = tile_renderer.make_map()
map_rect = map_surface.get_rect()


"""Simple game loop that blits the map_surface onto
the main_surface."""
while True:
    main_surface.blit(map_surface, map_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
    fps_clock.tick(30)

