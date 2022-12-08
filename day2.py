class day2:
    def __init__(self) -> None:
        pass
        
    def star1(self, input):
        rounds = input.split("\n")
        total = 0
        for round in rounds:
            score = 0
            match round:
                case "A X":
                    score = 4
                case "A Y":
                    score = 8
                case "A Z":
                    score = 3
                case "B X":
                    score = 1
                case "B Y":
                    score = 5
                case "B Z":
                    score = 9
                case "C X":
                    score = 7
                case "C Y":
                    score = 2
                case "C Z":
                    score = 6
            total += score
        print(f"Total score is {total}")
        return total

    def star2(self, input):
        rounds = input.split("\n")
        total = 0
        for round in rounds:
            score = 0
            match round:
                case "A X":
                    score = 3
                case "A Y":
                    score = 4
                case "A Z":
                    score = 8
                case "B X":
                    score = 1
                case "B Y":
                    score = 5
                case "B Z":
                    score = 9
                case "C X":
                    score = 2
                case "C Y":
                    score = 6
                case "C Z":
                    score = 7
            total += score
        print(f"Total score is {total}")
        return total
        

if __name__ == '__main__':
    with open("input/day2.star1") as f:
        input = f.read()
    d2 = day2()
    d2.star1(input)
    d2.star2(input)