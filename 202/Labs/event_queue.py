from time import sleep
from priority_queue import *


#An EventQueue includes a PQueue and an int (representing the time)
class EventQueue:
    def __init__(self):
        self.pqueue = empty_pqueue(event_before)   #PQueue
        self.time = 0   #int
    def __eq__(self, other):
        return type(other) == EventQueue and self.pqueue == other.pqueue and self.time == other.time
    def __repr__(self):
        return "EventQueue({}, {})".format(self.pqueue, self.time)

class Event:
    def __init__(self, func, time_delay):
        self.func = func  #the event that will be run
        self.time_delay = time_delay
    def __eq__(self, other):
        return type(other) == EventQueue and self.pqueue == other.pqueue and self.time == other.time
    def __repr__(self):
        return "EventQueue({}, {})".format(self.pqueue, self.time)


#event1, event2 --> bool
#determines if event1 comes before event2
def event_before(event1, event2):
    return event1.time_delay < event2.time_delay



#EventQueue, func, int --> EventQueue
#adds and stores the event to be scheduled in the EventQueue
def add_event(eq, func, secs):
    eq.pqueue = enqueue(eq.pqueue, Event(func, secs + eq.time))



#EventQueue --> None
#to run the events at a specific time
def run_events(eq):
    while eq.pqueue.queue != None:
        event = peek(eq.pqueue)
        while eq.time == event.time_delay:
            event_tuple = dequeue(eq.pqueue)
            eq.pqueue = event_tuple[1]
            run_event = event_tuple[0]
            run_event.func(eq)
            event = peek(eq.pqueue)
        sleep(1)
        eq.time += 1
