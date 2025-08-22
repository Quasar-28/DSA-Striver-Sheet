# see leetcode problem 206
# Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.
class Node :
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next 
def reverse_SLL(head) :

    