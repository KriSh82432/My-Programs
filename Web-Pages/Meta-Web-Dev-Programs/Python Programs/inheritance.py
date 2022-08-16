class employees():
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

class supervisors(employees):
    def __init__(self, fname, lname, password) -> None:
        super().__init__(fname, lname)
        self.password = password

class chefs(employees):
    def __init__(self, fname, lname, status) -> None:
        super().__init__(fname, lname)
        self.status = status
    def leave_request(self, days):
        return "May I take a leave for "+str(days)+" days?"
    def verify_approval(self):
        self.status = "yes"
    def deny_approval(self):
        self.status = "no"
    def check_status(self):
        if self.status == "yes":
            return self.fname+", your leave request is approved."
        else:
            return self.fname+", your leave request is denied."

subiksha = supervisors("Subiksha", "K", "Subik824@32")
krishna = chefs("Krishna", "V", None)
elan = chefs("Elanthiraivel", "K", None)

print(subiksha.password, subiksha.fname, subiksha.lname)
print(krishna.leave_request(3))
print(elan.leave_request(2))

krishna.verify_approval()
print(krishna.check_status(), elan.check_status(), sep="\n")
elan.verify_approval()
print(krishna.check_status(), elan.check_status(), sep="\n")
krishna.deny_approval()
print(krishna.check_status(), elan.check_status(), sep="\n")
