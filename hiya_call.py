from collections import defaultdict

# assuming that each person has unique name
# assuming that one person cannot be a part of multiple different calls at once
# assuming a person must either not currently be on a call or must hangup before starting/accepting a new call
# assuming hangup time for call i is later than call time for call i

class CallEvent:
    def __init__(self, from_person, to_person, timestamp):
        self.from_person = from_person
        self.to_person = to_person
        self.timestamp = timestamp

class Call(CallEvent):
    pass

class Hangup(CallEvent):
    pass

def short_calls(phone_call_traffic):
    res = [] # final result list
    average_length = defaultdict(list) # map to keep track of people's call lengths
    ongoing_calls = {}  # map to keep track of people that are on call and the time it started at
    for event in phone_call_traffic:
        if isinstance(event, Call):
            ongoing_calls[event.from_person] = event.timestamp
        elif isinstance(event, Hangup):
            if event.from_person in ongoing_calls:
                length = event.timestamp - ongoing_calls[event.from_person]
                average_length[event.from_person].append(length)
                ongoing_calls.pop(event.from_person)
            elif event.to_person in ongoing_calls:
                length = event.timestamp - ongoing_calls[event.to_person]
                average_length[event.to_person].append(length)
                ongoing_calls.pop(event.to_person)
    for key, value in average_length.items():
        avg = sum(value)/len(value)
        if avg < 5:
            res.append(key)
    return res


# test case
phone_call_traffic = []
c1 = Call("Bob", "Alice", 1711132463)
phone_call_traffic.append(c1)
c2 = Call("Carl", "Doug", 1711132465)
phone_call_traffic.append(c2)
h1 = Hangup("Alice", "Bob", 1711132467)
phone_call_traffic.append(h1)
c3 = Call("Ed", "Frank", 1711132481)
phone_call_traffic.append(c3)
h2 = Hangup("Carl", "Doug", 1711132482)
phone_call_traffic.append(h2)
c4 = Call("Bob", "Doug", 1711132483)
phone_call_traffic.append(c4)
h3 = Hangup("Doug", "Bob", 1711132484)
phone_call_traffic.append(h3)
h4 = Hangup("Ed", "Frank", 1711132501)
phone_call_traffic.append(h4)

sc = short_calls(phone_call_traffic)
print(sc)