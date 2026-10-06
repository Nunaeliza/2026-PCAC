/*
Problema 1113 beecrowd
Data: 2026.10.06
Autor: Luana Eliza dos Santos
*/
#include <stdio.h>

int main() {
    int x, y;

    scanf("%d %d", &x, &y);

    while (x != y) {
        if (x < y) {
            printf("Crescente\n");
        } else {
            printf("Decrescente\n");
        }
        scanf("%d %d", &x, &y);
    }
    return 0;
}