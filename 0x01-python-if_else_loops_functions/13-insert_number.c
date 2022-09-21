#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linked list
 * @number: integer to be inserted as element of new node
 *
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;
	listint_t *current = *head;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (current && number > current->n)
		{
			temp = current;
			current = current->next;
		}
		temp->next = new;
		new->next = current;
	}

	return (new);
}
