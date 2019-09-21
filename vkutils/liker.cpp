#include <iostream>
#include "lib/api.h"
#include "lib/json.hpp"

using namespace std;
using  json = nlohmann::json;

int main(int argc, char *argv[]) {
    if (argc == 1 || argc > 4) {
        cout << "Liker: VK Photo Liker" << endl;
        cout << "Usage: liker login pass album_owner_id album_id" << endl;
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

    VK::params_map test = {
    {"owner_id", "223134400"},
    {"album_id", "saved"},
    {"count", "2"}
    };
   json parse = client.call("photos.get", test);
   auto count = parse["response"]["count"].get<int>();
   cout << count << endl;
    return 0;
}