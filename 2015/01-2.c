#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *filePointer;
	char ch;
 	int floor = 0;

	const int up =  *"(";
	const int down = *")";

	filePointer = fopen("01.txt", "r");

    int pos = 0;
	while ((ch = fgetc(filePointer)) != EOF)
	{
        pos++;
		if (ch == up) {
			floor++;
		} else if (ch == down) {
			floor--;
		}

        if (floor == -1) {
            printf("%d\n", pos);
            return 0;
        }

	}
	return 0;
}
