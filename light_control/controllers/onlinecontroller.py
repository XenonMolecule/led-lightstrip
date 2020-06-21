from controller import Controller

class OnlineController(Controller):

    def __init__(self, base_ipattern, pattern_map, connection):
        super(OnlineController, self).__init__(base_ipattern)
        self.pattern_map = pattern_map
        self.connection = connection
        self.curr_patt = self.base

    def run_locking(self):
        while True:
            next_patt = self.connection.getNextPattern()
            # Switch pattern if the user queued up a new one
            if next_patt != 'base':
                self.curr_patt.reset()
                self.curr_patt = self.pattern_map.get(next_patt, self.base)
                self.connection.setNextPattern('base')
                self.curr_patt.reset()
            else:
                self.last_patt_str = next_patt
            # If not done move to the next step of the pattern
            if not self.curr_patt.isDone():
                self.curr_patt.runStep()
            # If we are done either reset this pattern or switch back to default
            else:
                if not self.connection.shouldHoldPattern():
                    self.curr_patt = self.base
                self.curr_patt.reset()
            self.curr_patt.pause()