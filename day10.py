import numpy as np
class day10:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        register = self.signal_strengths(input)
        sum_of_signal_strength = 0
        # print(register)
        nb_of_values = (len(register)-20)//40+1
        # print(nb_of_values)
        for i in range(nb_of_values):
            sum_of_signal_strength += register[20+i*40]*(20+i*40)
            # print(register[20+i*40]*(20+i*40))
        print(f"Sum of signal strengths are: {sum_of_signal_strength}")
        return sum_of_signal_strength

    def signal_strengths(self, input):
        instructions = input.split("\n")
        cycle = 1
        x = 1
        register = {}
        for instruction in instructions:
            if instruction[0] == "n":
                register.update({cycle:x})
                cycle += 1
            else:
                v = int(instruction.split(" ")[1])
                for i in range(2):
                    register.update({cycle:x})
                    cycle += 1
                x += v
        return register
    
    def star2(self, input):
        register = self.signal_strengths(input)
        # instructions = input.split("\n")
        x = 1
        CRT_Screen = ""
        # print(register)
        for i in range(len(register)):
            x = register[i+1]
            sprite = [x-1, x, x+1]
            pixel = "#" if ((i%40) in sprite) else "."
            CRT_Screen += pixel
            if(i%40 == 39):
                CRT_Screen += "\n"
        print(CRT_Screen)
        return CRT_Screen

if __name__ == '__main__':
    with open("input/day10.star1") as f:
        input = f.read()
    d = day10()
    d.star1(input)
    d.star2(input)