#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cpt.packager import ConanMultiPackager
import os
import platform

def get_os():
    return platform.system().replace("Darwin", "Macos")

if __name__ == "__main__":

    arch = os.environ["ARCH"]
    builder = ConanMultiPackager()
    builder.add({"os" : get_os(), "arch_build" : arch, "arch": arch}, {}, {}, {})
    builder.run()
