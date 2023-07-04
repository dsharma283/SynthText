import pygame
import pygame.locals
import sys

pygame.init()
screen = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

#font = pygame.freetype.Font("/usr/share/fonts/truetype/Sarai/Sarai.ttf", 50)
#font.set_script("Deva")
#surf = pygame.Surface((200, 70), pygame.locals.SRCALPHA, 32)
#print(surf)
#im = font.render(text, True, "black")
#im = font.render(text True, "black")
#print(im)
#rect = font.get_rect(text, rotation=0)
#im = font.render_to(surf, rect, text, rotation=0)
#print(rect)
#print(im)
#r = surf.get_rect()
#print(f'r = {r}')
#r.x += 10
#r.y += 10
#rect = surf.blit(im, r)
#print(f'rect = {rect}')

def display_object(obj):
    while True:
        screen.fill("lightgreen")
        screen.blit(obj, (10,10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        pygame.display.flip()
        clock.tick(144)


def render_sdl_ttf(fontpath, text, set_style):
    font = pygame.font.Font(fontpath, 50)
    if set_style:
        font.set_script("Deva")
    im = font.render(text, True, "black")
    display_object(im)


def render_ft(fontpath, text, use_render=0):
    pygame.freetype.init()
    font = pygame.freetype.Font(fontpath, 50)
    surf = pygame.Surface((200, 70), pygame.locals.SRCALPHA, 32)
    if use_render == 0:
        rect = font.get_rect(text, rotation=0)
        im = font.render_to(surf, rect, text, rotation=0,
                            style=pygame.freetype.STYLE_NORMAL)
        im = surf
    else:
        im = font.render(text, "black",
                         style=pygame.freetype.STYLE_NORMAL)
        im = im[0]
    display_object(im)


def start_main(ftype, fontpath, text, use_render, set_style):
    if ftype == 'sdl_ttf':
        render_sdl_ttf(fontpath, text, set_style)
    elif ftype == 'ft':
        render_ft(fontpath, text, use_render)
    else:
        print("Invalid font lib type")


if __name__ == "__main__":
    text = f"सुरक्षा"
    fontpath = f"/usr/share/fonts/truetype/Sarai/Sarai.ttf"
    if len(sys.argv) != 4:
        print(f'Usage:\n\t{sys.argv[0]} <font type to use>[sdl_ttf, ft]',
              f'\n\t<use render() api for ft type [0, 1]>',
              f'\n\t<use set_stype api for sdl_ttf type [0, 1]>')
        exit(-1)
    ftype = sys.argv[1]
    if isinstance(ftype, str) is False:
        print(f"Specify only strings")
        exit(-1)
    use_render = sys.argv[2]
    if use_render != '0' and use_render != '1':
        print(f"Specify 0 or 1")
        exit(-1)
    use_render = int(use_render)

    set_style = sys.argv[3]
    if set_style != '0' and set_style != '1':
        print(f"Specify 0 or 1")
        exit(-1)
    set_style = int(set_style)
    start_main(ftype, fontpath, text, use_render, set_style)

