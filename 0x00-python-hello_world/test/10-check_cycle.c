#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function name
 * @list: a pointer to a list
 * Description:  checks if a singly linked list has a cycle in it.
 * Return: 0 if no cycle, 1 if there is one
 */
int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	t = list;
	h = list;

	while (h != NULL)
	{
		t = t->next;
		h = h->next->next;

		if (t == h)
			return (1);
	}
	return (0);
}
