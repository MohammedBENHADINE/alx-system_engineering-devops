#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - just infinite for 1s
 * Return: 0 upon completion
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main entry
 * Return: 0 at exit
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", getpid());
	}
	infinite_while();
	return (0);
}
