// Meow part
// KID : Kills by ID
// Copyright 2019, Oleg Sazonov(@x0r3d) in collaboration with Mark Hargreaves(@nergzd723)
// 24.09.19: Initial write
#include <iostream>
#include <signal.h>
#include <unistd.h>
#include <cctype>
using namespace std;
int get_external_process_id( std::string name )
{
std::string output = "pidof ";
output += name; 
char line[ 15 ];
FILE *cmd = popen( output.c_str( ), "r");
fgets( line, 15, cmd );
pid_t pid = strtoul( line, NULL, 10 );
pclose(cmd);
return( pid );
};
int main(int argc, char *argv[]) {
    if(argc == 1) {
        cout << "KID: Kills by ID" << endl;
        cout << "Usage: kid name_of_process[pid]" << endl;
        return 0;
    };
    string kid = argv[1];
    pid_t pid;
    if(isdigit(atoi(kid.c_str())) && !kid.empty()) {
        pid = atoi(kid.c_str());
    } else if(!kid.empty()) {
        pid = get_external_process_id(kid);
    };
    int ret = kill(pid, SIGKILL);
    if(ret == 0) {
        cout << "It's don't killed!" << endl;
    } else {
        cout << "It's killed!" << endl;
    };
    return 0;
};