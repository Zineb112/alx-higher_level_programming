#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointre.
 * Return: 1 if success 0 if failed
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int value[2048], x = 0, p, limit;

	if (head == NULL || *head == NULL)
		return (1);

	while (tmp != NULL)
	{
		value[x] = tmp->n;
		x++;
		tmp = tmp->next;
	}

	limit = (x % 2 == 0) ? x / 2 : (x + 1) / 2;

	for (p = 0; p < limit; p++)
		if (value[p] != value[x - 1 - p])
			return (0);

	return (1);
}
