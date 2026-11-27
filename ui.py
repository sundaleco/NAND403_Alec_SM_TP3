from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QGroupBox, QSpinBox
from PySide6.QtCore import Qt

import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance


import importlib
import animator
importlib.reload(animator)


def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)


class ProgramUI(QWidget):

    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowTitle("Random Animation Generator")
        self.setWindowFlags(Qt.Window)
        self.create_ui()

    def create_ui(self):
        self.layout_main = QVBoxLayout(self)

        self.create_timing()
        self.translate_settings()
        self.rotate_settings()
        self.scale_settings()
        self.create_button()
  
    def create_timing(self):
        group_timing = QGroupBox("Animation Timing")
        layout_timing = QHBoxLayout()

        layout_timing.addWidget(QLabel("Durations (Frames):"))

        self.duration = QSpinBox()
        self.duration.setRange(1, 10000)
        self.duration.setValue(100)

        layout_timing.addWidget(self.duration)

        layout_timing.addWidget(QLabel("Step (Frames):"))

        self.step = QSpinBox()
        self.step.setRange(1, 10000)
        self.step.setValue(30)

        layout_timing.addWidget(self.step)

        group_timing.setLayout(layout_timing)

        self.layout_main.addWidget(group_timing)

    def translate_settings(self):
        group_translate = QGroupBox("Translate Parameters")
        layout_translate = QGridLayout()

        self.translate_min_x = QSpinBox()
        self.translate_min_x.setRange(-1000, 1000)
        self.translate_min_x.setValue(-5)

        self.translate_min_y = QSpinBox()
        self.translate_min_y.setRange(-1000, 1000)
        self.translate_min_y.setValue(-5)

        self.translate_min_z = QSpinBox()
        self.translate_min_z.setRange(-1000, 1000)
        self.translate_min_z.setValue(-5)

        self.translate_max_x = QSpinBox()
        self.translate_max_x.setRange(-1000, 1000)
        self.translate_max_x.setValue(5)

        self.translate_max_y = QSpinBox()
        self.translate_max_y.setRange(-1000, 1000)
        self.translate_max_y.setValue(5)

        self.translate_max_z = QSpinBox()
        self.translate_max_z.setRange(-1000, 1000)
        self.translate_max_z.setValue(5)

        layout_translate.addWidget(QLabel("min x:"), 0, 0)
        layout_translate.addWidget(self.translate_min_x, 0, 1)
        layout_translate.addWidget(QLabel("min y:"), 0, 2)
        layout_translate.addWidget(self.translate_min_y, 0, 3)
        layout_translate.addWidget(QLabel("min z:"), 0, 4)
        layout_translate.addWidget(self.translate_min_z, 0, 5)

        layout_translate.addWidget(QLabel("max x:"), 1, 0)
        layout_translate.addWidget(self.translate_max_x, 1, 1)
        layout_translate.addWidget(QLabel("max y:"), 1, 2)
        layout_translate.addWidget(self.translate_max_y, 1, 3)
        layout_translate.addWidget(QLabel("max z:"), 1, 4)
        layout_translate.addWidget(self.translate_max_z, 1, 5)

        layout_translate.setVerticalSpacing(40)

        group_translate.setLayout(layout_translate)

        self.layout_main.addWidget(group_translate)

    def rotate_settings(self):
        group_rotate = QGroupBox("Rotate Parameters")
        layout_rotate = QGridLayout()

        self.rotate_min_x = QSpinBox()
        self.rotate_min_x.setRange(-360, 360)
        self.rotate_min_x.setValue(-180)

        self.rotate_min_y = QSpinBox()
        self.rotate_min_y.setRange(-360, 360)
        self.rotate_min_y.setValue(-180)

        self.rotate_min_z = QSpinBox()
        self.rotate_min_z.setRange(-360, 360)
        self.rotate_min_z.setValue(-180)

        self.rotate_max_x = QSpinBox()
        self.rotate_max_x.setRange(-360, 360)
        self.rotate_max_x.setValue(180)

        self.rotate_max_y = QSpinBox()
        self.rotate_max_y.setRange(-360, 360)
        self.rotate_max_y.setValue(180)

        self.rotate_max_z = QSpinBox()
        self.rotate_max_z.setRange(-360, 360)
        self.rotate_max_z.setValue(180)

        layout_rotate.addWidget(QLabel("min x:"), 0, 0)
        layout_rotate.addWidget(self.rotate_min_x, 0, 1)
        layout_rotate.addWidget(QLabel("min y:"), 0, 2)
        layout_rotate.addWidget(self.rotate_min_y, 0, 3)
        layout_rotate.addWidget(QLabel("min z:"), 0, 4)
        layout_rotate.addWidget(self.rotate_min_z, 0, 5)

        layout_rotate.addWidget(QLabel("max x:"), 1, 0)
        layout_rotate.addWidget(self.rotate_max_x, 1, 1)
        layout_rotate.addWidget(QLabel("max y:"), 1, 2)
        layout_rotate.addWidget(self.rotate_max_y, 1, 3)
        layout_rotate.addWidget(QLabel("max z:"), 1, 4)
        layout_rotate.addWidget(self.rotate_max_z, 1, 5)

        layout_rotate.setVerticalSpacing(40)

        group_rotate.setLayout(layout_rotate)
        self.layout_main.addWidget(group_rotate)
    
    def scale_settings(self):
        group_scale = QGroupBox("Scale Parameters")
        layout_scale = QGridLayout()

        self.scale_min_x = QSpinBox()
        self.scale_min_x.setRange(0, 100)
        self.scale_min_x.setValue(1)

        self.scale_min_y = QSpinBox()
        self.scale_min_y.setRange(0, 100)
        self.scale_min_y.setValue(1)

        self.scale_min_z = QSpinBox()
        self.scale_min_z.setRange(0, 100)
        self.scale_min_z.setValue(1)

        self.scale_max_x = QSpinBox()
        self.scale_max_x.setRange(0, 100)
        self.scale_max_x.setValue(2)

        self.scale_max_y = QSpinBox()
        self.scale_max_y.setRange(0, 100)
        self.scale_max_y.setValue(2)

        self.scale_max_z = QSpinBox()
        self.scale_max_z.setRange(0, 100)
        self.scale_max_z.setValue(2)

        layout_scale.addWidget(QLabel("min x:"), 0, 0)
        layout_scale.addWidget(self.scale_min_x, 0, 1)
        layout_scale.addWidget(QLabel("min y:"), 0, 2)
        layout_scale.addWidget(self.scale_min_y, 0, 3)
        layout_scale.addWidget(QLabel("min z:"), 0, 4)
        layout_scale.addWidget(self.scale_min_z, 0, 5)

        layout_scale.addWidget(QLabel("max x:"), 1, 0)
        layout_scale.addWidget(self.scale_max_x, 1, 1)
        layout_scale.addWidget(QLabel("max y:"), 1, 2)
        layout_scale.addWidget(self.scale_max_y, 1, 3)
        layout_scale.addWidget(QLabel("max z:"), 1, 4)
        layout_scale.addWidget(self.scale_max_z, 1, 5)

        layout_scale.setVerticalSpacing(40)

        group_scale.setLayout(layout_scale)
        self.layout_main.addWidget(group_scale)

    def get_values(self):

        self.duration_frames = self.duration.value()
        self.step_frames = self.step.value()


        self.min_tx = self.translate_min_x.value()
        self.min_ty = self.translate_min_y.value()
        self.min_tz = self.translate_min_z.value()

        self.max_tx = self.translate_max_x.value()
        self.max_ty = self.translate_max_y.value()
        self.max_tz = self.translate_max_z.value()

        self.min_rx = self.rotate_min_x.value()
        self.min_ry = self.rotate_min_y.value()
        self.min_rz = self.rotate_min_z.value()

        self.max_rx = self.rotate_max_x.value()
        self.max_ry = self.rotate_max_y.value()
        self.max_rz = self.rotate_max_z.value()

        self.min_sx = self.scale_min_x.value()
        self.min_sy = self.scale_min_y.value()
        self.min_sz = self.scale_min_z.value()

        self.max_sx = self.scale_max_x.value()
        self.max_sy = self.scale_max_y.value()
        self.max_sz = self.scale_max_z.value()

    def generate(self): #tout les parametres sont entrés ici
        self.get_values()

        animator.generate_animation(

            self.duration_frames, self.step_frames,

            self.max_tx, self.max_ty, self.max_tz,
            self.min_tx, self.min_ty, self.min_tz,

            self.max_rx, self.max_ry, self.max_rz,
            self.min_rx, self.min_ry, self.min_rz,

            self.max_sx, self.max_sy, self.max_sz,
            self.min_sx, self.min_sy, self.min_sz
        )

    def create_button(self):
                self.generate_button = QPushButton("Generate")
                self.layout_main.addWidget(self.generate_button)

                self.generate_button.clicked.connect(self.generate)
# correction