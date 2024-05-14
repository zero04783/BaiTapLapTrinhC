
#include <stdio.h>

void xuatBoiCua7Co2ChuSo(){
    for(int i = 0; i< 100; i++){
        if(i%7 == 0)
            printf("%d ", i);
    }
}
int main()
{
    printf("Chuong Trinh xuat cac so nguyen co 2 chu so va la boi cua 7\n");
    xuatBoiCua7Co2ChuSo();
    return 0;
}
