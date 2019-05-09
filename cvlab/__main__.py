#!/usr/bin/env python3
# coding: utf-8

r"""cvlab launching"""

import logging
import sys
import os.path
from cvlab import main  # main() is defined in __init__.py

if __package__ is None and not hasattr(sys, 'frozen'):
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s :: %(levelname)6s :: %(module)20s '
                               ':: %(lineno)3d :: %(message)s')
    main()
