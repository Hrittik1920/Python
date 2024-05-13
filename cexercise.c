#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){int age;scanf("%d",&age);if(age>=18) printf("You are a adult"); else if(age<18 && age>12) printf("You are a Teenage");else printf("You are a child");return 0;}