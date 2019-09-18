#include <iostream>

using namespace std;

int main(void) {
    struct hello {
        string m = "Hello World";
        string out = m;
    };
    class h {
        public:
        struct hello fuck;
        h(void) {
        };
        void print(void) {
            cout << fuck.out << endl;
        }
    };

    class e {
        public:
        e(void) {
            class h;
        };
    };

    class l {
        public:
        l(void) {
            class e;
        };
    };
    class o {
        public:
        o(void) {
            class l;
        };
    };

    class o;
    o.print();
    return 0;
}