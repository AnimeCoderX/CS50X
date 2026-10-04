#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

// Function to check if a key is valid
bool is_valid_key(const char *key);

// Function to encrypt plaintext using a substitution cipher
void encrypt(const char *plaintext, const char *key);

int main(int argc, char *argv[])
{
    // Check for correct number of command-line arguments
    if (argc != 2 || !is_valid_key(argv[1]))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Get the key from the command-line argument
    const char *key = argv[1];

    // Prompt the user for plaintext
    char plaintext[1000];
    printf("plaintext:  ");
    fgets(plaintext, sizeof(plaintext), stdin);

    // Encrypt and print the ciphertext
    printf("ciphertext: ");
    encrypt(plaintext, key);

    return 0;
}

bool is_valid_key(const char *key)
{
    // Check if the key is exactly 26 characters long
    if (strlen(key) != 26)
    {
        return false;
    }

    // Create an array to track used characters
    bool used[26] = {false};

    for (int i = 0; i < 26; i++)
    {
        char c = key[i];

        // Check if the character is an alphabetic letter
        if (!isalpha(c))
        {
            return false;
        }

        // Convert the character to uppercase
        c = toupper(c);

        // Check if the character has been used before
        if (used[c - 'A'])
        {
            return false;
        }

        used[c - 'A'] = true;
    }

    return true;
}

void encrypt(const char *plaintext, const char *key)
{
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];

        // Check if the character is an alphabetic letter
        if (isalpha(c))
        {
            // Determine if it's uppercase or lowercase
            char base = isupper(c) ? 'A' : 'a';

            // Calculate the index of the character in the key
            int index = c - base;

            // Replace the character with the corresponding key character
            printf("%c", isupper(plaintext[i]) ? toupper(key[index]) : tolower(key[index]));
        }
        else
        {
            // Character is not an alphabetic letter, print it unchanged
            printf("%c", c);
        }
    }

    printf("\n");
}
