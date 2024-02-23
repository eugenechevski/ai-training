/*
    Prompt: Perfect. Next time, ensure that you have a header included as well. 
    Alright, let's move to the next task that I need you to accomplish: create a function that counts digits in a string.
*/

#include <ctype.h> // Both models failed to include this header

// Model A

#include <stdio.h>
#include <string.h>

int count_digitsA(const char *str) {
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        char c = str[i];
        if (c >= '0' && c <= '9') {
            count++;
        }
    }
    return count;
}

int mainA() {
    char str[] = "Hello, world! 123";
    int num_digits = count_digitsA(str);
    printf("Number of digits: %d\n", num_digits);
    return 0;
}


// Model B

#include <stdio.h>
#include <string.h>

int count_digitsB(const char *str) {
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        char c = str[i];
        if (isdigit(c)) {
            count++;
        }
    }
    return count;
}

int mainB() {
    char str[] = "Hello, world! 123";
    int num_digits = count_digitsB(str);
    printf("Number of digits: %d\n", num_digits);
    return 0;
}


int main() {
    mainA();
    mainB();

    return 0;
}

// VERDICT: Models provided an identical quality of code. Both models failed to included the required header