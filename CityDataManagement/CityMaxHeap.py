from typing import List
from CityDataManagement.City import City
from CityDataManagement.AbstractCityHeap import AbstractCityHeap


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative upwards.
        """
        # TODO: implement me!
        index = self.currentHeapLastIndex -1
        while self.has_parent(index):
            if self.get_city_population(index) > self.get_parent_population(index):
                self.swap_nodes(self.get_parent_index(index), index)
                index = self.get_parent_index(index)
            else:
                break

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        # TODO: implement me!
        if not self.has_parent(index):
            return
        if self.get_city_population(index) > self.get_parent_population(index):
            self.swap_nodes(self.get_parent_index(index), index)
            
            self.heapify_up_recursive(self.get_parent_index(index))

    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.

        """
        # TODO: implement me!
        for i in range(amount_of_cities // 2, -1, -1):
            self.heapify_down_recursive(index)

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        # TODO: implement me!

        index = 0

        while self.has_left_child(index):
            max_index = index
            left_child_index = self.get_left_child_index(index)
            right_child_index = self.get_right_child_index(index)

            if self.get_left_child_population(index) > self.get_city_population(
                max_index
            ):
                max_index = left_child_index
            if self.has_right_child(index) and self.get_right_child_population(
                index
            ) > self.get_city_population(max_index):
                max_index = right_child_index
            if max_index != index:
                self.swap_nodes(max_index, index)
                index = max_index
            else:
                break

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # TODO: implement me!

        max_index = index
        if self.has_left_child(index) and self.get_left_child_population(
            index
        ) > self.get_city_population(max_index):
            max_index = self.get_left_child_index(index)
        if self.has_right_child(index) and self.get_right_child_population(
            index
        ) > self.get_city_population(max_index):
            max_index = self.get_right_child_index(index)
        if max_index != index:
            self.swap_nodes(max_index, index)
            self.heapify_down_recursive(max_index)

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # TODO: implement me!
