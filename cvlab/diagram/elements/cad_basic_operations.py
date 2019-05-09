#!/usr/bin/env python
# coding: utf-8

r"""Basic PythonOCC shapes"""

import logging

from .base import *
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.TopTools import TopTools_ListOfShape

logger = logging.getLogger(__name__)


class BooleanCut(NormalElement):
    name = "Boolean Cut"
    comment = "A boolean cut operation"

    def get_attributes(self):
        logger.debug("Call to BooleanCut.get_attributes()")
        return [Input("shape1"), Input("shape2")], \
               [Output("output")], \
               []

    def process_inputs(self, inputs, outputs, parameters):
        logger.debug("Call to BooleanCut.process_inputs()")
        shape1 = inputs["shape1"].value
        shape2 = inputs["shape2"].value

        logger.debug("shape1 is %s" % str(shape1))
        logger.debug("shape2 is %s" % str(shape2))

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

        outputs["output"] = Data(cut.Shape())


register_elements_auto(__name__, locals(), "CAD Boolean Operations", -99)
