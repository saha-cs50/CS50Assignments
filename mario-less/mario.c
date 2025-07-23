#include <cs50.h>
#include <stdio.h>


int main(void)
{
    //get input from user
    int height;
    do
    {
        height = get_int("Enter a Positive Number: ");
    }
    while (height < 1 || height > 8);

    //controls new line
    for (int i = height - 1; i >= 0; i--)
    {
        //controls spaces
        for (int j = 0; j < i; j++)
        {
            printf(" ");
        }

        //controls hashes
        for (int k = height; k > i; k--)
        {
            printf("#");
        }

        printf("\n");
    }

}