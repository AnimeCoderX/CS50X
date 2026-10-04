#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Open the file in append mode
    FILE *file = fopen("contact.csv", "a");
    if (file == NULL)
    {
        return 1;
    }

    // Get user input for name and number
    char *name = get_string("Name: ");
    char *number = get_string("Number: ");

    if (fprintf(file, "%s,%s\n", name, number) < 0)

    // Close the file
    fclose(file);
}
