#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

	int mass = 0;
	int fuel_total = 0;

    fp = fopen("01.txt", "r");

    while ((read = getline(&line, &len, fp)) != -1) {
		sscanf(line, "%d", &mass);
		fuel_total += floor((mass / 3) - 2);
		printf("%d : %d\n", mass, fuel_total);
    }

    fclose(fp);
    if (line) free(line);
    exit(0);
}
