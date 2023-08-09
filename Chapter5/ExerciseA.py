from OpenGL.GL import *
from Mesh3D import *

class Cube(Mesh3D):
    def __init__(self, draw_type, filename):
        self.verticies = [(0.5, -0.5, 0.5),  # _-_ 0
                          (-0.5, -0.5, 0.5),  # --_ 1
                          (0.5, 0.5, 0.5),  # ___ 2
                          (-0.5, 0.5, 0.5),  # -__ 3
                          (0.5, -0.5, -0.5),  # _-- 4
                          (-0.5, -0.5, -0.5),  # --- 5
                          (0.5, 0.5, -0.5),  # __- 6
                          (-0.5, 0.5, -0.5)]  # -_- 7
        self.triangles = [0, 2, 3, 0, 3, 1,
                          2, 6, 7, 2, 7, 3, #North
                          6, 4, 5, 6, 5, 7,
                          4, 0, 1, 4, 1, 5,
                          1, 3, 7, 1, 7, 5,
                          4, 6, 2, 4, 2, 0]
        self.uvs = [(1.0, 0.0),
                    (1.0, 1.0),
                    (0.0, 1.0),
                    (1.0, 0.0),
                    (0.0, 1.0),
                    (0.0, 0.0)]
        Mesh3D.texture = pygame.image.load(filename)
        Mesh3D.draw_type = draw_type
        Mesh3D.init_texture(self)
