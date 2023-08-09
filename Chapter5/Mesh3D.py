from OpenGL.GL import *
import pygame

class Mesh3D:
    def __init__(self):
        self.verticies = [(0.5, -0.5, 0.5), 
                          (-0.5, -0.5, 0.5), 
                          (0.5, 0.5, 0.5), 
                          (-0.5, 0.5, 0.5), 
                          (0.5, 0.5, -0.5), 
                          (-0.5, 0.5, -0.5)]
        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP
        self.texture = pygame.image.load()
        self.texID = 0
    def draw(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        uv_len = len(self.uvs)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glTexCoord2fv(self.uvs[(t)%uv_len])
            glVertex3fv(self.verticies[self.triangles[t]])
            glTexCoord2fv(self.uvs[(t+1)%uv_len])
            glVertex3fv(self.verticies[self.triangles[t+1]])
            glTexCoord2fv(self.uvs[(t+2)%uv_len])
            glVertex3fv(self.verticies[self.triangles[t+2]])
            glEnd()
    def init_texture(self):
        self.texID = glGenTextures(1)
        textureData = pygame.image.tostring(self.texture, "RGB", 1)
        width = self.texture.get_width()
        height = self.texture.get_height()
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)