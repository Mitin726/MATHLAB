from .figure3D import Figure3D
import math

class Sphere(Figure3D):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("The radius must be greater than zero...")
        
        self.radius = radius
        
    def calculate_volume(self):
        return 4/3 * math.pi * self.radius**3
    
    def calculate_surface_area(self):
        return 4 * math.pi * self.radius**2
    
    def __str__(self):
        return f"Sphere(radius: {self.radius})"
    
    def info(self):
        return f"""
                {self}
                Volume: {self.calculate_volume():.2f}
                Surface Area: {self.calculate_surface_area():.2f}
                """