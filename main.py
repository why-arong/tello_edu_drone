from djitellopy import Tello


def execute_maneuver(tello, action, value):
    if action == "up":
        tello.move_up(value)
    elif action == "rotate_right":
        tello.rotate_clockwise(value)
    elif action == "rotate_left":
        tello.rotate_counter_clockwise(value)
    elif action == "forward":
        tello.move_forward(value)


tello = Tello()
tello.connect()
tello.takeoff()

maneuvers = [
    ("up", 100),
    ("rotate_right", 30),
    ("forward", 10),
    ("rotate_left", 120),
    ("forward", 10),
    ("rotate_left", 120),
    ("forward", 10),
    ("rotate_right", 30),
    ("forward", 10)
]

for action, value in maneuvers:
    execute_maneuver(tello, action, value)

tello.land()
tello.end()
