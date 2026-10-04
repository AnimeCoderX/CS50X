#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Define the maximum number of candidates
#define MAX 2

// Define a struct called "candidate" representing a candidate
typedef struct
{
    string name;
    int votes;
} candidate;

// Global array of candidates
candidate candidates[MAX];

// Number of candidates in the election
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: %s [candidate1] [candidate2] [...]\n", argv[0]);
        return 1;
    }
    // Populate the candidates array with the candidate names from command line arguments
    candidate_count = argc - 1;

    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %d\n", MAX);
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    // Add "barket" as a candidate
    candidates[candidate_count].name = "barket";
    candidates[candidate_count].votes = 0;
    candidate_count++;

    // Get the number of voters from the user
    int voter_count = get_int("Number of voters: ");

    // Loop through each voter
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check if the vote is valid and update vote counts
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Print the winner(s) of the election
    print_winner();
}

// Update vote totals for a given candidate
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner(s) of the election
void print_winner(void)
{
    int max_votes = 0;

    // Find the maximum number of votes
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > max_votes)
        {
            max_votes = candidates[i].votes;
        }
    }

    // Print the name(s) of the winner(s)
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == max_votes)
        {
            printf("%s\n", candidates[i].name);
        }
    }
}
