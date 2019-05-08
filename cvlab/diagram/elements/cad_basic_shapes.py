#!/usr/bin/env python
# coding: utf-8

r"""Basic PythonOCC shapes"""

from .base import *
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder


class Cube(NormalElement):
    name = "Cube"
    comment = "A simple cube"

    def get_attributes(self):
        return [Input("input")], \
               [Output("output")], \
               [FloatParameter("size", "Size", 10, min_=0, max_=1000, step=10), ]

    def process_inputs(self, inputs, outputs, parameters):
        size = parameters["size"]
        cube = BRepPrimAPI_MakeBox(size, size, size).Shape()

        outputs["output"] = cube


class Cylinder(NormalElement):
    name = "Cylinder"
    comment = "A simple cylinder"

    def get_attributes(self):
        return [Input("input")], \
               [Output("output")], \
               [FloatParameter("height", "Height", 10, min_=0, max_=1000, step=10),
                FloatParameter("radius", "Radius", 2, min_=0, max_=1000, step=10)]

    def process_inputs(self, inputs, outputs, parameters):
        height = parameters["height"]
        radius = parameters["radius"]
        cylinder = BRepPrimAPI_MakeCylinder(radius, height).Shape()

        outputs["output"] = cylinder


register_elements_auto(__name__, locals(), "Basic CAD Shapes", -100)
