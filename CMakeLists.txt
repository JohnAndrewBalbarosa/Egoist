cmake_minimum_required(VERSION 3.16)
project(EgoistCppWorkspace LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Put every built executable into a single folder at the repo root.
set(PROJECT_BIN_DIR "${CMAKE_SOURCE_DIR}/project")
file(MAKE_DIRECTORY "${PROJECT_BIN_DIR}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BIN_DIR}")

# Optional warnings for common compilers.
if(MSVC)
    add_compile_options(/W4 /permissive-)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Discover all C++ source files in the workspace.
file(GLOB_RECURSE ALL_CPP_SOURCES CONFIGURE_DEPENDS
    "${CMAKE_SOURCE_DIR}/*.cpp"
    "${CMAKE_SOURCE_DIR}/*.cc"
    "${CMAKE_SOURCE_DIR}/*.cxx"
)

set(ADDED_TARGET_COUNT 0)

foreach(SRC_FILE IN LISTS ALL_CPP_SOURCES)
    string(REPLACE "\\" "/" SRC_FILE_NORMALIZED "${SRC_FILE}")

    # Skip build and output folders if they exist.
    if(SRC_FILE_NORMALIZED MATCHES "/build/" OR
       SRC_FILE_NORMALIZED MATCHES "/cmake-build-" OR
       SRC_FILE_NORMALIZED MATCHES "/project/" OR
       SRC_FILE_NORMALIZED MATCHES "/webDevelopment/react-todo-app/")
        continue()
    endif()

    get_filename_component(SRC_DIR "${SRC_FILE}" DIRECTORY)
    file(RELATIVE_PATH REL_DIR "${CMAKE_SOURCE_DIR}" "${SRC_DIR}")

    if(REL_DIR STREQUAL ".")
        set(REL_DIR "root")
    endif()

    get_filename_component(FILE_STEM "${SRC_FILE}" NAME_WE)

    # Build a stable, unique target name from folder + filename.
    set(TARGET_NAME "${REL_DIR}__${FILE_STEM}")
    string(REPLACE "/" "_" TARGET_NAME "${TARGET_NAME}")
    string(REPLACE " " "_" TARGET_NAME "${TARGET_NAME}")
    string(REPLACE "+" "p" TARGET_NAME "${TARGET_NAME}")
    string(REGEX REPLACE "[^A-Za-z0-9_]" "_" TARGET_NAME "${TARGET_NAME}")

    add_executable("${TARGET_NAME}" "${SRC_FILE}")
    set_target_properties("${TARGET_NAME}" PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BIN_DIR}"
    )

    math(EXPR ADDED_TARGET_COUNT "${ADDED_TARGET_COUNT} + 1")
endforeach()

message(STATUS "Configured ${ADDED_TARGET_COUNT} C++ executable target(s).")
