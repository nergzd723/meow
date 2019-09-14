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
        cout << "Usage: yadd path_from path_to size_of_transaction(in bytes, 4K) count_of_blocks" << endl;
        return 0;
    };
    int bufnsize;
    if(isdigit(atoi(argv[3]))) {
      bufnsize = atoi(argv[3]);
    } else {
      bufnsize = 4096;
    }

    if(isdigit(atoi(argv[4]))) {
      const int count = atoi(argv[4]);
    } else {
      const int count = 1;
    }
    const int bufsize = bufnsize;
    char buf[bufsize]; // buffer for readed data

    try {
        FILE *read = fopen64(argv[1], "r");
        if(!read) {
            cerr << "read: Failed to open with fopen64, try fopen()" << endl;
            throw 1;
        };
    } catch(int a) {
        FILE *read = fopen(argv[1], "r");
        if(!read) cerr << "read: Failed to open file!" << endl;
        return 0;
    };

    try {
        FILE *write = fopen64(argv[2], "w");
        if(!write) {
            cerr << "write: Failed to open with fopen64, try fopen()" << endl;
            throw 1;
        };
    } catch(int b) {
        FILE *write = fopen(argv[2], "w");
        if(!write) {
            cerr << "write: Failed to open!" << endl;
            return 0;
        };
    };
 int i;
while(!feof(read) || count < i) {
  fread(buf, bufsize, 1, read);
  fwrite(buf, bufsize, 1, write);
  ++i;
}


    return 0;
}
