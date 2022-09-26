#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */

void reverse_listint_t(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares 2 linked lists to check if they
 * have the same data
 * @first: first linked list
 * @second: second list
 *
 * Return: 1 if true. 0 if otherwise
 */
int compare_listint_t(listint_t **first, listint_t **second)
{
	listint_t *tmp1 = *first;
	listint_t *tmp2 = *second;

	while (tmp1 && tmp2)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
			return (0);
	}
	if (!tmp1 && !tmp2)
		return (1);

	return (0);
}

 /**
 * is_palindrome - checks if a singly linked list
 * is a palindrome or not
 * @head: linked list
 *
 * Return: 1 if it is a palindrome. 0 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *second_half = NULL;
	listint_t *prev_of_slow = *head;
	listint_t *mid_node = NULL;
	int res = 1;

	if (*head && (*head)->next)
	{
		while (fast && fast->next)
		{
			fast = fast->next->next;
			prev_of_slow = slow;
			slow = slow->next;
		}
		if (fast)
		{
			mid_node = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev_of_slow->next = NULL;
		reverse_listint_t(&second_half);
		res = compare_listint_t(head, &second_half);
		reverse_listint_t(&second_half);
		if (mid_node)
		{
			prev_of_slow->next = mid_node;
			mid_node->next = second_half;
		}
		else
			prev_of_slow->next = second_half;
	}
	return (res);
}
