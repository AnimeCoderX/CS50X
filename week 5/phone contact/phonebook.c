#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main (void)
{
    person people[3];

    people[0].name = "messi";
    people[0].number = "0-305-234-162-4";

    people[1].name = "askari";
    people[1].number = "0-313-285-941-7";

    people[2].name = "ammi";
    people[2].number = "0-333-217-974-1";

    string s = get_string("Name: ");
    for(int i = 0; i < 3; i++)
    {
        if(strcmp(people[i].name, s) == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not Found\n");
}
