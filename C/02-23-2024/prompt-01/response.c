/*
    Prompt: I need to write a function that takes a string as input and returns the number of vowels in the string. Can you help me with that? In C?
*/

// Model A

#include <string.h>

int count_vowelsA(const char *str)
{
    int count = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        char c = str[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
        {
            count++;
        }
    }
    return count;
}

int mainA()
{
    // Model A
    // warning: ISO C++ forbids converting a string constant to ‘char*’
    char *str = "hello world";
    int num_vowels = count_vowelsA(str);
    printf("%d\n", num_vowels); // Output: 3

    return 0;
}


// Model B

#include <stdio.h>
#include <string.h>

int count_vowelsB(const char *str)
{
    int count = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        char c = str[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
        {
            count++;
        }
    }
    return count;
}

int mainB()
{
    // Model B
    char str[] = "Hello, world!";
    int num_vowels = count_vowelsB(str);
    printf("Number of vowels: %d\n", num_vowels);

    return 0;
}


int main() {
    mainA();
    mainB();

    return 0;
}

// VERDICT: Model B is better