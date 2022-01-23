class Game:
    def __init__(self):
        self.screen = "012345678"

    def print_screen(self):
        s = self.screen
        res = s[0:3] + "\n" + s[3:6] +"\n" + s[6:9]
        return res

    def play(self, position: int, side: str):
        s = self.screen.lower()

        if not -1 <= position < 9 : return "Invalid position - pick a number 0 - 9"
        if s[position] == "o" or s[position] == "x": return "This cell is occupised"
        self.screen = s[:position] + side + s[position + 1:]

        res, y = self.checkWin(), ""
        if res[0] == True: y += res[1] + " has won\n"
        return y + self.print_screen()

    def checkWin(self):
        def check(arr, side):
            s = self.screen.lower()
            return side == s[arr[0]] and side == s[arr[1]] and side == s[arr[2]]
        
        all, x = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [2,4,6], [0,4,8]], 0

        while x < len(all):
            if check(all[x], "o"): 
                return [True, "o"]
            elif check(all[x], "x"): 
                return [True, "x"]
            else:
                return [False]
    
    def finished(self):
        list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        
        if self.checkWin()[0] == True: return [True, "win"]
        if not any(x in self.screen for x in list): return [True, "draw"]
        return [False]

    def start_terminal_game(self):
        x = 0

        while self.finished()[0] == False:
            print(self.play(int(input("Pick a position (0 to 8): ")), "o" if x % 2 == 0 else "x"))
            res = self.finished()

            if res[0] == True: 
                if(res[1] == "draw"): 
                    print("It\'s a draw")
                break

            x += 1