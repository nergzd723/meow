// Meow part
// Copyright 2019, Oleg Sazonov(@x0r3d)
// Basic Auto Remove toolKit
// 25.08.19: Inital write
// 26.08.19: Moved to Boost library
#include <iostream> // for IO management
#include <cstring> // for strcmp
#include <boost/filesystem.hpp> // for filesystem management
using namespace std;
using namespace boost::filesystem;
int main(int argc, char *argv[]) {
    
    bool Recursive = false; // bool for -r key
    
    if(argc == 1) { // if no arguments, write help
        cout << "Basic Auto Remove toolKit" << endl;
        cout << "Usage: bark [OPTIONS] paths_to_remove" << endl;
        cout << "Options:" << endl;
        cout << "-r                                 detete 'em recursivily" << endl;
        return 0;
    };
    if(!strcmp(argv[1], "-r")) { // check for -r key
    Recursive = true;
    };
    
    if(strcmp(argv[1], "-r")) path need_to_remove = argv[1];
    
path need_to_remove = argv[2]; // main part start, setup path to files
    
    if(is_directory(need_to_remove) == true && Recursive == false) { // checks for key and directory comparation
        cout << "Is a directory(use -r to delete 'em recursivily" << endl;
        return 1;
    } else if(is_directory(need_to_remove) == true && Recursive == true) {
       uintmax_t count = remove_all(need_to_remove);
       if(count == -1) {
           cout << "Failed to remove directory!" << endl;
           return 1;
       } else {
           cout << "Removed " << count << " files and directories!" << endl;
           return 0;
       };
    };
    if(is_directory(need_to_remove) == false) {
        if(strcmp(argv[1], "-r")  && argc > 2) { // check for key, and arguments
        int i;
        for(i = 1;i < argc;i++) { // deleting multiple files
            path removed = argv[i];
            remove(removed);
        }
        cout << "Removed" << i << "files!" << endl; // write how many files has been deleted
        return 0;
        }
        if(!remove(need_to_remove)) {
            cout << "Failed to remove!" << endl;
            return 1;
        } else {
            cout << "Removed!" << endl;
            return 0;
        };
    }; // main part end
   return 0;
};
    
    


