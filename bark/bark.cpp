// Meow part
// Copyright 2019, Oleg Sazonov(@x0r3d)
// Basic Auto Remove toolKit
// 25.08.19: Inital write
// 26.08.19: Moved to Boost library
// 20.09.19: Fix for one file
// 8.11.19: Fully rewrite it to memory logic
#include "../external_projects/argh/argh.h" // argument handler
#include <boost/filesystem.hpp>             // for filesystem management
#include <cstring>                          // for strcmp
#include <iostream>                         // for IO management
#include <memory>                           // for memory management
using namespace std;
using namespace boost::filesystem;
int main(int argc, char *argv[]) {
  argh::parser cmdl(argv);
  bool Recursive = false; // bool for -r key
  if (cmdl({"-r", "--recursive"})) {
    Recursive = true;
  }
  if (argc == 1) { // if no arguments, write help
    cout << "Basic Auto Remove toolKit" << endl;
    cout << "Usage: bark [OPTIONS] paths_to_remove" << endl;
    cout << "Options:" << endl;
    cout << "-r, --recursive                                 detete 'em "
            "recursivily"
         << endl;
    return 0;
  };

  path need_to_remove;
  if (!Recursive) {
    need_to_remove = argv[1];
  } else {
    need_to_remove = argv[2];
  }

  if (is_directory(need_to_remove) == true &&
      Recursive == false) { // checks for key and directory comparation
    cout << "Is a directory(use -r to delete 'em recursivily" << endl;
    return 1;
  } else if (is_directory(need_to_remove) == true && Recursive == true) {
    uintmax_t count = remove_all(need_to_remove);
    if (count == -1) {
      cout << "Failed to remove directory!" << endl;
      return 1;
    } else {
      cout << "Removed " << count << " files and directories!" << endl;
      return 0;
    };
  };
  if (is_directory(need_to_remove) == false) {
    if (Recursive == true && argc > 2) { // check for key, and arguments
      int *i = new int;
      for (int i = 1; i < argc; i++) { // deleting multiple files
        path removed = argv[i];
        remove(removed);
      }
      cout << "Removed" << i << "files!"
           << endl; // write how many files has been deleted
      delete i;
      return 0;
    }
    if (!remove(need_to_remove)) {
      cout << "Failed to remove!" << endl;
      return 1;
    } else {
      cout << "Removed!" << endl;
      return 0;
    };
  }; // main part end
  return 0;
};
