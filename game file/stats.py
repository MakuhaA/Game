class Stat():
    # отслеживание статистики

    def __init__(self):
        # инициализирует статистику
        self.reset_stat()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.score_high = int(f.readline())

    def reset_stat(self):
        # статистика, изменяющаяся во время игры
        self.live = 3
        self.score = 0
