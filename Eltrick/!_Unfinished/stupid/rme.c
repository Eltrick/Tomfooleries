#include <stdio.h>

int main() {
    int a = 0;
    while (a%49!=14||a%46!=41||a%36!=13||a%43!=37||a%22!=9||a%45!=13)a++;
    printf("%d",a);
    return 0;
}