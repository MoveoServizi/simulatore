# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/Desktop/simulatore/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/Desktop/simulatore/build

# Utility rule file for simulator_gencpp.

# Include the progress variables for this target.
include simulator/CMakeFiles/simulator_gencpp.dir/progress.make

simulator_gencpp: simulator/CMakeFiles/simulator_gencpp.dir/build.make

.PHONY : simulator_gencpp

# Rule to build all files generated by this target.
simulator/CMakeFiles/simulator_gencpp.dir/build: simulator_gencpp

.PHONY : simulator/CMakeFiles/simulator_gencpp.dir/build

simulator/CMakeFiles/simulator_gencpp.dir/clean:
	cd /home/ubuntu/Desktop/simulatore/build/simulator && $(CMAKE_COMMAND) -P CMakeFiles/simulator_gencpp.dir/cmake_clean.cmake
.PHONY : simulator/CMakeFiles/simulator_gencpp.dir/clean

simulator/CMakeFiles/simulator_gencpp.dir/depend:
	cd /home/ubuntu/Desktop/simulatore/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/Desktop/simulatore/src /home/ubuntu/Desktop/simulatore/src/simulator /home/ubuntu/Desktop/simulatore/build /home/ubuntu/Desktop/simulatore/build/simulator /home/ubuntu/Desktop/simulatore/build/simulator/CMakeFiles/simulator_gencpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : simulator/CMakeFiles/simulator_gencpp.dir/depend

