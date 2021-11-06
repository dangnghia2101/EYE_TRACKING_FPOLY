from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
import numpy as np
import cv2
from gaze_tracking import GazeTracking

Builder.load_file('layout.kv')
gaze = GazeTracking()

class AndroidCamera(Camera):
    camera_resolution = (640, 480)
    cam_ratio = camera_resolution[0] / camera_resolution[1]

class MyLayout(BoxLayout):
    pass


class MyApp(App):
    counter = 0

    def build(self):
        return MyLayout()

    def on_start(self):
        Clock.schedule_once(self.get_frame, 5)

    def get_frame(self, dt):
        cam = self.root.ids.a_cam
        image_object = cam.export_as_image(scale=round((400 / int(cam.height)), 2))
        w, h = image_object._texture.size
        frame = np.frombuffer(image_object._texture.pixels, 'uint8').reshape(h, w, 4)
        # gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        
        gaze.refresh(frame)
        text = ""

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        self.root.ids.frame_counter.text = f'check: {text}'
        # self.counter += 1
        Clock.schedule_once(self.get_frame, 0.25)

if __name__ == "__main__":
    MyApp().run()