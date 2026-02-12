import logging

#Logging configuration
logging.basicConfig(
    filename = "result_man.log",
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

class Result10th:
    def __init__(self,sname,phone_num,email,passingYear_10,className):
        self.sname = sname
        self.phone_num = phone_num
        self.email = email
        self.passingYear_10 = passingYear_10
        self.className = className
    def display(self):
        # print(self.sname,self.phone_num,self.email,self.passingYear_10,self.className)
        logging.info("Name: %s \n Phone Number: %d \n Email: %s \n Year of Passing 10th : %s \n Class Name : %s\n",
                     self.sname,self.phone_num,self.email,self.passingYear_10,self.className)
    
class Result12th(Result10th):
    #constructor chaining
    def __init__(self,sname,phone_num,email,passingYear_10,className,passingYear_12,percentage_12):
        super().__init__(sname,phone_num,email,passingYear_10,className)
        self.passingYear_12 = passingYear_12
        self.percentage_12 = percentage_12
    def display(self):
        super().display()
        # logging.info("Name : %s \n Phone number: %d \n Email : %s",self.sname,self.phone_num,self.email)
        # print(self.passingYear_12,self.percentage_12)
        logging.info("Year of Passing 12th : %s \n 12th Percentage : %s",
                     self.passingYear_12,self.percentage_12)

class ResultBE(Result12th):
        #constructor chaining
    def __init__(self,sname,phone_num,email,passingYear_10,className,passingYear_12,percentage_12,branch,university,BE_perc):
        super().__init__(sname,phone_num,email,passingYear_10,className,passingYear_12,percentage_12)
        self.branch = branch
        self.university = university
        self.BE_perc = BE_perc
    def display(self):
        super().display()
        print(self.branch,self.university,self.BE_perc)
        # logging.info("Name : %s \n Phone number: %d \n Email : %s",self.sname,self.phone_num,self.email)
        logging.info("Branch Name : %s \n University Name : %s \n BE Percentage : %d",
                    self.branch,self.university,self.BE_perc)


be1 = ResultBE("Padma Sri",7396428777,"sri29@gmail.com",2020,"10A",2022,98.2,"AIML","BVRITH",90.4)
be1.display()
