#!/usr/bin/env python
# coding: utf-8

r"""Data flow elements"""

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg

from .base import *


class ShapePreview(NormalElement):
    name = "OCC Shape preview"
    comment = "Shows an OCC Shape"

    def get_attributes(self):
        return [Input("input")], \
               [Output("output")], \
               []

    def process_inputs(self, inputs, outputs, parameters):
        i = inputs["input"].value
        o = None

        if t == 0:
            o = i
        elif t == 10:
            o = i.clip(0, 255).astype(np.uint8)
        elif t == 20:
            o = i.astype(np.float32).clip(0.0, 1.0)
        elif t == 21:
            o = i.astype(np.float32)
            min_, max_, _, _ = cv.minMaxLoc(o.flatten())
            if min_ == max_:
                o = np.zeros(o.shape) + 0.5
            else:
                o = (o - min_) / (max_ - min_) + min_
        elif t == 22:
            o = i.astype(np.float32)
            min_, max_, _, _ = cv.minMaxLoc(o.flatten())
            if min_ == max_:
                o = np.zeros(o.shape) + 0.5
            else:
                if len(o.shape) > 2:
                    mean = cv.mean(cv.mean(o)[:3])[0]
                else:
                    mean = cv.mean(o)[0]
                scale = 0.5 / max(max_ - mean, mean - min_)
                o = (o - mean) * scale + 0.5
        elif t == 23:
            o = i / 255.
        elif t == 30:
            o = i.astype(np.float32)
            min_, max_, _, _ = cv.minMaxLoc(o.flatten())
            if min_ == max_:
                o = np.zeros(o.shape) + 0.5
            else:
                scale = 0.5 / max(max_, -min_)
                o = o * scale + 0.5

        outputs["output"] = Data(o)


register_elements_auto(__name__, locals(), "CAD Visualization", -98)
