class DiodeExperiment:
    def __init__(self):
        return
    def scan(self, start,stop,device):
        self.start = start
        self.stop = stop
        for i in range(start,stop,1):
            self.device.query(f"OUT:CH{channel} "+ f"{i}")
            return (self.device.query(f"OUT:CH{channel} "+ f"{i}"))