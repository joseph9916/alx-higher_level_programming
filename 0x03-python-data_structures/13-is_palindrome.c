#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - a function that checks if a singly linked list
 * is a palindrome.
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *walk_back, *walk_forward, *walk;

	if (!head)
		return (1);
	walk_back = *head;
	walk_forward = *head;
	if (!walk_forward->next)
		return (1);
	/*to get to the tail of the list*/
	while (walk_back->next)
	{
		walk_back = walk_back->next;
	}
	while (walk_forward->n == walk_back->n)
	{
		if (walk_back == walk_forward || walk_forward->next == walk_back)
			return (1);
		walk = walk_forward;
		while (walk->next != walk_back)
			walk = walk->next;
		walk_back = walk;
		walk_forward = walk_forward->next;
	}
	return (0);
}
