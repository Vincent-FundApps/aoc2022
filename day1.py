class day1:
    def __init__(self) -> None:
        self.ranked_elves = {}
        
    def star1(self, input):
        elves = input.split("\n\n")
        max_calories = 0
        happiest_elf = 0
        i = 0
        for elf in elves:
            calories = elf.split("\n")
            sum_calories = sum(map(int, calories))
            self.ranked_elves[i]=sum_calories
            if sum_calories > max_calories:
                max_calories = sum_calories
                happiest_elf = i+1
            i+=1
        print (f"The elf carrying the most calories is {happiest_elf} with {max_calories} calories")
        return max_calories

    def star2(self):
        keys = sorted(self.ranked_elves.items(), key=lambda item: item[1], reverse=True)[:3]
        top3_calories = sum(key[1] for key in keys)
        print (f"The sum of top 3 calories carried by elves are: {top3_calories}")
        return top3_calories
        

if __name__ == '__main__':
    with open("input/day1.star1") as f:
        input = f.read()
    d1 = day1()
    d1.star1(input)
    d1.star2()