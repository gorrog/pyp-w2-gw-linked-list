# -*- coding: utf-8 -*-
import unittest

from linked_list.node import Node
from linked_list.implementation import LinkedList


class LinkedListTestCase(unittest.TestCase):

    def test_creation_and_equal(self):
        l1 = LinkedList([1, 2, 3])

        self.assertTrue(l1.start is not None)
        self.assertEqual(l1.start.elem, 1)

        self.assertTrue(l1.end is not None)
        self.assertEqual(l1.end.elem, 3)

        self.assertTrue(l1.start.next is not None)
        self.assertEqual(l1.start.next.elem, 2)

        self.assertTrue(l1.start.next.next is not None)
        self.assertEqual(l1.start.next.next.elem, 3)

    def test_append(self):
        my_list = LinkedList()

        my_list.append(1)
        self.assertEqual(my_list.start.elem, 1)
        self.assertEqual(my_list.start.next, None)
        self.assertEqual(my_list, LinkedList([1]))

        my_list.append(2)
        self.assertEqual(my_list.start.elem, 1)
        self.assertEqual(my_list.start.next, Node(2))
        self.assertEqual(my_list.start.next.elem, 2)
        self.assertEqual(my_list.start.next.next, None)

        self.assertEqual(my_list.count(), 2)

    def test_count(self):
        self.assertEqual(LinkedList([1, 2, 3]).count(), 3)

    def test_pop_removes_last_item_by_default(self):
        l1 = LinkedList([1, 2, 3])

        elem = l1.pop()
        self.assertEqual(elem, 3)
        self.assertEqual(l1.count(), 2)
        self.assertEqual(l1, LinkedList([1, 2]))

    def test_pop_removes_first_item(self):
        l1 = LinkedList([1, 2, 3])

        elem = l1.pop(0)
        self.assertEqual(elem, 1)
        self.assertEqual(l1.count(), 2)
        self.assertEqual(l1, LinkedList([2, 3]))

    def test_pop_removes_last_item(self):
        l1 = LinkedList([1, 2, 3])

        elem = l1.pop(2)
        self.assertEqual(elem, 3)
        self.assertEqual(l1.count(), 2)
        self.assertEqual(l1, LinkedList([1, 2]))

    def test_pop_removes_item_in_the_middle_of_the_list(self):
        l1 = LinkedList([1, 2, 3, 4, 5])

        elem = l1.pop(2)
        self.assertEqual(elem, 3)
        self.assertEqual(l1.count(), 4)
        self.assertEqual(l1, LinkedList([1, 2, 4, 5]))

        elem = l1.pop(1)
        self.assertEqual(elem, 2)
        self.assertEqual(l1.count(), 3)
        self.assertEqual(l1, LinkedList([1, 4, 5]))

    def test_pop_with_a_single_element_list(self):
        # Default index
        l1 = LinkedList([9])

        elem = l1.pop()
        self.assertEqual(elem, 9)
        self.assertEqual(l1.count(), 0)
        self.assertEqual(l1, LinkedList([]))

        # index == 0
        l1 = LinkedList([9])

        elem = l1.pop(0)
        self.assertEqual(elem, 9)
        self.assertEqual(l1.count(), 0)
        self.assertEqual(l1, LinkedList([]))

    def test_pop_raises_an_exception_with_empty_list(self):
        with self.assertRaises(IndexError):
            LinkedList().pop()

        with self.assertRaises(IndexError):
            LinkedList().pop(0)

        with self.assertRaises(IndexError):
            LinkedList().pop(3)

    def test_pop_raises_an_exception_with_invalid_index(self):
        with self.assertRaises(IndexError):
            LinkedList([1]).pop(1)

        with self.assertRaises(IndexError):
            LinkedList([1, 2, 3]).pop(3)

    def test_equals(self):
        self.assertEqual(
            LinkedList([1, 2, 3]),
            LinkedList([1, 2, 3]))

        self.assertEqual(
            LinkedList([]),
            LinkedList([]))

        self.assertEqual(
            LinkedList([1]),
            LinkedList([1]))

        self.assertNotEqual(
            LinkedList([1, 2]),
            LinkedList([1, 2, 3]))

        self.assertNotEqual(
            LinkedList([1]),
            LinkedList([]))

    def test_add_list(self):
        my_list = LinkedList()
        new_list = my_list + LinkedList([1])
        self.assertEqual(new_list, LinkedList([1]))
        self.assertEqual(my_list, LinkedList())

        my_list = LinkedList([1, 2])
        new_list = my_list + LinkedList([3, 4])
        self.assertEqual(new_list, LinkedList([1, 2, 3, 4]))
        self.assertEqual(my_list, LinkedList([1, 2]))

        my_list = LinkedList([1, 2])
        new_list = my_list + LinkedList()
        self.assertEqual(new_list, LinkedList([1, 2]))
        self.assertEqual(my_list, LinkedList([1, 2]))

        my_list = LinkedList()
        new_list = my_list + LinkedList()
        self.assertEqual(new_list, LinkedList())
        self.assertEqual(new_list.count(), 0)
        self.assertEqual(my_list, LinkedList())
        self.assertEqual(my_list.count(), 0)

    def test_str(self):
        my_list = LinkedList([1, 2, 3])
        self.assertEqual(str(my_list), "[1, 2, 3]")

        my_list = LinkedList()
        self.assertEqual(str(my_list), "[]")

        my_list = LinkedList([])
        self.assertEqual(str(my_list), "[]")

    def test_add_equals_list(self):
        my_list = LinkedList()
        my_list += LinkedList([1, 2])
        self.assertEqual(my_list, LinkedList([1, 2]))

        my_list = LinkedList([1, 2])
        my_list += LinkedList([3, 4])
        self.assertEqual(my_list, LinkedList([1, 2, 3, 4]))

        my_list = LinkedList([1, 2])
        my_list += LinkedList()
        self.assertEqual(my_list, LinkedList([1, 2]))

        my_list = LinkedList()
        my_list += LinkedList()
        self.assertEqual(my_list.count(), 0)
        self.assertEqual(my_list, LinkedList())

    def test_not_equals(self):
        self.assertNotEqual(
            LinkedList([1, 2, 3]),
            LinkedList([5, 2, 1]))

        self.assertNotEqual(
            LinkedList([]),
            LinkedList([3]))

        self.assertNotEqual(
            LinkedList([1,5]),
            LinkedList([4]))

        self.assertEqual(
            LinkedList([1, 2]),
            LinkedList([1, 2]))

        self.assertEqual(
            LinkedList([1]),
            LinkedList([1])) 
  
    def test_node_str(self):
        my_node = Node(4)
        self.assertEqual(str(my_node), "4")
        
    def test_get_item(self):
        my_list = LinkedList([1,2,3,4])
        self.assertEqual(my_list[2], 3)
        self.assertEqual(my_list[0], 1)
        self.assertEqual(my_list[3], 4)
        
        my_list2 = LinkedList([1])
        self.assertEqual(my_list[0], 1)
        with self.assertRaises(TypeError):
            my_list2["hello"]
        with self.assertRaises(KeyError):
            my_list2[9]
        with self.assertRaises(KeyError):
            my_list2[-1]