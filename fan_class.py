class Fan:
    # Three constant fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = True):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed in (Fan.SLOW, Fan.MEDIUM, Fan.FAST):
            self.__speed = new_speed
        else:
            raise TypeError("Invalid speed")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        self.__radius = float(new_radius)
        


