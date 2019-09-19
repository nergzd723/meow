#include <iostream>
using namespace std;int main(void) {struct hello {string m = "Hello World";string out = m; };class h {public: int i = 0;struct hello fuck;h(void) {};void print(void) {cout << fuck.out << endl;}};class e : public h {public: e(void) {i++;};};class l : public e {public: l(void) {i++;};};class o : public l {public: o(void) {i++;};};o hell;hell.print();return 0;
}