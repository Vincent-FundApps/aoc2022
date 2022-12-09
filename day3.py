class day3:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        priorities = 0
        for rucksack in input.split("\n"):
            inter=''.join(set(rucksack[:len(rucksack)//2]).intersection(rucksack[len(rucksack)//2:]))
            if (inter.islower()):
                priorities += ord(inter)-97+1
            else:
                priorities += ord(inter)-65+1+26
        print(f"The sum of priorities is {priorities}")
        return priorities

    def star2(self, input):
        priorities = 0
        rucksacks = input.split("\n")
        i=len(rucksacks)
        while(i>0):
            inter = ''.join(set((rucksacks[i-1])).intersection(set((rucksacks[i-2])), set((rucksacks[i-3]))))
            if (inter.islower()):
                priorities += ord(inter)-97+1
            else:
                priorities += ord(inter)-65+1+26
            i-=3
        print(f"The sum of priorities is {priorities}")
        return priorities

if __name__ == '__main__':
    with open("input/day3.star1") as f:
        input = f.read()
    d3 = day3()
    d3.star1(input)
    d3.star2(input)