#include <iostream>
#include <string>
#include "modulelist.h"

using namespace std;

int checkforvar(string main){
    char doll;
    
    doll << main.at(0);
    
    if (doll = '$'){
        char* env;
        char* v;
        v* << main;
        env* << getenv(v*);
        if (env!=NULL){
            
            cout << env << endl;
            
        }
        return 0;
    }
    return 0;
}
