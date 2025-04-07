# Sersh throgh tree in deap
# Explore each branch to deep branch by branch

from treelib import Tree


tree = Tree()
tree.create_node('a', 'a')
tree.create_node('b', 'b', parent='a')
tree.create_node('c', 'c', parent='a')
tree.create_node('d', 'd', parent='a')
tree.create_node('h', 'h', parent='d')
tree.create_node('g', 'g', parent='d')
tree.create_node('k', 'k', parent='g')
tree.create_node('e', 'e', parent='b')
tree.create_node('f', 'f', parent='b')
tree.create_node('i', 'i', parent='f')
tree.create_node('j', 'j', parent='f')
tree.show()


# Enstead of depth serch I write finde leafs alg)
def leafs(tree, node, result = []):
    '''Return list of leafs'''
    if not tree.children(node):
        result.append(node)
    
    for node in tree.children(node):
        leafs(tree, node.identifier)

    return result

print(leafs(tree, tree.root))


# O(v+e) time. v:vertices e:edges | O(v) space
def depth_first_search(tree, node, result = []):
    '''Return list of nodes tag'''
    result.append(node)
    
    for node in tree.children(node):
        depth_first_search(tree, node.identifier)
    
    return result


# [a,b,e,f,i,j,c,d,g,k,h]
print(depth_first_search(tree, tree.root))
