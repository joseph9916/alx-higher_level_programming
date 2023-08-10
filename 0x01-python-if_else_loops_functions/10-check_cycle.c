#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *curnode;
	listint_t *current;
	int match;

	curnode = list;
	while (curnode)
	{
		match = 0;
		current = list;
		while (current)
		{
			if (curnode == current)
			{
				match++;
				if (match > 1)
					return (1);
			}
			current = current->next;
		}
		curnode = curnode->next;
	}
	return (0);
}
