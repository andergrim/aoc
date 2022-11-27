#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	FILE *filePointer;
	char *line;
	size_t len = 0;
	ssize_t read;

	filePointer = fopen("02.txt", "r");

	if (filePointer == NULL)
		exit(EXIT_FAILURE);

	while ((read = getline(&line, &len, filePointer)) != -1)
	{
		printf("%s", line);
		int width, length, height = 0;
		char *token = strtok(line, "x");
		while (token) {
			printf("%s", token);
			token = strtok(NULL, " ");
		}

		printf("%s", line);
	}

	fclose(filePointer);
	if (line)
		free(line);
	
	return 0;
}
