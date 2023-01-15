class Stat():

    def __init__(self):
        self.reset_stat()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.score_high = int(f.readline())

    def reset_stat(self):
        self.live = 3
        self.score = 0
