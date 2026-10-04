#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // calculate the number of quarter to give the customer
    int quarters = calculate_quarters(cents);
    cents -= quarters * 25;a

    // calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents -= dimes * 10;

    // calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents -= nickels * 5;

    // calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);

    // Sum coins
    int total_coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%d\n", total_coins);
}

 int get_cents(void)
{
     int cents;
     do
     {
         cents = get_int("Enter the number of cents: ");
     }
     while (cents < 0);
     return cents;
}

 int calculate_quarters(int cents)

{
     return cents / 25;
}

 int calculate_dimes(int cents)

{
     return cents / 10;
}

 int calculate_nickels(int cents)

{
     return cents / 5;
}

 int calculate_pennies(int cents)

{
     return cents;
}
