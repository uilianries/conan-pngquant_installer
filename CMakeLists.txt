cmake_minimum_required(VERSION 2.8)

project(pngquant C)

option(BUILD_WITH_SSE "Use SSE" ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

if(BUILD_WITH_SSE)
  add_definitions(-DUSE_SSE=1)
endif()

if(BUILD_SHARED_LIBS AND MSVC)
  add_definitions(-DIMAGEQUANT_EXPORTS)
endif()
#find_package(OpenMP)
#if(OPENMP_FOUND)
#  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
#  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
#endif()

#find_package(PNG REQUIRED)
#include_directories(${PNG_INCLUDE_DIRS})
#include_directories(${PROJECT_SOURCE_DIR} "${PROJECT_SOURCE_DIR}/lib")

if(CMAKE_COMPILER_IS_GNUCC)
  add_compile_options("-std=c99")
endif()
if(MSVC)
    add_definitions( /wd4244 /wd4267 /wd4305)
endif()
add_library(imagequant
  lib/libimagequant.c
  lib/blur.c
  lib/mediancut.c
  lib/mempool.c
  lib/nearest.c
  lib/pam.c
  lib/viter.c
)

#add_executable(pngquant pngquant.c rwpng.c)
#target_link_libraries(pngquant ${PNG_LIBRARIES} imagequant)
