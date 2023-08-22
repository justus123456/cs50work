#include <stdio.h>
#include <cs50.h>

int main(void){
    int rice = get_int("what is the number? ");
    int oat = get_int("what is the other number? ");

    if (rice < oat)
    {
        printf("rice is big.\n")
    }
}