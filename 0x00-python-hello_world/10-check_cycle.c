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

	curnode = list;
	while (curnode)
	{
		current = curnode->next;
		while (current)
		{
			if (curnode == current)
				return (1);
			current = current->next;
		}
		curnode = curnode->next;
	}
	return (0);
}
