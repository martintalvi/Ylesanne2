import pygame

pygame.init()

aken = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ulesanne 2")

taust = pygame.image.load("bg_shop.png")
seller = pygame.image.load("seller.png",)
jutumull = pygame.image.load("chat.png")

seller = pygame.transform.scale(seller, (255, 305))
jutumull = pygame.transform.scale(jutumull, (255, 200))

aken.blit(taust, [0, 0])
aken.blit(seller, [105, 160])
aken.blit(jutumull, [247, 67])

font = pygame.font.SysFont("Tahoma", 35)
tekst = font.render("Martin", True, [255, 255, 255])
aken.blit(tekst, [325, 145])

pygame.display.flip()

tootab = True
while tootab:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False