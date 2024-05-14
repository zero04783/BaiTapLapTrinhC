#include <stdio.h>
#include <math.h>

int kiemTraSCP(int n){
    
    int flag = 0;
    int i = 0;
    while(i <= n){
        if( pow( i, 2) == n ) {   
            flag = 1;
            break;
        }
        i++;
    }

    return flag;
}
int demSCPNhoHonN(int n){
    int count = 0;
    for(int i = 0; i < n; i++){
        if(kiemTraSCP(i) == 1){
            count++;
        }
    }
    return count;
}
void inSCPNhoHonN(int n){
    for(int i = 0; i < n; i++){
        if(kiemTraSCP(i) == 1){
            printf("%d ", i);
        }
    }
}
int main(){
    int n;
    do{
        printf(">> nhap mot so nguyen duong: ");
        scanf("%d",&n);
    }while(n <= 0);

    
    printf("\nCo %d so chinh phuong nho hon n: ", demSCPNhoHonN(n));
    inSCPNhoHonN(n);

    return 0;
}