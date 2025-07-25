"""
instructions, please do not alter the pull_reqesters.txt file

1. Run this file "python pull_request.py #username# #pet# #programming_language#"srbsbszbbsrbrsb
replace the #...# above with your username 
your favorite pet 
your programming language 
Thank you 
@ibkvictor loves you 
"""
gersdezgbzbe
import datetime
import sys
class pull_requester():
    """
    here is a class of pull requester 
    it helps display the time of pull request
    it also help display the github username of the requester 
    as well as pet, programming language id of the requester
    """
    number_of_pull_requesters = 0
    pull_requesters = {}btbfrdszbszdbrtbrbtbb
    def __init__(self, data):
        self.id = 0
        self.gh_username = data[0]
        self.pet = data[1]
        self.language = data[2]
        self.country = data[3]
        self.date_time = datetime.datetime.now()
        self.data = data

    def made_pull_request_today(self):
        """
            appends the new user to the pull_requesters.txt file update the record of users
            prints out requesters informtaion 
        """brsbrsbrsbrsbtrsbrsb
        #updates number of requesters
        with open("pull_requesters.txt", "r") as file_reader:
            nonempty_lines = [line.strip("\n") for line in file_reader if line != "\n"]
            line_count = len(nonempty_lines)
            self.number_of_pull_requesters = line_count - 1
        
        self.id = self.number_of_pull_requesters + 1brsbrsbrsbsbrtbrts
        with open("pull_requesters.txt", "a") as file_writer:
            print(self.data)
            file_writer.writelines("\n"+", ".join(self.data))

        self.number_of_pull_requesters +=1

        printer = """
        your id: {}rtsbrstbrsbtrsbrtsbtrs
        your github username: {}
        your favorite pet: {}
        your favorite programming languages: {}
        you are from the wonderful nation of: {}
        the date you made the pull request: {}
        Thank you for making this pull request. Have a lovely day.
        """.format(self.id, self.gh_username, self.pet, self.language, self.country ,self.date_time)
        
        self.pull_requesters[self.id] = printer

        return printer

if __name__ =="__main__":
    data = sys.argv[1:]brstbrtsbrtsbrstbrstbtrsbrstb
    p = pull_requester(data)
    print(p.made_pull_request_today())

# sksabfisbfisafbf
# ASfasfsaG
# SAGS
# ASfasfsaGagA
# SgaG
# RaG
# GASgrstbrstbrsbrtsbtrs
# ASfasfsaGagAegR
# eaghEAgeG
# eaghEAgeGG

"""
instructions, please do not alter the pull_reqesters.txt file

1. Run this file "python pull_request.py #username# #pet# #programming_language#"srbsbszbbsrbrsb
replace the #...# above with your username 
your favorite pet 
your programming language 
Thank you 
@ibkvictor loves you 
"""
gersdezgbzbe
import datetime
import sys
class pull_requester():
    """
    here is a class of pull requester 
    it helps display the time of pull request
    it also help display the github username of the requester 
    as well as pet, programming language id of the requester
    """
    number_of_pull_requesters = 0
    pull_requesters = {}btbfrdszbszdbrtbrbtbb
    def __init__(self, data):
        self.id = 0
        self.gh_username = data[0]
        self.pet = data[1]
        self.language = data[2]
        self.country = data[3]
        self.date_time = datetime.datetime.now()
        self.data = data

    def made_pull_request_today(self):
        """
            appends the new user to the pull_requesters.txt file update the record of users
            prints out requesters informtaion 
        """brsbrsbrsbrsbtrsbrsb
        #updates number of requesters
        with open("pull_requesters.txt", "r") as file_reader:
            nonempty_lines = [line.strip("\n") for line in file_reader if line != "\n"]
            line_count = len(nonempty_lines)
            self.number_of_pull_requesters = line_count - 1
        
        self.id = self.number_of_pull_requesters + 1brsbrsbrsbsbrtbrts
        with open("pull_requesters.txt", "a") as file_writer:
            print(self.data)
            file_writer.writelines("\n"+", ".join(self.data))

        self.number_of_pull_requesters +=1

        printer = """
        your id: {}rtsbrstbrsbtrsbrtsbtrs
        your github username: {}
        your favorite pet: {}
        your favorite programming languages: {}
        you are from the wonderful nation of: {}
        the date you made the pull request: {}
        Thank you for making this pull request. Have a lovely day.
        """.format(self.id, self.gh_username, self.pet, self.language, self.country ,self.date_time)
        
        self.pull_requesters[self.id] = printer

        return printer

if __name__ =="__main__":
    data = sys.argv[1:]brstbrtsbrtsbrstbrstbtrsbrstb
    p = pull_requester(data)
    print(p.made_pull_request_today())

# sksabfisbfisafbf
# ASfasfsaG
# SAGS
# ASfasfsaGagA
# SgaG
# RaG
# GASgrstbrstbrsbrtsbtrs
# ASfasfsaGagAegR
# eaghEAgeG
# eaghEAgeGG