#include <iostream>
#include <string>

using namespace std;

void checkforvar(const string & var){
    const char* val = getenv(var.c_str());
    if (val == 0){
        exit(1);
    }
    cout << *val << endl;
    exit(0);
}
