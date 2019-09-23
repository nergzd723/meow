#include <iostream>
#include <string>
#include "lib/api.h"
#include "lib/json.hpp"

using namespace std;
using  json = nlohmann::json;

void liker_main(int id, const string access_token) {
    VK::params_map liker_main = {
        {"type", "photo"},
        {"item_id", to_string(id)}
    };
    VK::Client l;
    if(l.auth(nullptr,nullptr,access_token)) {
        cout << "liker auth ok" << endl;
    };
    l.call("likes.add", liker_main);
};

int main(int argc, char *argv[]) {
    if (argc == 1 || argc > 4) {
        cout << "Liker: VK Photo Liker" << endl;
        cout << "Usage: liker login pass album_owner_id" << endl;
        return 0;
    }

    string login,pass;
    int owner_id;
    login = argv[1];
    pass = argv[2];

    VK::Client client;
    if(client.auth(login, pass)) {
        cout << "auth ok!" << endl;
    }
    const string access_token = client.access_token();

   VK::params_map second_try = {
       {"owner_id", to_string(owner_id)},
       {"album_id", "saved"},
       {"count", to_string(500)}
   };
  
   json second = client.call("photos.get", second_try);
   for (const auto& item : second["response"]["items"])
   {
       int id = item["id"];
       cout << id << endl;
        liker_main(id, access_token);
   }
   
    return 0;
};