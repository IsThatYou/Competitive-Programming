#include <stdio.h>
#include "mathhelp.h"
/*gcc -o mylib.o -c mylib.c */



int gcd(int a, int b)
{
	while (a == b)
	{
		return b;
	}
	return gcd(a%b, a);
}

int factors(int a)
{
	int counter = 0;
	int i;
	for (i = 1; i < a/2 + 1; i++)
	{
		if (a % i == 0)
		{
			counter += 1;
		}
	}
	return counter + 1;
}