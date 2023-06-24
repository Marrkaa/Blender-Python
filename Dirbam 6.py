import bpy
import math

from mathutils import Matrix as Matrica

objektas = bpy.context.object

def Funkcija():
    
    M = objektas.matrix_world
    
    for i in range(4):
        naujas_objektas = objektas.copy()
        naujas_objektas.data = objektas.data.copy()
        S1 = Matrica.Scale(0.5, 4)
        l = (0.5*objektas.dimensions.x + math.sqrt(pow(objektas.dimensions.x, 2) + pow(objektas.dimensions.y, 2))) / 2
        M1 = Matrica.Translation((l, 0, 0))
        R1 = Matrica.Rotation(math.radians(45 + 90*i), 4, 'Z')
        naujas_objektas.matrix_world = M @ R1 @ M1 @ S1
        bpy.data.scenes[0].collection.objects.link(naujas_objektas)
        
    for i in range(8):
        naujas_objektas = objektas.copy()
        naujas_objektas.data = objektas.data.copy()
        S1 = Matrica.Scale(0.25, 4)
        l = (0.5*objektas.dimensions.x + math.sqrt(pow(objektas.dimensions.x, 2) + pow(objektas.dimensions.y, 2))) / 2
        l1 = (1 + 0.25)*l
        M1 = Matrica.Translation((0, l1, 0))
        R1 = Matrica.Rotation(math.radians(22.5 + 45*i), 4, 'X')
        naujas_objektas.matrix_world = M @ R1 @ M1 @ S1
        bpy.data.scenes[0].collection.objects.link(naujas_objektas)
    
    return
        
Funkcija()


