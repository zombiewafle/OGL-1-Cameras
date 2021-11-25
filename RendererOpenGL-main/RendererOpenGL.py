import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders
from OpenGL.GLU import *
from pygame.math import Vector2


width = 960
height = 540

deltaTime = 0.0

act_shader = 0
maxZoom = 3
actualZoom = 0


pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, 
                shaders.fragment_shader)
face = Model('model.obj', 'model.bmp')
face.position.z = -5

rend.scene.append( face )

camPos = Vector2(rend.camPosition[0],rend.camPosition[2])

eyeX = rend.camPosition.x 
eyeY = rend.camPosition.y 
eyeZ = rend.camPosition.z 
step = 10000

isRunning = True
while isRunning:

    gluLookAt(eyeX, eyeY, eyeZ, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        rend.camPosition.x += 1 * deltaTime
        #eyeX += step * deltaTime

    if keys[K_a]:
        rend.camPosition.x -= 1 * deltaTime
        #eyeX -= step * deltaTime

    if keys[K_w]:
        rend.camPosition.z += 1 * deltaTime
        #eyeY += step * deltaTime

    if keys[K_s]:
        if actualZoom > -maxZoom: 
            rend.camPosition.z -= 1 * deltaTime
            actualZoom -= 1 * deltaTime
        #eyeY -= step * deltaTime

    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
        #eyeZ -= step * deltaTime

    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime
        #eyeZ += step * deltaTime

    if keys[K_c]:
        face.position.z += 1 * deltaTime
        #face.position.z = -5

    if keys[K_v]:
        face.position.z -= 1 * deltaTime
        #face.position.z = -5

    if keys[K_LEFT]:
        if rend.valor > 0:
            rend.valor -= 0.1 * deltaTime

    if keys[K_RIGHT]:
        if rend.valor < 0.2:
            rend.valor += 0.1 * deltaTime

    # Rotacion de camara
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime





    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()

            if ev.key == pygame.K_PERIOD:
                    if act_shader != 5:
                        act_shader += 1
                    else:
                        act_shader = 0
                    if act_shader == 0:
                        rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                    elif act_shader == 1:
                        rend.setShaders(shaders.toon_shader_Vertex, shaders.toon_shader_fragment)
                    #elif act_shader == 2:
                    #   rend.setShaders(shaders.vertex_shader, shaders.fragment_static_shader)
            

            #if ev.key == K_4:
            #    rend.psicoShader()

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

    

pygame.quit()
