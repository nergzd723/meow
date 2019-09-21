#include <iostream>
#include "lib/api.h"

using namespace std;

int main(int argc, char *argv[]) {
    if (argc == 1 || argc > 4) {
        cout << "Liker: VK Photo Liker" << endl;
        cout << "Usage: liker login pass album" << endl;
        return 0;
    }

    string login,pass;
    login = argv[1];
    pass = argv[2];

    VK::Client client;
    if(client.auth(login, pass)) {
        cout << "auth ok!" << endl;
        cout << "Access token: " << client.access_token() << endl;
    }
    return 0;
}