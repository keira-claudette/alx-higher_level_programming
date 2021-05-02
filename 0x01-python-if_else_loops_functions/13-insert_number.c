#include "lists.h"

/**
 * insert_node - inserts a number in an ordered linked list
 * @head: double pointer to the linked list
 * @number: number to insert in the new node
 *
 * Return: address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new = NULL;
	listint_t *prev_node = NULL;

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
		return (*head = new);
	}
	else
	{
		while (temp && number > temp->n)
		{
			prev_node = temp;
			temp = temp->next;
		}
		prev_node->next = new;
		new->next = temp;
	}

	return (new);
}
