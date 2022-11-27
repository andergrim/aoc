#include <stdio.h>
#include <stdlib.h>

int prog[] = {1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 9, 19, 1, 5, 19,
			  23, 1, 6, 23, 27, 1, 27, 10, 31, 1, 31, 5, 35, 2, 10, 35, 39, 1, 9, 39,
			  43, 1, 43, 5, 47, 1, 47, 6, 51, 2, 51, 6, 55, 1, 13, 55, 59, 2, 6, 59,
			  63, 1, 63, 5, 67, 2, 10, 67, 71, 1, 9, 71, 75, 1, 75, 13, 79, 1, 10,
			  79, 83, 2, 83, 13, 87, 1, 87, 6, 91, 1, 5, 91, 95, 2, 95, 9, 99, 1, 5,
			  99, 103, 1, 103, 6, 107, 2, 107, 13, 111, 1, 111, 10, 115, 2, 10, 115,
			  119, 1, 9, 119, 123, 1, 123, 9, 127, 1, 13, 127, 131, 2, 10, 131, 135,
			  1, 135, 5, 139, 1, 2, 139, 143, 1, 143, 5, 0, 99, 2, 0, 14, 0};

int main() {
	int pointer = 0;
	int operation, input_x_pos, input_y_pos, output_pos;

	prog[1] = 12;
	prog[2] = 2;

	while (1) {
		operation = prog[pointer];

		if (operation == 99) {
			printf("Halt at pos %d\n", pointer);
			printf("Output is: %d\n", prog[0]);
			exit(0);
		}

		input_x_pos = prog[pointer + 1];
		input_y_pos = prog[pointer + 2];
		output_pos = prog[pointer + 3];

		switch (operation) {
			case 1:
				prog[output_pos] = prog[input_x_pos] + prog[input_y_pos];
				break;
			case 2:
				prog[output_pos] = prog[input_x_pos] * prog[input_y_pos];
				break;
			default:
				printf("ERROR Illegal operation %d at pos %d\n", operation, pointer);
				exit(1);
		}

		pointer = pointer + 4;

	}
}
