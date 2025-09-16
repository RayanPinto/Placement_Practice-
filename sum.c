#include<stdio.h>
int rayan(int n){
    if(n<=0){
        return 0;
    }
    return rayan(n-1)+n;
}
int main(){
    int n=5;
    printf("%d\n",rayan(n));
    return 0;
}