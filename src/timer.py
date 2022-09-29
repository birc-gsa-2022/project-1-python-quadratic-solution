import time

class Clock:
    def init(self):
        pass

    def timeAlgorithm(self, algorithm, *args):
        starttime = time.perf_counter()
        algorithm(*args)
        endtime = time.perf_counter()
        return endtime-starttime

    def getAlgorithmTimeAndResult(self, algorithm, args):
        starttime = time.perf_counter()
        res = algorithm(args) 
        endtime = time.perfcounter()
        return endtime-starttime, res 

    def sleep(self, sec):
        time.sleep(sec)

    def getAverageTime(self, iterations, algorithm, *args):
        total = 0.0
        for _ in range(iterations):
            total += self.timeAlgorithm(algorithm, *args)
        return total/float(iterations)