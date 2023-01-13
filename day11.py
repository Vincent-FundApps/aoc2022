import numpy as np
import operator

class day11:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        monkey_register = self.build_monkey_register(input)
        for _ in range(20):
            for i in range(len(monkey_register)):
                for _ in range(len(monkey_register[i]['starting_items'])):
                    old = monkey_register[i]['starting_items'].pop()
                    new = eval(monkey_register[i]['operation'])
                    new = new // 3
                    next_monkey = monkey_register[i]['If true'] if new%monkey_register[i]['divisible'] == 0 else monkey_register[i]['If false']
                    monkey_register[next_monkey]['starting_items'].append(new)
                    monkey_register[i]['inspected_items'] +=1
        monkey_business = []
        for k in sorted(monkey_register, key = lambda x: monkey_register[x]['inspected_items'], reverse=True):
            monkey_register[k] = monkey_register.pop(k)
            monkey_business.append(monkey_register[k]['inspected_items'])
        print(f"Monkey business is {monkey_business[0]*monkey_business[1]}")
        return monkey_business[0]*monkey_business[1]

    def build_monkey_register(self, input):
        monkey_register = {}
        monkeys = input.split("\n\n")
        for monkey in monkeys:
            monkey_info = monkey.split("\n")
            starting_items = []
            for element in monkey_info[1].split("Starting items: ")[1].split(", "):
                starting_items.append(int(element))
            monkey_register.update({
                int(monkey_info[0].split(" ")[1].split(":")[0]):{
                'starting_items':starting_items,
                'operation':monkey_info[2].split("Operation: new = ")[1],
                'divisible':int(monkey_info[3].split("Test: divisible by ")[1]),
                'If true':int(monkey_info[4].split("If true: throw to monkey ")[1]),
                'If false':int(monkey_info[5].split("If false: throw to monkey ")[1]),
                'inspected_items':0}
            })
        return monkey_register

    def star2(self, input):
        monkey_register = self.build_monkey_register(input)
        lcm = self.find_lcm(monkey_register)
        for z in range(10000):
            for i in range(len(monkey_register)):
                for _ in range(len(monkey_register[i]['starting_items'])):
                    old = (monkey_register[i]['starting_items'].pop())%lcm
                    new = eval(monkey_register[i]['operation'])
                    next_monkey = monkey_register[i]['If true'] if new%monkey_register[i]['divisible'] == 0 else monkey_register[i]['If false']
                    monkey_register[next_monkey]['starting_items'].append(new)
                    monkey_register[i]['inspected_items'] +=1
        monkey_business = []
        for k in sorted(monkey_register, key = lambda x: monkey_register[x]['inspected_items'], reverse=True):
            monkey_register[k] = monkey_register.pop(k)
            monkey_business.append(monkey_register[k]['inspected_items'])
        print(f"Monkey business is {monkey_business[0]*monkey_business[1]}")
        return monkey_business[0]*monkey_business[1]
    def find_lcm(self, monkey_register):
        divisible_array = []
        for i in range(len(monkey_register)):
            divisible_array.append(monkey_register[i]['divisible'])
        lcm = 1
        for divisible in divisible_array:
            lcm = lcm * divisible
        return lcm 

if __name__ == '__main__':
    with open("input/day11.star1") as f:
        input = f.read()
    d = day11()
    d.star1(input)
    d.star2(input)