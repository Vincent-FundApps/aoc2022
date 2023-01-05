import numpy as np
class day9:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        number_of_tail_positions = 0
        instructions = input.split("\n")
        head_tail_coordinates = {}
        number_of_knots = 2
        for i in range(number_of_knots):
            head_tail_coordinates[i] = [0, 0]
        tail_coordinates = set()
        for instruction in instructions:
            coordinates = self.move_knots(head_tail_coordinates, instruction, tail_coordinates)
            head_tail_coordinates = coordinates[0]
            tail_coordinates = coordinates[1]
        number_of_tail_positions = len(tail_coordinates)
        print(f"There are {number_of_tail_positions} positions for last knot")
        return number_of_tail_positions
    
    def follow_head(self, current_head_coordinates, current_tail_coordinates):
        move_x = current_head_coordinates[0]-current_tail_coordinates[0]
        move_y = current_head_coordinates[1]-current_tail_coordinates[1]
        if(abs(move_x)>1):
            if (move_y == 0):
                current_tail_coordinates[0] = current_tail_coordinates[0] + move_x//abs(move_x)
            else:
                current_tail_coordinates[0] = current_tail_coordinates[0] + move_x//abs(move_x)
                current_tail_coordinates[1] = current_tail_coordinates[1] + move_y//abs(move_y)
        elif(abs(move_y)>1):
            if (move_x == 0):
                current_tail_coordinates[1] = current_tail_coordinates[1] + move_y//abs(move_y)
            else:
                current_tail_coordinates[1] = current_tail_coordinates[1] + move_y//abs(move_y)
                current_tail_coordinates[0] = current_tail_coordinates[0] + move_x//abs(move_x)
        return current_tail_coordinates

    def move_knots (self, head_tail_coordinates, instruction, last_tail_coordinates):
            direction = instruction.split(" ")[0]
            moves = int(instruction.split(" ")[1])
            for i in range(moves):
                match direction:
                    case "R":
                        head_tail_coordinates[0][1] += 1
                    case "L":
                        head_tail_coordinates[0][1] -= 1
                    case "U":
                        head_tail_coordinates[0][0] += 1
                    case "D":
                        head_tail_coordinates[0][0] -= 1
                for j in range(len(head_tail_coordinates)-1):
                    head_tail_coordinates[j+1] = self.follow_head(head_tail_coordinates[j], head_tail_coordinates[j+1])
                last_tail_coordinates.add(tuple(head_tail_coordinates[len(head_tail_coordinates)-1]))
            return ([head_tail_coordinates, last_tail_coordinates])    

    def star2(self, input):
        instructions = input.split("\n")
        head_tail_coordinates = {}
        number_of_knots = 10
        for i in range(number_of_knots):
            head_tail_coordinates[i] = [0, 0]
        tail_coordinates = set()
        for instruction in instructions:
            coordinates = self.move_knots(head_tail_coordinates, instruction, tail_coordinates)
            head_tail_coordinates = coordinates[0]
            tail_coordinates = coordinates[1]
        number_of_tail_positions = len(tail_coordinates)
        print(f"There are {number_of_tail_positions} positions for last knot")
        return number_of_tail_positions


if __name__ == '__main__':
    with open("input/day9.star1") as f:
        input = f.read()
    d = day9()
    d.star1(input)
    d.star2(input)