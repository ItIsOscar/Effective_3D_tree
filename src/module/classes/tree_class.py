from typing import List

class Tree:
    def __init__(self, treeNode):
        self.root = treeNode

    def byPassInDeepBranch(self):
        '''Создает генератор, при вызове которого возращает следующий ветку дерева прохода в глубину'''
        yield self.__recursive_byPassInDeepBranch(self.root)

    def __recursive_byPassInDeepBranch(self, treeNode):
            for branch in treeNode.branches:
                self.__recursive_byPassInDeepBranch(branch)
            yield treeNode.parent

    def byPassInWidthBranch(self):
        '''Создает генератор, при вызове которого возращает следующий ветку дерева прохода в ширину'''

class TreeNode:
    branches = []

    def addBranch(self, treeNode, radius: float):
        self.branches.append(Branch(self, treeNode, radius))

    def deleteBranch(self, coordinate : List[float, float, float]):
        pass

    def __init__(self, coordinate: List[float, float, float], parent: Branch = None):
        self.x, self.y, self.z = coordinate
        self.parent = parent

    def __eq__(self, value: object) -> bool:
        if isinstance(value, TreeNode):
            return True if self.x == value.x and self.y == value.y and self.z == value.z else False
        else:
            return False

class Branch:

    def __init__(self, first_Node: TreeNode, second_Node: TreeNode, radius: float):
        self.first_Node = first_Node
        self.second_Node = second_Node
        self.radius = radius

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Branch):
            return True if self.first_Node == value.first_Node and self.second_Node == value.second_Node else False
        else:
            return False