#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node*next;
};
int printhead(struct node*n){
    while(n!=NULL){
        printf("%d\n",n->data);
        n=n->next;
    }
}
void modifynode(struct node*n,int oldvalue,int newvalue){
    struct node*current=n;
    while(current!=NULL){
        if(current->data==oldvalue){
            current->data=newvalue;
            break;
        }
        current=current->next;
    }
}
int main(){
    struct node*head;
    struct node*second;
    struct node*last;
    head=(struct node*)malloc(sizeof(struct node));
        second=(struct node*)malloc(sizeof(struct node));
    last=(struct node*)malloc(sizeof(struct node));

    head->data=10;
    head->next=second;
    second->data=20;
    second->next=last;
    last->data=30;
    last->next=NULL;
    printhead(head);
    free(head);
    free(second);
    free(last);
    return 0;
}
