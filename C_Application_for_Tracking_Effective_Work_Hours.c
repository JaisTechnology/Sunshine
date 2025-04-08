#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main() {
    time_t start, end;
    char ch;

    printf("Press ENTER to start working...\n");
    getchar();
    time(&start);

    printf("Working... Press ENTER to stop\n");
    getchar();
    time(&end);

    double hours = difftime(end, start) / 3600;
    printf("Total effective work time: %f hours\n", hours);
    return 0;
}
