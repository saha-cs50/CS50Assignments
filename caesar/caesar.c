#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>


//taking command line input
int main(int argc, string argv[])
{
    //checking if there are two values in cli
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //checking to see if the valid key is given
    int i = 0;
    while (strlen(argv[1]) > i)
    {
        if (isdigit(argv[1][i]) == false)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        i++;
    }

    int key = atoi(argv[1]);

    //printing the prompt for plaintext
    string plaintext = get_string("Plaintext: ");
    printf("Ciphertext: ");

    for (int j = 0; j < strlen(plaintext); j++)
    {
        //if upper case letter
        if (isupper(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 65 + key) % 26 + 65);
        }

        //if lower case letter
        else if (islower(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 97 + key) % 26 + 97);
        }

        //if symbol, space, punctuation
        else
        {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
}

