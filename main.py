import time
import cv2
from threading import Thread
from djitellopy import Tello


# 텔로 연결 시키기
def connect_to_tello():
    tello = Tello()
    tello.connect()
    return tello


# 각 행동에 맞는 행동을 지정함
def execute_maneuver(tello, action, value):
    if action == "up":
        tello.move_up(value)
    elif action == "rotate_right":
        tello.rotate_clockwise(value)
    elif action == "rotate_left":
        tello.rotate_counter_clockwise(value)
    elif action == "forward":
        tello.move_forward(value)


# 영상 녹화를 담당하는 함수
def video_recorder(frame_read, keepRecording):
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter(
        'video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording[0]:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()


# 취해야 할 행동을 input으로 받아 실제 행동을 시키는 함수
def perform_flight_maneuvers(tello, maneuvers):
    for action, value in maneuvers:
        execute_maneuver(tello, action, value)


def main():
    # 텔로 연결 시키기
    tello = connect_to_tello()

    # 드론이 움직이는 행동을 지정함
    # 이 코드를 그대로 실행한다면 "ㄷ"자 모양을 돌게 됨
    maneuvers = [
        ("up", 100),
        ("forward", 80),
        # 바람의 영향으로 90도 보다 더 돌아야 함
        ("rotate_left", 95),
        ("forward", 80),
        ("rotate_left", 90),
        ("forward", 100),
    ]

    # 드론으로 영상촬영을 위한 코드
    # dji tello py 라이브러리를 약간 수정했음
    # 기본적으로 thread 프로그래밍을 했음
    keepRecording = [True]
    tello.streamon()
    frame_read = tello.get_frame_read()
    # 조종과 동시에 비디오 녹화를 위해 python의 thread를 사용함.
    recorder = Thread(target=video_recorder, args=(frame_read, keepRecording))
    recorder.start()

    # 드론 움직임의 시작
    tello.takeoff()
    perform_flight_maneuvers(tello, maneuvers)
    tello.land()
    # 드론 움직임의 끝

    # 녹화 종료 -> video.avi에 저장
    keepRecording[0] = False
    recorder.join()


# 가장 먼저 실행되는 부분임.
# main 함수가 실행됨
if __name__ == "__main__":
    main()
