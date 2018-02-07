class Call(object):
    def __init__(self, c_id, caller_name, caller_phone_number, time_of_call, reason):
        self.c_id = c_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason = reason
    def display(self):
        print ("ID: ", self.c_id)
        print ("Name: ", self.caller_name)
        print ("Phone: ", self.caller_phone_number)
        print ("Time: ", self.time_of_call)
        print ("Resaon: ", self.reason)
        
class CallCenter(object):
    def __init__(self, calls = None):
        if calls == None:
            self.calls = []
            self.queue_size = 0
    def addCall(self, new_call):
        self.calls.append(new_call)
        self.queue_size = len(self.calls)
        return self
    def removeCall(self, call):
        self.calls.remove(call)
        self.queue_size = len(self.calls)
        return self
    def removeCallByNumber(self, callNumber):
        for key in self.calls:
            if key.caller_phone_number == callNumber:
                self.calls.remove(key)
        self.queue_size = len(self.calls)
        return self
    def info(self):
        print("The call query: " + str(self.queue_size))
        for call in self.calls:
            print("Caller Name: " + call.caller_name)
            print("Call number: " + call.caller_phone_number)
        return self


call1 = Call(1,"Anton Test","443-827-0000","02/07/18 09:07am","Technical support")
call2 = Call(2,"John Deer","410-560-1111","02/07/18 09:10am","Billing")
call3 = Call(3,"Mark Sams","xxx-xxx-xxxx","02/07/18 09:30am","New Order")


center = CallCenter()
center.addCall(call1)
center.addCall(call2)
center.addCall(call3)

center.removeCallByNumber("235-673-6437")
center.info()