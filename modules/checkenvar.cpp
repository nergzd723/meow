#include <iostream>
#include <string>
#include "modulelist.h"
using namespace std;
int checkforvar(string main){
    char doll;
    doll << main.at(0);
    if (doll = '$'){
        char* env;
        env << getenv(main);
        if (env!=NULL){
            cout << env << endl;
        }
        return 0;
    }
    return 0;
}
