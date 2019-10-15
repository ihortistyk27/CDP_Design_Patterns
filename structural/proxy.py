import time


class Producer:

    def produce(self):
        print("Working hard")

    def meet(self):
        print("Producer has time to meet you now!")


class Proxy:

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Proxy Checking whether Producer is available")

        if self.occupied == "No":
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")


# Instantiate the Proxy
proxy = Proxy()

# Make the Proxy: Artist produce until Producer is available
proxy.produce()
# Change the state to occupied
proxy.occupied = "Yes"

# Make the Producer produce
proxy.produce()



