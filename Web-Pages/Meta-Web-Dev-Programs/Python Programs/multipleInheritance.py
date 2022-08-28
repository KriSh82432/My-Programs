class supervisors():
    def __init__(self, fname, lname, password) -> None:
        self.fnmae = fname 
        self.lname = lname
        self.password = password


class chefs():
    def __init__(self, fname, lname, password) -> None:
        self.fname = fname
        self.lname = lname
        self.password = password
    def leave_request(self, days):
        return "May I take a leave for "+str(days)+" days?"
    def verify_approval(self):
        self.password = "yes"
    def deny_approval(self):
        self.password = "no"
    def check_status(self):
        if self.password == "yes":
            return self.fname+", your leave request is approved."
        else:
            return self.fname+", your leave request is denied."

class employees(chefs, supervisors):
    def __init__(self, fname, lname, password, id) -> None:
        super().__init__(fname, lname, password)
        self.id = id


subiksha = employees("Subiksha", "K","Subik824@32", "12345")
print(subiksha.password)
elan = employees("Elan", "K", None, "12346")
elan.verify_approval()
print(elan.check_status())
print(elan.id)