// Meow part
// Copyrtight 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// YaDD: Yet another DD
// 28.08.19: Initial write
#include <stdio.h> // for fopen,fread,fwrite
#include <iostream> // for IO management
using namespace std;

int main(int argc, char *argv[]) {
    if(argc == 1) {
        cout << "YaDD: Yet another DD" << endl;
        cout << "Usage: yadd path_from path_to size_of_transaction(in bytes, by default 4K) count_of_blocks" << endl;
        return 0;
    };

    int bufsize, count;

    if(isdigit(atoi(argv[3]))) {
      bufsize = atoi(argv[3]);
    } else {
      bufsize = 4096;
    }

    if(isdigit(atoi(argv[4]))) {
      count = atoi(argv[4]);
    } else {
      count = 1;
    }

    char buf[bufsize];

    try {
      FILE* read = fopen64(argv[1],"r");
      if(!read) {
        cerr << "read: failed to open by fopen64(), try fopen()";
        throw 1;
      }
    }
      catch(int a) {
        FILE* read = fopen(argv[1], "r");
        if(!read) {
          cerr << "read: FAILED to open by fopen(), closing...";
          return 1;
        }
      };

      try {
        FILE* write = fopen64(argv[2], "w");
        if(!write) {
          cerr << "write: failed to open by fopen64(), try fopen()";
          throw 1;
        }
      }
      catch(int a) {
        FILE* write = fopen(argv[2], "w");
        if(!write) {
          cerr << "write: FAILED to open by fopen64(), closing...";
          return 1;
        }
      };

int i;

while(!feof(read) || count < i) {
  fread(buf, bufsize, 1, read);
  fwrite(buf, bufsize, 1, write);
  ++i;
}
    return 0;
}
