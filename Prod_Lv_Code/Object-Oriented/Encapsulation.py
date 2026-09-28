'''
Encapsulation is the practice of hiding an object's internal data and restricting direct access. In Python, 
this is done using naming conventions to create protected or private attributes, combined with public methods 
(getters and setters) or properties to manage them safely.

'''

class SmartThermostat:
    def __init__(self, owner, temperature):
        self.owner = owner
        self.__temperature = temperature  # Private attribute

    # Getter Method (Property decorator)
    @property
    def temperature(self):
        return self.__temperature

    # Setter Method (Enforces validation rules)
    @temperature.setter
    def temperature(self, new_temp):
        if 15 <= new_temp <= 30:  # Validation rule
            self.__temperature = new_temp
        else:
            print("Error: Temperature must be between 15°C and 30°C.")

# --- Usage ---
house = SmartThermostat("Alice", 22)
print(house.temperature)  # Output: 22 (Calls the getter method)

house.temperature = 45   # Output: Error: Temperature must be between 15°C and 30°C.
house.temperature = 24   # Updates successfully


## @property is the production pattern — controlled access instead of raw public attributes.

