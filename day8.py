import numpy as np
class day8:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        visible_trees_from_outside_the_grid = 0
        tree_matrix = self.build_trees(input)
        forest_width = len(tree_matrix[0])
        forest_height = len(tree_matrix)
        
        #Check if tree is visible
        for i in range(forest_height):
            for j in range(forest_width):
                if (i == 0 or j == 0 or i == forest_height-1 or j == forest_width-1):
                    visible_trees_from_outside_the_grid += 1
                    pass
                elif (tree_matrix[i][j] > max(tree_matrix.transpose()[j][:i], default=0) 
                    or tree_matrix[i][j] > max(tree_matrix.transpose()[j][i+1:], default=0)
                    or tree_matrix[i][j] > max(tree_matrix[i][:j], default=0)
                    or tree_matrix[i][j] > max(tree_matrix[i][j+1:], default=0)
                    ):
                    visible_trees_from_outside_the_grid += 1
                    pass

        print(f"There are {visible_trees_from_outside_the_grid} visible trees")
        return visible_trees_from_outside_the_grid
 
    def build_trees(self, input):
        horizontal_lines = input.split('\n')
        tree_matrix = np.zeros([len(horizontal_lines), len(horizontal_lines[0])], dtype = int)
        forest_width = len(horizontal_lines[0])
        forest_height = len(horizontal_lines)
        for i in range(forest_height):
            for j in range(forest_width):
                tree_matrix[i][j] = int(horizontal_lines[i][j])
        return tree_matrix
    
    def star2(self, input):
        highest_scenic_score = 0
        tree_matrix = self.build_trees(input)
        forest_width = len(tree_matrix[0])
        forest_height = len(tree_matrix)
        for i in range(forest_height):
            for j in range(forest_width):
                if (i == 0 or j == 0 or i == forest_height-1 or j == forest_width-1):
                    scenic_score = 0
                else:
                    tree_height = tree_matrix[i][j]
                    left = self.scenic_score(tree_height, (tree_matrix[i][:j])[::-1])
                    right = self.scenic_score(tree_height, tree_matrix[i][j+1:])
                    top = self.scenic_score(tree_height, (tree_matrix.transpose()[j][:i])[::-1])
                    bottom = self.scenic_score(tree_height, tree_matrix.transpose()[j][i+1:])
                    scenic_score = left * right * top * bottom
                    highest_scenic_score = scenic_score if scenic_score > highest_scenic_score else highest_scenic_score
        print(f"The highest scenic score is: {highest_scenic_score}")
        return highest_scenic_score

    def scenic_score(self, tree_height, slice):
        scenic_score = 0
        while(len(slice) > 0):
            scenic_score += 1
            tree = slice[0]
            slice = np.delete(slice, 0, 0)
            if(tree >= tree_height):
                break
        return scenic_score



if __name__ == '__main__':
    with open("input/day8.star1") as f:
        input = f.read()
    d = day8()
    d.star1(input)
    d.star2(input)