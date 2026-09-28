'''ABCs make an interface explicit. A concrete subclass must implement required abstract methods before it can be instantiated.'''

from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def predict(self, x):
        ...

class LinearModel(Model):
    def predict(self, x):
        return x
