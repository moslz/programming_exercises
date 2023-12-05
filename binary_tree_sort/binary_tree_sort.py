
def tree_by_levels(root):
    result, queue = [], [root] if root else []

    while queue:
        current_node = queue.pop(0)
        
        if current_node is not None:
            result.append(current_node.value)
            queue.extend([current_node.left, current_node.right])

    return result
