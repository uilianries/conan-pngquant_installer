cmake_minimum_required(VERSION 2.8)
project(pngquant C)

option(BUILD_WITH_SSE "Use SSE" ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(imagequant
  source_subfolder/lib/libimagequant.c
  source_subfolder/lib/blur.c
  source_subfolder/lib/mediancut.c
  source_subfolder/lib/mempool.c
  source_subfolder/lib/nearest.c
  source_subfolder/lib/pam.c
  source_subfolder/lib/viter.c
)

if(BUILD_WITH_SSE)
  target_compile_definitions(imagequant PUBLIC USE_SSE=1)
endif()

set_target_properties(imagequant PROPERTIES C_STANDARD 99)

if(MSVC)
    target_compile_definitions(imagequant PRIVATE /wd4244 /wd4267 /wd4305 /wd4244)
    if(BUILD_SHARED_LIBS)
        target_compile_definitions(imagequant PUBLIC IMAGEQUANT_EXPORTS=1)
    endif()
endif()

export(TARGETS imagequant
       NAMESPACE ${CMAKE_PROJECT_NAME}::
       FILE "${CMAKE_CURRENT_BINARY_DIR}/${CMAKE_PROJECT_NAME}-config.cmake")

install(TARGETS imagequant
        EXPORT ${CMAKE_PROJECT_NAME}-config
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(DIRECTORY source_subfolder/lib/
        DESTINATION include
        FILES_MATCHING PATTERN "*.h")

install(EXPORT ${CMAKE_PROJECT_NAME}-config
        DESTINATION "${CMAKE_INSTALL_LIBDIR}/${CMAKE_PROJECT_NAME}/cmake"
        NAMESPACE ${CMAKE_PROJECT_NAME}::)