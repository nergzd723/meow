#include <iostream>
#include <string>

using namespace std;

string checkforvar(const string & key){
    string readwrite;
    readwrite = key;
    if(readwrite.find('$') == 1) readwrite.erase(1, 1);
    cout << readwrite << endl;
    char* val;
    val = getenv(key.c_str());
    string retval = "";
    if (val != NULL) retval = val;
    return retval;
}
