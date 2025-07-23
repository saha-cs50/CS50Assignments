#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    //condition for taking 2 arguments in cli
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE \n");
        return 1;
    }

    FILE *f = fopen(argv[1], "r");

    unsigned char buffer[512];

    int imagecount = 0;

    FILE *output = NULL;

    //allocating memory for the output(same size as input file)
    char *file = malloc(8 * sizeof(char));

    while (fread(buffer, sizeof(char), 512, f))
    {
        //if it is recognized as the beginning of the JPEG file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(file, "%03i.jpg", imagecount);
            output = fopen(file, "w");
            imagecount++;
        }

        if (output != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output);
        }
    }

    //freeing all used up memory
    free(file);
    fclose(output);
    fclose(f);

    return 0;
    fclose(file);
}