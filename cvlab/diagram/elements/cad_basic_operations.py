#!/usr/bin/env python
# coding: utf-8

r"""Basic PythonOCC shapes"""

from .base import *
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.TopTools import TopTools_ListOfShape


class BooleanCut(NormalElement):
    name = "Boolean Cut"
    comment = "A boolean cut operation"

    def get_attributes(self):
        return [Input("shape1"), Input("shape2")], \
               [Output("output")], \
               []

    def process_inputs(self, inputs, outputs, parameters):
        shape1 = inputs["shape1"]
        shape2 = inputs["shape2"]

        cut = BRepAlgoAPI_Cut()
        L1 = TopTools_ListOfShape()
        L1.Append(shape1)
        L2 = TopTools_ListOfShape()
        L2.Append(shape2)
        cut.SetArguments(L1)
        cut.SetTools(L2)
        cut.SetFuzzyValue(5e-5)
        cut.SetRunParallel(False)
        cut.Build()

        outputs["output"] = cut.Shape()


register_elements_auto(__name__, locals(), "CAD Boolean Operations", -99)
