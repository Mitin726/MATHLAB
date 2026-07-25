from abc import ABC, abstractmethod

class Figure3D(ABC):
    @abstractmethod
    def calculate_volume(self):
        pass
    
    @abstractmethod
    def calculate_surface_area(self):
        pass