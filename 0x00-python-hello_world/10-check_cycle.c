#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the linked list
 * Return: Returns 0 to indicate no cycle  and 1 to indicate cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *temp2 = list->next;

	if (!temp)
		return (0);

	while (temp2)
	{
		temp2 = temp2->next;

		if (temp2 == list)
			break;

	}
	if (!temp2)
		return (0);

	return (1);
}
