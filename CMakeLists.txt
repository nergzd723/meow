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
set(PYPY "python3")
set(PYMO "-m")
set(NUITKA "nuitka")

if(UNIX)
    set(UNIX TRUE)
endif()

if(NOT UNIX)
    message(FATAL_ERROR "You are trying to build on Windows. It is not supported. Use WSL.")
endif()

add_custom_target(bark COMMAND ${MAKE} ${EXEC} ${bark}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(cpy COMMAND ${MAKE} ${EXEC} ${cpy}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(dip COMMAND ${MAKE} ${EXEC} ${dip}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(dutils COMMAND ${MAKE} ${EXEC} ${dutils}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(exo COMMAND ${MAKE} ${EXEC} ${exo}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(lt COMMAND ${MAKE} ${EXEC} ${lt}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(meow COMMAND ${MAKE} ${EXEC} ${meow}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(mkdip COMMAND ${MAKE} ${EXEC} ${mkdip}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(no COMMAND ${MAKE} ${EXEC} ${no}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(tap COMMAND ${MAKE} ${EXEC} ${tap}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(yedd COMMAND ${MAKE} ${EXEC} ${yedd}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(aname COMMAND ${MAKE} ${EXEC} ${aname}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(kid COMMAND ${MAKE} ${EXEC} ${kid}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(patrat COMMAND ${MAKE} ${EXEC} ${patrat}
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR})
add_custom_target(all ALL 
    DEPENDS bark cpy dip dutils exo lt meow mkdip no tap yedd kid patrat aname)
message(STATUS "cmake test build succeeded")