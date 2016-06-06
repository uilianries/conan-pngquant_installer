from conans import ConanFile, CMake, tools
import os, shutil


class pngquantConan(ConanFile):
    name = "pngquant"
    version = "2.6.0"
    license = "Dual GPL v3 + Commercial"
    url = "https://github.com/memsharded/conan-pngquant"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "sse": [True, False]}
    default_options = "shared=False", "sse=False"
    generators = "cmake"
    exports = "CMakeLists.txt"
    requires =  "libpng/1.6.21@lasote/stable"

    def config(self):
        del self.settings.compiler.libcxx

    def source(self):
       self.run("git clone https://github.com/pornel/pngquant.git")
       self.run("cd pngquant && git checkout msvc")
       shutil.copy("CMakeLists.txt", "pngquant")
       #tools.download("https://github.com/pornel/pngquant/archive/%s.zip" % self.version, "pngquant.zip")
       #tools.unzip("pngquant.zip")
       #shutil.copy("CMakeLists.txt", "pngquant-%s/" % self.version)

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        sse = "-DBUILD_WITH_SSE=ON" if self.options.sse else ""
        self.run('cmake pngquant %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*libimagequant.h", dst="include", src="pngquant/lib")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["imagequant"]
