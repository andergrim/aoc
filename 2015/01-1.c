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

	while ((ch = fgetc(filePointer)) != EOF)
	{
		if (ch == up) {
			floor++;
		} else if (ch == down) {
			floor--;
		}

	}
	printf("%d\n", floor);
	return 0;
}
