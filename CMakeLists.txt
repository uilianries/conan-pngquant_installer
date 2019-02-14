cmake_minimum_required(VERSION 2.8.11)
project(pngquant C)

set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

option(USE_SSE "Activate SSE feature for x86" OFF)

set(SOURCE_FILES    source_subfolder/pngquant_opts.c
                    source_subfolder/pngquant.c
                    source_subfolder/rwpng.c)

set(HEADER_FILES    source_subfolder/rwpng.h
                    source_subfolder/pngquant_opts.h)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES} ${HEADER_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})

target_compile_definitions(${CMAKE_PROJECT_NAME} PUBLIC USE_LCMS=1)
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES C_STANDARD 99)

if (USE_SSE)
    target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE USE_SSE=1)
    if ((CMAKE_C_COMPILER_ID MATCHES "(Clang)|(GNU)") AND
        (CMAKE_SYSTEM_PROCESSOR MATCHES "(x86)|(X86)|(amd64)|(AMD64)"))
        target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -fno-math-errno -funroll-loops -fomit-frame-pointer -msse -mfpmath=sse -fexcess-precision=fast)
    endif()
endif()

install(TARGETS ${CMAKE_PROJECT_NAME}
        RUNTIME DESTINATION bin)
