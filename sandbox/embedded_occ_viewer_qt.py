# coding: utf-8

from PyQt5 import QtWidgets

from OCC.Display.backend import load_backend
load_backend('qt-pyqt5')
from OCC.Display.qtDisplay import qtViewer3d

from aocutils.display.color import color


class Qt3dViewer(QtWidgets.QWidget):
    def __init__(self,
                 parent,
                 viewer_background_color=(100., 100., 100., 250., 250., 250.)):
        QtWidgets.QWidget.__init__(self, parent)

        self.viewer = qtViewer3d(self)
        self.viewer.InitDriver()

        self.background_color = viewer_background_color
        r1, g1, b1, r2, g2, b2 = viewer_background_color
        self.viewer_display.set_bg_gradient_color(r1, g1, b1, r2, g2, b2)

        vbox = QtWidgets.QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)

        # vbox.addLayout(hbox)
        vbox.addWidget(self.viewer)
        self.setLayout(vbox)
        self.show()

        self._shapes = list()

    @property
    def viewer_display(self):
        r"""Viewer3d getter
        Returns
        -------
        OCC.Display.OCCViewer.Viewer3d
        """
        return self.viewer._display

    def display_shape(self,
                      shapes,
                      material=None,
                      texture=None,
                      color=None,
                      transparency=None,
                      update=False):
        r"""DisplayShape and keep track of displayed shapes
        Parameters
        ----------
        shapes : list of OCC Shapes or single OCC Shape
        material
        texture
        color
        transparency : float between 0 and 1
        update : bool
        """
        self.viewer_display.DisplayShape(shapes,
                                         material=material,
                                         texture=texture,
                                         color=color,
                                         transparency=transparency,
                                         update=update)
        if isinstance(shapes, list):
            for shape in shapes:
                self._shapes.append(shape)
        else:
            self._shapes.append(shapes)


def colour_qt_to_occ(qt_colour):
    r"""Convert a qt colour coded on ints from 0 to 255 to an OCC color coded
    on floats from 0 to 1
    Parameters
    ----------
    qt_colour : tuple of 3 ints
    """
    r, g, b = qt_colour  # 255
    return color(r / 255., g / 255., b / 255.)  # 1


if __name__ == '__main__':
    import aocutils.primitives

    box = aocutils.primitives.box(100, 50, 25)

    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()

    widget = Qt3dViewer(window)
    # window.setWindowTitle('Simple')
    window.setCentralWidget(widget)
    widget.display_shape(box)
    widget.viewer_display.FitAll()
    window.show()
    window.resize(400, 300)
    app.exec_()
