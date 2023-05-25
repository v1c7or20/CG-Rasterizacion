cmake_minimum_required(VERSION 3.24)
project(CG_Rasterizacion)

set(CMAKE_CXX_STANDARD 17)

include_directories(${GLFW_INCLUDE_DIR})
link_libraries(${GLFW_LIBRARY})

add_executable(CG_Rasterizacion main.cpp ./include/glad.c include/stb_image.cpp include/Camara.h)

target_link_libraries(CG_Rasterizacion -lOpenGL32 -lGLU32 -lglfw3)
