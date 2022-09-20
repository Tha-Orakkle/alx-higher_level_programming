#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: liked list
 *
 * Return: 0 if there is no cycle, 1 if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp1 = list;
	listint_t *tmp2 = list;

	if (!list)
		return (0);

	while (tmp1 && tmp2 && tmp2->next)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;

		if (tmp1 == tmp2)
			return (1);
	}

	return (0);
}
