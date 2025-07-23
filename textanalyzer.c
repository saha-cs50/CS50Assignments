#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int letternumber(string text);
int wordnumber(string text);
int sentencenumber(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = letternumber(text);
    int words = wordnumber(text);
    int sentences = sentencenumber(text);


    printf("Number of letters is: %i\n",letters);
    printf("Number of words is: %i\n",words);
    printf("Number of sentences is: %i\n",sentences);
}



//counts words
int wordnumber(string text)
{
    int j = 0;
    int spaces = 0;
    while(text[j] != '\0')
    {
        if(isspace(text[j]))
        {
            spaces++;
        }
        j++;
    }
    int wordcount = spaces + 1;
    return wordcount;
}

//counts letters
int letternumber(string text)
{
    int i = 0;
    int lettercount = 0;
    while(text[i] != '\0')
    {
        if(isalpha(text[i]))
        {
            lettercount++;
        }
        i++;
    }
    return lettercount;
}

//counts sentences
int sentencenumber(string text)
{
    int k = 0;
    int sentencecount = 0;
    while(text[k] != '\0')
    {
        if(text[k] == '.' || text[k] == '?' || text[k] == '!')
        {
            sentencecount++;
        }
        k++;
    }
    return sentencecount;
}