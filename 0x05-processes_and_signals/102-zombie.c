#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * main - Creates 5 zombies processes
 *
 * Return: Status
 */


int infinite_while(void);

int main(void)
{
	pid_t pid;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == 0)
		{
			exit(0);
		}
		else
			printf("Zombie process created, PID:%d\n", pid);
	}

		sleep(10000);

	return (0);
}

/**
 * infinite_while - Infinite loop to sleep
 *
 * Return: Status
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}
