#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char String[20];

void occurCount(char **strings, char **queries, int stringsSize, int queriesSize)
{
    int ctr1, ctr2, count;

    for (ctr1 = 0; ctr1 < queriesSize; ctr1++)
    {
        count = 0;

        for (ctr2 = 0; ctr2 < stringsSize; ctr2++)
        {
            if (strcmp(queries[ctr1], strings[ctr2]) == 0)
                count++;
        }

        printf("%d\n", count);
    }
}

int main()
{
    int ctr, stringsSize, queriesSize;
    char **strings, **queries;
    String word;

    scanf("%d", &stringsSize);

    strings = malloc(stringsSize * sizeof(char *));

    for (ctr = 0; ctr < stringsSize; ctr++)
    {
        scanf("%s", word);

        strings[ctr] = malloc(strlen(word));

        strcpy(strings[ctr], word);
    }

    scanf("%d", &queriesSize);

    queries = malloc(queriesSize * sizeof(char *));

    for (ctr = 0; ctr < queriesSize; ctr++)
    {
        scanf("%s", word);

        queries[ctr] = malloc(strlen(word));

        strcpy(queries[ctr], word);
    }

    occurCount(strings, queries, stringsSize, queriesSize);

    return 0;
}