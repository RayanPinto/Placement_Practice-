#include<stdio.h>
int binarysearch(int* arr,int left,int right,int key){
if(left<=right){
    int mid=(left+right)/2;
    if(arr[mid]==key){
        return mid;
    }else if(arr[mid]<key){
        return binarysearch(arr,mid+1,right,key);

    }else{
        return binarysearch(arr,left,mid-1,key);

    }

}
return -1;
}
int main(){
    int arr[]={1,2,3,4,5,6};
    int key=6;
    int n=sizeof(arr)/sizeof(arr[0]);
    printf("%d\n",binarysearch(arr,0,n-1,key));
    return 0;
}