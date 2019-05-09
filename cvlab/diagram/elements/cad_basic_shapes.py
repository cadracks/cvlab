#!/usr/bin/env python
# coding: utf-8

r"""Basic PythonOCC shapes"""

import logging

from .base import *
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeCylinder

logger = logging.getLogger(__name__)


class Cube(NormalElement):
    name = "Cube"
    comment = "A simple cube"

    def get_attributes(self):
        logger.debug("Call to Cube.get_attributes()")
        return [], \
               [Output("output")], \
               [FloatParameter("size", "Size", 10, min_=0, max_=1000, step=10), ]

    def process_inputs(self, inputs, outputs, parameters):
        logger.debug("Call to Cube.process_inputs()")
        size = parameters["size"]
        cube = BRepPrimAPI_MakeBox(size, size, size).Shape()

        outputs["output"] = Data(cube)


class Cylinder(NormalElement):
    name = "Cylinder"
    comment = "A simple cylinder"

    def get_attributes(self):
        logger.debug("Call to Cylinder.get_attributes()")
        return [], \
               [Output("output")], \
               [FloatParameter("height", "Height", 10, min_=0, max_=1000, step=10),
                FloatParameter("radius", "Radius", 2, min_=0, max_=1000, step=10)]

    def process_inputs(self, inputs, outputs, parameters):
        logger.debug("Call to Cylinder.process_inputs()")
        height = parameters["height"]
        radius = parameters["radius"]
        cylinder = BRepPrimAPI_MakeCylinder(radius, height).Shape()

        outputs["output"] = Data(cylinder)


register_elements_auto(__name__, locals(), "Basic CAD Shapes", -100)
