project(meowproj)
cmake_minimum_required(VERSION 2.8)

set(MAKE "make")
set(EXEC "-C")
set(bark "bark")
set(cpy "cpy")
set(dip "dip")
set(dutils "dutils")
set(exo "exo")
set(lt "lt")
set(meow "meow")
set(mkdip "mkdip")
set(no "no")
set(tap "tap")
set(yedd "yedd")
set(aname "aname")
set(kid "kid")
set(patrat "patrat")
set(pyma "pyma")

if(UNIX AND NOT APPLE)
    set(LINUX TRUE)
endif()

if(NOT LINUX)
    message(FATAL_ERROR "You are trying to build on Windows or on macOS. It is not supported yet. Use WSL on Windows.")
endif()
execute_process(COMMAND ${MAKE} ${EXEC} ${bark}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${cpy}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${dip}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${dutils}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${exo}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${lt}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${meow}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${mkdip}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${no}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${tap}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${yedd}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${aname}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${kid}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${patrat}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
execute_process(COMMAND ${MAKE} ${EXEC} ${pyma}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
message(STATUS "cmake test build succeeded")
