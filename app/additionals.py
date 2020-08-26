from colorama import Fore
import time
import math


class ProgressBar:
    _empty = "░"
    _filled = "█"

    def __init__(self, bars=25, latency=0.2, title='', success_display=True):
        self.bars = bars
        self.latency = latency
        self.title = title
        self.success_display = success_display
        self.row_ch = list(map(lambda i: self._empty, range(bars)))
        self.ch_filled = 0
        self.is_finished = False
        self.percents = 0
        self.percents_unit = math.ceil(100 / bars)

    def progress(self, percents):
        if not self.is_finished:
            if percents < 0 or percents > 100:
                raise ValueError()
            print(f"  Loading {self.percents}%   " + ''.join(self.row_ch), end='\r')
            if len(self.row_ch) > self.ch_filled:
                self.row_ch[self.ch_filled] = self._filled
            else:
                self.is_finished = True
                return
            self.ch_filled += 1
            self.percents += self.percents_unit

    def run(self):
        print('\n')
        for x in range(0, self.bars + 1):
            self.progress(x)
            time.sleep(self.latency)
        if self.success_display and self.percents >= 100:
            print(Fore.GREEN, f'\n✔ Done!          {self.title}', Fore.RESET)
        print('\n')
