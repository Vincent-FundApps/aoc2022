import re
from queue import LifoQueue
class day5:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        stacks = self.initialise_stacks_of_crates(input)
        instructions = input.split('\n\n')[1]
        stacks = self.move_crates(stacks, instructions)
        top_crates = self.get_top_crates(stacks)
        print(f"The list of top crates is {top_crates}")
        return top_crates
        

    def initialise_stacks_of_crates(self, input):
        crates = input.split('\n\n')[0].split('\n')
        nb_of_stacks = len(crates[0])//4+1
        stacks = []
        for i in range(nb_of_stacks):
            stack = []
            stacks.append(stack)
        crates.pop() #Remove the line with numbers
        crates.reverse() #Start from the bottom
        for line_of_crates in crates:
            for i in range(nb_of_stacks):
                crate_name = line_of_crates[i*4+1]
                if crate_name != ' ':
                    stacks[i].append(crate_name)
        return stacks
    
    def move_crates(self, stacks, instructions):
        for instruction in instructions.split('\n'):
            movements = instruction.split(' ')
            popped_crates = []
            for i in range(int(movements[1])):
                popped_crates.append(stacks[(int(movements[3])-1)].pop())
            stacks[(int(movements[5])-1)].extend(popped_crates)
        return stacks
    
    def move_crates_9001(self, stacks, instructions):
        for instruction in instructions.split('\n'):
            movements = instruction.split(' ')
            popped_crates = []
            for i in range(int(movements[1])):
                popped_crates.append(stacks[(int(movements[3])-1)].pop())
            popped_crates.reverse()
            stacks[(int(movements[5])-1)].extend(popped_crates)
        return stacks

    def get_top_crates(self, stacks):
        top_crates = ""
        for stack in stacks:
            top_crates += stack.pop()
        return top_crates

    def star2(self, input):
        stacks = self.initialise_stacks_of_crates(input)
        instructions = input.split('\n\n')[1]
        stacks = self.move_crates_9001(stacks, instructions)
        top_crates = self.get_top_crates(stacks)
        print(f"The list of top crates is {top_crates}")
        return top_crates

if __name__ == '__main__':
    with open("input/day5.star1") as f:
        input = f.read()
    d = day5()
    d.star1(input)
    d.star2(input)