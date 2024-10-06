# Example sets for demonstration
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. add() - Adds an element to the set
set1.add(6)
print("1. add(6):", set1)

# 2. clear() - Removes all elements from the set
cleared_set = set1.copy()
cleared_set.clear()
print("2. clear():", cleared_set)

# 3. copy() - Returns a shallow copy of the set
copied_set = set1.copy()
print("3. copy():", copied_set)

# 4. difference() - Returns the difference of two sets as a new set
difference_set = set1.difference(set2)
print("4. difference(set2):", difference_set)

# 5. difference_update() - Removes all elements of another set from this set
set1_difference_update = set1.copy()
set1_difference_update.difference_update(set2)
print("5. difference_update(set2):", set1_difference_update)

# 6. discard() - Removes an element from the set if it is a member (does nothing if not)
set1_discard = set1.copy()
set1_discard.discard(3)
print("6. discard(3):", set1_discard)

# 7. intersection() - Returns the intersection of two sets as a new set
intersection_set = set1.intersection(set2)
print("7. intersection(set2):", intersection_set)

# 8. intersection_update() - Updates the set with the intersection of itself and another
set1_intersection_update = set1.copy()
set1_intersection_update.intersection_update(set2)
print("8. intersection_update(set2):", set1_intersection_update)

# 9. isdisjoint() - Returns True if two sets have a null intersection
is_disjoint = set1.isdisjoint(set2)
print("9. isdisjoint(set2):", is_disjoint)

# 10. issubset() - Returns True if another set contains this set
is_subset = {1, 2}.issubset(set1)
print("10. issubset({1, 2}):", is_subset)

# 11. issuperset() - Returns True if this set contains another set
is_superset = set1.issuperset({1, 2})
print("11. issuperset({1, 2}):", is_superset)

# 12. pop() - Removes and returns an arbitrary set element (raises KeyError if empty)
set1_pop = set1.copy()
popped_element = set1_pop.pop()
print("12. pop():", popped_element)
print("After pop:", set1_pop)

# 13. remove() - Removes an element from the set (raises KeyError if not found)
set1_remove = set1.copy()
set1_remove.remove(2)
print("13. remove(2):", set1_remove)

# 14. symmetric_difference() - Returns the symmetric difference of two sets as a new set
symmetric_difference_set = set1.symmetric_difference(set2)
print("14. symmetric_difference(set2):", symmetric_difference_set)

# 15. symmetric_difference_update() - Updates a set with the symmetric difference of itself and another
set1_symmetric_difference_update = set1.copy()
set1_symmetric_difference_update.symmetric_difference_update(set2)
print("15. symmetric_difference_update(set2):", set1_symmetric_difference_update)

# 16. union() - Returns the union of sets as a new set
union_set = set1.union(set2)
print("16. union(set2):", union_set)

# 17. update() - Updates the set with the union of itself and another
set1_update = set1.copy()
set1_update.update(set2)
print("17. update(set2):", set1_update)

# Additional set operations

# 18. length of set
length_of_set = len(set1)
print("18. Length of set1:", length_of_set)

# 19. Checking membership
is_in_set = 3 in set1
print("19. Is 3 in set1:", is_in_set)

# 20. Iterating through a set
print("20. Iterating through set1:")
for element in set1:
    print(element, end=" ")
print()

# 21. Creating a set from a list
list_to_convert = [1, 2, 2, 3, 4]
converted_set = set(list_to_convert)
print("21. Converted set from list:", converted_set)

# 22. Frozenset (immutable set)
frozen_set = frozenset([1, 2, 3, 4])
print("22. frozenset:", frozen_set)
