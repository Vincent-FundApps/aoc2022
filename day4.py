import re
class day4:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        pairs = 0
        for pair_of_elves in input.split("\n"):
            sections = list(map(int, re.split('-|,',pair_of_elves)))
            if (sections[0] <= sections[2]) and (sections[1] >= sections[3]):
                    pairs += 1
            if (sections[0] > sections[2]) and (sections[1] <= sections[3]):
                    pairs +=1
        print(f"There are {pairs} pairs")
        return pairs

    def star2(self, input):
        overlaps = 0
        for pair_of_elves in input.split("\n"):
            sections = list(map(int, re.split('-|,',pair_of_elves)))
            if((sections[1] <= sections[3] and sections[1] >= sections[2]) or (sections[3] <= sections[1] and sections[3] >= sections[0])):
                overlaps += 1
                pass

        print(f"There are {overlaps} pairs that overlap")
        return overlaps

if __name__ == '__main__':
    with open("input/day4.star1") as f:
        input = f.read()
    d = day4()
    d.star1(input)
    d.star2(input)