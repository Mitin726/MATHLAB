from .figure2D import Figure2D
import math

class Circle(Figure2D):
  def __init__(self, radius: float):
    if radius <= 0:
        raise ValueError("The radius must be greater than zero...")
      
    self.radius = radius
    
  def calculate_area(self) -> float:
    return math.pi * (self.radius**2)
  
  def calculate_perimeter(self) -> float:
    return 2 * math.pi * self.radius
  
  def __str__(self) -> str:
    return f"Circle(Radius: {self.radius})"
  
  def info(self):
    return f"""
            {self}
            Area: {self.calculate_area():.2f}
            Perimeter: {self.calculate_perimeter():.2f}
            """