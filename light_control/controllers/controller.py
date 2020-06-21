class Controller(object):

    def __init__(self, base_ipattern):
        self.base = base_ipattern
    
    def run_locking(self):
        while True:
            while not self.base.isDone():
                self.base.runStep()
                self.base.pause()
            self.base.reset()
            