import data
import decision_tree

def main(input_data):
    tree = decision_tree.DecisionTree()
    tree.buildTree(data.graph)
    print(tree.compile(input_data))

main(['less', 1991, 'hy', 1981, 2004])