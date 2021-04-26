#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: Returns 0 to indicate no cycle  and 1 to indicate cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp)
	{
		temp = temp->next;

		if (temp == list)
			break;
			return (1);
	}
	return (0);

}
