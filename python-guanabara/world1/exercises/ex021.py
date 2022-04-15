# DESAFIO 021
# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("/home/trustindestiny/Música/samsung.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

