#include <stdio.h>

int main() {
	int x = 0;
	int y = 1;
	int z;
	do {
		printf("%d ", x);
		z = x + y;
		x = y;
		y = z;
	} while (x < 255);
	return 0;
}