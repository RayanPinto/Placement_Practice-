#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int num,rev;
    while(n!=0){
        num=n%10;
        rev=rev*10+num;
        n=n/10;
    }
    printf("%d\t",rev);

    return 0;

}