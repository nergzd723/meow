// Meow part
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// cpy: analog of cp
// 26.08.19: Initial write
#include <iostream> // for IO management
#include <boost/filesystem.hpp> // for filesystem management
#include <cstring> // for checking of argument
using namespace std;
using namespace boost::filesystem;
int main(int argc, char* argv[]) {
    if(argc == 1) {
        cout << "CPY: simple copy tool" << endl;
        cout << "Usage: cpy [OPTIONS] path_from path_to" << endl;
        cout << "Options:" << endl;
        cout << "-r                         copy 'em recursivily" << endl;
        return 0;
    };
    bool Recursive = false;
    if(!strcmp(argv[1], "-r")) Recursive = true;
    
    path from_to_copy = argv[2];
    path to_copy = argv[3];
    
    bool directory = is_directory(from_to_copy);
    
    if(directory == true && Recursive == false) {
        cout << "cpy: is a directory" << endl;
        return 1;
    } else {
        cout << "cpy: -r key don't needed" << endl;
        return 1;
    };
    if(directory == true && Recursive == true) {
        copy_directory(from_to_copy, to_copy);
        return 0;
    } else {
        copy_file(from_to_copy, to_copy);
        return 0;
    };
    return 0;
}
