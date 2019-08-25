#include <iostream>
#include <cstring>
#include <experimental/filesystem>
using namespace std;
using namespace std::experimental::filesystem;
int main(int argc, char *argv[]) {
    
    bool Recursive = false;
    
    if(argc == 1) {
        cout << "Basic Auto Remove toolKit" << endl;
        cout << "Usage: bark [OPTIONS] path_to_remove" << endl;
        cout << "Options:" << endl;
        cout << "-r                                 detete 'em recursivily" << endl;
        return 0;
    };
    if(!strcmp(argv[1], "-r")) {
    Recursive = true;
    };
    
   path need_to_remove = argv[2];
    
    if(is_directory(need_to_remove) == true && Recursive == false) {
        cout << "Is a directory(use -r to delete 'em recursivily" << endl;
        return 1;
    } else if(is_directory(need_to_remove) == true && Recursive == true) {
        if(remove_all(need_to_remove) == -1) {
            cout << "Failed to remove!" << endl;
            return 1;
        } else {
            cout << "Removed!" << endl;
            return 0;
        };
    };
    if(is_directory(need_to_remove) == false) {
        if(argc >= 3) {
            cout << "I'm deleting only single file, but not multiple files!" << endl;
            return 1;
        }
        if(!remove(need_to_remove)) {
            cout << "Failed to remove!" << endl;
            return 1;
        } else {
            cout << "Removed!" << endl;
            return 0;
        };
    };
   return 0;
}
    
    


