#include <stdio.h>

int main()
{
    FILE* fileptr;
    char buf;
    long filelen;
    fileptr = fopen("mem", "rb");
    fseek(fileptr, 0, SEEK_END);
    filelen = ftell(fileptr);
    rewind(fileptr);
    for(int i = 0; i<filelen; i++){
        fread(buf, 1, 1, fileptr);
        printf("%c", buf);
    }
}
