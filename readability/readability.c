#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int letternumber(string text);
int wordnumber(string text);
int sentencenumber(string text);

int main(void)
{
    //getting input from user
    string text = get_string("Text: ");

    //using the functions made to find number of letters, words and sentences in the text
    int letters = letternumber(text);
    int words = wordnumber(text);
    int sentences = sentencenumber(text);

    //readability coleman-lieu formula
    float formula = (0.0588 * letters / words * 100) - (0.296 * sentences / words * 100) - 15.8;
    int level = round(formula);

    //printing readability level before 1
    if (level < 1)
    {
        printf("Before Grade 1\n");
    }
    //after level 16
    else if (level >= 16)
    {
        printf("Grade 16+\n");
    }
    //between levels 1 to 15
    else
    {
        printf("Grade %i\n", level);
    }
}



//counts words
int wordnumber(string text)
{
    int j = 0;
    int spaces = 0;
    while (text[j] != '\0')
    {
        if (isspace(text[j]))
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
    while (text[i] != '\0')
    {
        if (isalpha(text[i]))
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
    while (text[k] != '\0')
    {
        if (text[k] == '.' || text[k] == '?' || text[k] == '!')
        {
            sentencecount++;
        }
        k++;
    }
    return sentencecount;
}