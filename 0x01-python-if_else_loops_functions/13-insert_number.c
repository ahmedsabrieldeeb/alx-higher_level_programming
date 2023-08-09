#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserting a number into a sorted singly linked list.
 * @head: a pointer to the pointer pointing to the first node.
 * @number: the number to be inserted (int).
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL || number <= (*head)->n)
	{
		newNode = *head;
		*head = newNode;
		return (*head);
	}

	while (temp->next != NULL && number > temp->next->n)
		temp = temp->next;

	newNode->next = temp->next;
	temp->next = newNode;

	return (newNode);
}
