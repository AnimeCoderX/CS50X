#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, i, j;
    do
    {
        height = get_int("Enter height: ");
    }
    while (height < 1 || height > 8);

    for (i = 0; i < height; i++)
    {
        for (j = 0; j < i + 1 ; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
