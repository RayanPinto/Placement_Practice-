#include<stdio.h>
int main(){
    int arr[]={1,5,3,2,2};
    int n=sizeof(arr)/sizeof(arr[0]);
int lar=arr[0];
int small=arr[0];
for(int i=0;i<n;i++){
    if(arr[i]>lar){
        lar=arr[i];
    }
    if (arr[i]<small){
        small=arr[i];
    }
}
int secondlar=arr[0];
for(int i=0;i<n;i++){
    if(arr[i]<lar && arr[i]>secondlar){
        secondlar=arr[i];
    }
}
printf("%d\t%d\t%d",lar,small,secondlar);

return 0;

}