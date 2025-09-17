#include<stdio.h>
#include<stdlib.h>

struct node{
int data;
struct node *next;
};
int printhead(struct node *n){
    while(n!=NULL){
        printf("%d\t",n->data);
        n=n->next;
    }
return 0;
}
int main(){
    struct node *head;
    struct node *second;
    struct node *third;
    head=(struct node*)malloc(sizeof(struct node));
    second=(struct node*)malloc(sizeof(struct node));
    third=(struct node*)malloc(sizeof(struct node));
    head->data=3;
    head->next=second;
    second->data=4;
    second->next=third;
    third->data;
    third->next=NULL;
    printhead(head);
    return 0;
}
