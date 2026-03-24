#include <stdio.h>
int main(){

    int n1, n2, n3;
    float media;

    printf("Digite as 3 notas: ");
    scanf("%d %d %d", &n1, &n2, &n3);
    media = (n1 + n2 + n3) / 3;
    printf("A média eh: %f", media);
    if(media < 7){
        printf("Exame\n");
    }
    else{
        printf("Passou\n");
    }
    return 0;
}