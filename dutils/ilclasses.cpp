#include <iostream>

using namespace std;

int main(void) {
    struct hello {
        string m = "Hello World";
        string out = m;
    };
    class Hello {
        public:
        Hello(void) {
            struct hello fuck;
            cout << fuck.m << endl;
        };
    };
    Hello a;
    return 0;
}