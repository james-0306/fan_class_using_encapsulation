from fan_class import Fan

first_fan = Fan()
first_fan.speed = Fan.FAST
first_fan.radius = 10
first_fan.color = "yellow"
first_fan.is_on = True

second_fan = Fan()
second_fan.speed = Fan.MEDIUM
second_fan.radius = 5
second_fan.color = "blue"
second_fan.is_on = False

# first fan
print("FIRST FAN")
print("Speed:", first_fan.speed)
print("Radius:", first_fan.radius)
print("Color:", first_fan.color)
print("Is on:", first_fan.is_on)

print()
print()

# second fan
print("SECOND FAN")
print("Speed:", second_fan.speed)
print("Radius:", second_fan.radius)
print("Color:", second_fan.color)
print("Is on:", second_fan.is_on)