PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(example example.c)
TARGET_LINK_LIBRARIES(example ${CONAN_LIBS})
set_target_properties(example PROPERTIES C_STANDARD 99)
