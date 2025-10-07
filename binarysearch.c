#include<stdio.h>
int binarysearch(int *arr,int left,int right,int key){
    if(left<=right){
        int mid=(left+right)/2;
        if(arr[mid]==key){
            return mid;
        }
        else if(arr[mid]<key){
            return binarysearch(arr,mid+1,right,key);
        }
        else{
            return binarysearch(arr,left,mid-1,key);
        }
    }
    return -1;
}
int main(){ 
    int arr[]={1,3,4,5,6,6,9,10};
    int n=sizeof(arr)/sizeof(arr[0]);
    int res=binarysearch(arr,0,n-1,3);
    printf("%d\n",res);
    return 0;

}