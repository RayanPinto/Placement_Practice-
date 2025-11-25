#include<stdio.h>
#include<ctype.h>
#include<string.h>
void isvowel(char *ss,int *v,int *c){
    char s[100];
    int i=0;
    while(ss[i]!='\0'){
        s[i]=tolower(ss[i]);
        i++;
    }
    s[i]='\0';
    printf("%s",s);

    int volcount=0;
    int consonants=0;
    int n;
    n=strlen(s);
    for(int i=0;i<n;i++){
    if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'){
        volcount++;
        
    }else{
        consonants++;
    }
}
    *v =volcount;
    *c=consonants;
}
int main(){
char str[]="Abcbabc";
int v,c;
isvowel(str,&v,&c);
printf("%d\t%d\t",v,c);

    return 0;
}