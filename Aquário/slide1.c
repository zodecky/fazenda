#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *pFile;
    long lSize;
    char *buffer;
    size_t result;

    pFile = fopen("myfine.bin", "rb");
    if (pFile == NULL)
    {
        fputs("File error", stderr);
        exit(1);
    }
    fseek(pFile, 0, SEEK_END);
    lSize = ftell(pFile);
    rewind(pFile);
    buffer = (char *)malloc(sizeof(char) * lSize);
    if (buffer == NULL)
    {
        fputs("Memory error", stderr);
        exit(2);
    }
    result = fread(buffer, 1, lSize, pFile);
    if (result != lSize)
    {
        fputs("Reading error", stderr);
        exit(3);
    }
    /* the whole file is now loaded in the memory buffer. */
    /* do something here with the buffer */
    fclose(pFile);
    free(buffer);
    return 0;
}