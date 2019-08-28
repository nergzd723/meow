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
        cout << "Usage: yadd path_from path_to size_of_transaction(K,M,G)" << endl;
        return 0;
    };
    
    char buf[1024]; // buffer for readed data
    
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
        
    
    return 0;
}
