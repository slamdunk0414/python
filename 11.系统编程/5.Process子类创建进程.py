from multiprocessing import Process

class Process_class(Process):

    def run(self):

        print('1')

p = Process_class()

p.start()

