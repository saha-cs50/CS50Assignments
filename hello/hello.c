#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //taking user input
    string name = get_string("What's your name?\n");
    //printing hello + inputted name
    printf("hello, %s\n", name);

}


