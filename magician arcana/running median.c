#include <stdio.h>
#include <stdlib.h>

float getMedian(int arr[], int ctr1)
{
    if (ctr1 % 2 == 0)
        return arr[ctr1 / 2];

    else
        return (arr[ctr1 / 2] + arr[(ctr1 + 1) / 2]) / 2.0;
}

int main()
{
    int ctr1, ctr2, ctr3, size, pivot, start, end, mid;
    int *arr;

    scanf("%d", &size);

    arr = malloc(size * sizeof(int));

    for (ctr1 = 0; ctr1 < size; ctr1++)
    {
        start = 0;
        end = ctr1;
        mid = (end - start) / 2;

        scanf("%d", &pivot);

        while (start != mid && mid != end)
        {
            if (arr[mid] > pivot)
                end = mid;

            else
                start = mid;

            mid = start + (end - start) / 2;
        }

        for (ctr2 = mid; ctr2 < ctr1; ctr2++)
        {
            if (arr[ctr2] > pivot)
                break;
        }

        for (ctr3 = ctr1; ctr3 >= (ctr2 + 1); ctr3--)
        {
            arr[ctr3] = arr[ctr3 - 1];
        }

        arr[ctr2] = pivot;

        printf("%.1f\n", getMedian(arr, ctr1));
    }

    return 0;
}