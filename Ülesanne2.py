import pygame

# Käivita Pygame
pygame.init()

# Loo aken suurusega 640x480 pikslit
aken = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ulesanne 2")  # Määra akna pealkiri

# Lae taustapilt ja pildid müüjast ning jutumullist
taust = pygame.image.load("bg_shop.png")
seller = pygame.image.load("seller.png")
jutumull = pygame.image.load("chat.png")

# Muuda müüja ja jutumulli suurust
seller = pygame.transform.scale(seller, (255, 305))
jutumull = pygame.transform.scale(jutumull, (255, 200))

# Joonista taust, müüja ja jutumull aknale
aken.blit(taust, [0, 0])               # Taustapilt
aken.blit(seller, [105, 160])          # Müüja pilt
aken.blit(jutumull, [247, 67])         # Jutumull müüja kõrval

# Lisa tekst jutumulli sisse
font = pygame.font.SysFont("Tahoma", 35)  # Font ja suurus
tekst = font.render("Martin", True, [255, 255, 255])  # Renderda valge tekst
aken.blit(tekst, [325, 145])  # Kuvatakse jutumulli sees

# Uuenda ekraani
pygame.display.update()

# Tsükkel, mis hoiab akna avatuna kuni kasutaja selle sulgeb
tootab = True
while tootab:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False
