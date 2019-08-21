#include <iostream>
#include <string>

using namespace std;

string checkforvar(const string & key){
    char* val;
    val = getenv(key.c_str());
    string retval = "";
    if (val != NULL){
        retval = val;
    }
    return retval;
}
