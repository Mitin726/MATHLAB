from figure2D import Figure2D

class Square(Figure2D):
  def __init__(self, side: float):
    if side <= 0:
        raise ValueError("The side must be greater than zero...")
      
    self.side = side
    
  def calculate_area(self) -> float:
    return self.side**2
  
  def calculate_perimeter(self) -> float:
    return self.side * 4
  
  def __str__(self) -> str:
    return f"Square\nSide: {self.side}"
  
  def info(self):
    return f"""
            {self}
            Area: {self.calculate_area():.2f}
            Perimeter: {self.calculate_perimeter():.2f}
            """