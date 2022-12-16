import re
from queue import LifoQueue
class day6:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        length_of_stream = len(input)
        first_marker = 0
        i=3
        while((i <= length_of_stream) and (first_marker == 0)):
            four_elements = []
            for j in range(4):
                four_elements.append(input[i-j])            
            if(len(set(four_elements)) == 4):
                first_marker = i+1
            i += 1
        print(f"The first marker is {first_marker}")
        return first_marker

    def star2(self, input):
        length_of_stream = len(input)
        first_marker = 0
        i=13
        while((i <= length_of_stream) and (first_marker == 0)):
            fourteen_elements = []
            for j in range(14):
                fourteen_elements.append(input[i-j])
            if(len(set(fourteen_elements)) == 14):
                first_marker = i+1
            i += 1
        print(f"The first marker is {first_marker}")
        return first_marker  


if __name__ == '__main__':
    with open("input/day6.star1") as f:
        input = f.read()
    d = day6()
    d.star1(input)
    d.star2(input)