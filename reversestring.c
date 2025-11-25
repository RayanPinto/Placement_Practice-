#include<stdio.h>
#include<string.h>
int main(){
    char arr[]="abcabc";
    int n=strlen(arr);
    int st=0;
    int end=n-1;
    char temp;
    while(st<end){
    arr[st]^=arr[end];
    arr[end]^=arr[st];
    arr[st]^=arr[end];
st++;
end--;
    }
    printf("%s",arr);
    return 0;
}