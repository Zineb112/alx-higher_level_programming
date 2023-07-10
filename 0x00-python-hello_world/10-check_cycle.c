#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: singly-linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	ptr1 = list->next;
	ptr2 = list->next->next;

	while (ptr1 && ptr2 && ptr2->next)
	{
		if (ptr1 == ptr2)
			return (1);

		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
	}
	return (0);
}
