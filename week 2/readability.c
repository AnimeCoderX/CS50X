#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int compute_index(int letters, int words, int sentences);

int main(void)
{
    // user Prompt the for a string of text
    string text = get_string("Text: ");

    // Count letters, words, and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    int index = compute_index(letters, words, sentences);

    // Determine the reading grade level
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

    return 0;
}

// Function to count the number of letters in a text
int count_letters(string text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }

    return count;
}

// Function to count the number of words in a text
int count_words(string text)
{
    int count = 1; // Start with 1 to account for the first word

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isspace(text[i]))
        {
            count++;
        }
    }

    return count;
}

// Function to count the number of sentences in a text
int count_sentences(string text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }

    return count;
}

// Function to compute the Coleman-Liau index
int compute_index(int letters, int words, int sentences)
{
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;

    return round(0.0588 * L - 0.296 * S - 15.8);
}
