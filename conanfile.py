#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, CMake, tools
import os


class PNGQuantConan(ConanFile):
    name = "pngquant"
    version = "2.12.2"
    license = "GPL-3.0", "Commercial"
    url = "https://github.com/conan-community/conan-pngquant"
    homepage = "https://github.com/pornel/pngquant"
    description = "Lossy PNG compressor"
    topics = ("conan", "pngquant", "png", "compressor")
    author = "Conan Community"
    settings = "os_build", "arch_build", "compiler"
    options = {"sse": [True, False]}
    default_options = {"sse": True}
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    exports = "LICENSE"
    requires = (
        "libimagequant/2.12.2@conan/stable",
        "zlib/1.2.11@conan/stable",
        "libpng/1.6.36@bincrafters/stable",
        "lcms/2.9@bincrafters/stable"
    )
    _source_subfolder = "source_subfolder"

    def config_options(self):
        self.options["libimagequant"].sse = self.options.sse

    def source(self):
        sha256 = "5edf7c5bffd07e5d28fcc6d4d94a187c30b532c52ac986b3e45aff3dce0567dc"
        tools.get("{}/archive/{}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["USE_SSE"] = self.options.sse
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("COPYRIGHT", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        del self.info.settings.compiler

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))