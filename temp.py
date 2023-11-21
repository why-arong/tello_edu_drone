
from djitellopy import Tello
import time


def triangle_pattern(tello, side_length):
    # 삼각형의 각 꼭짓점에서의 회전 각도
    angle = 120

    # 삼각형의 세 변을 그립니다.
    for _ in range(3):
        tello.move_forward(side_length)
        tello.rotate_clockwise(angle)


tello = Tello()
tello.connect()
tello.takeoff()

# 삼각형 패턴을 그립니다. 여기서 side_length는 cm 단위입니다.
triangle_pattern(tello, 100)

tello.land()
tello.end()
