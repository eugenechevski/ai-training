/*
    Prompt: great! now take this approach and create a similar function, but instead of vowels, it should count consonants
*/

// Model A

// No <string.h> and <stdio.h> import

/*
int count_consonantsA(const char *str) {
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        char c = str[i];
        if ((c >= 'a' && c <= 'z') && (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')) {
            count++;
        }
    }
    return count;
}

int mainA() {
    char str[] = "Hello, world!";
    int num_consonants = count_consonantsA(str);
    printf("Number of consonants: %d\n", num_consonants);
    return 0;
}
*/

// Model B

#include <stdio.h>
#include <string.h>

int count_consonantsB(const char *str) {
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        char c = str[i];
        if ((c >= 'a' && c <= 'z') && (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')) {
            count++;
        }
    }
    return count;
}

int mainB() {
    char str[] = "Hello, world!";
    int num_consonants = count_consonantsB(str);
    printf("Number of consonants: %d\n", num_consonants);
    return 0;
}

int main()
{
    // mainA();
    mainB();

    return 0;
}

// VERDICT: Model B is better, but with some issues
