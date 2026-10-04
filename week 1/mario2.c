#include <cs50.h>
#include <stdio.h>

// prototye
void draw(int n);

int main(void)
{
    int height = get_int("Height: ");
    draw(height);
}

void draw(int n)
{
    // if nothin do draw
    if(n <= 0)
    return;

    // printing # of HEIGHT n-1
        draw(n-1);

    // printing one more row
        for(int i = 0; i < n; i++)
        {
            printf("#");
        }
        printf("\n");

}
