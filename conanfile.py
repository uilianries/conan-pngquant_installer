#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, CMake, tools
import os


class PNGQuantConan(ConanFile):
    name = "pngquant"
    version = "2.6.0"
    license = "GPL-3.0", "Commercial"
    url = "https://github.com/conan-community/conan-pngquant"
    homepage = "https://github.com/pornel/pngquant"
    description = "Lossy PNG compressor"
    topics = ("conan", "pngquant", "png", "compressor")
    author = "Conan Community"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "fPIC": [True, False],
               "sse": [True, False]}
    default_options = {"shared": False, "sse": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "CMakeLists.txt"
    exports = "LICENSE"
    requires = "libpng/1.6.36@bincrafters/stable"
    _source_subfolder = "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        sha256 = "ea897936c418c15329914d0dbbbce0a764f808e9f161b3103acf23eb71022e09"
        tools.get("{}/archive/{}.tar.gz".format(self.homepage, self.version), sha256=sha256)
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_WITH_SSE"] = self.options.sse
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("COPYRIGHT", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
