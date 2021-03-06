# HW2
# Due Date: 02/20/2021, 11:59PM

"""
### Collaboration Statement:
-Professor
-Timothy Office Hours

"""

import random


class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''

    def __init__(self, cid, cname, credits):
        # Store the ID, NAME and number of credits for a class
        self.cid = cid
        self.cname = cname
        self.credits = credits

    def __str__(self):
        # return a formatted summary of the course as a string
        return '{}({}): {}'.format(self.cid, self.credits, self.cname)

    def __repr__(self):
        # return a formatted summary of the course as a string
        return '{}({}): {}'.format(self.cid, self.credits, self.cname)

    def __eq__(self, other):
        # Determins if two objects are equal
        # Equal is defined as: when the course id of one object is the same as the course id of the other object
        if type(other) == Course:
            if self.cid == other.cid:
                return True
            else:
                return False
        else:
            return False


class Catalog:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
        >>> isinstance(C.courseOfferings['CMPSC132'], Course)
        True
    '''

    def __init__(self):
        # courseOfferings stores courses with the id as the key and the course as the value
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        # The method addCourse creates a course object with the parameters and stores it as a value in courseOfferings
        # cid is the id of the course
        # cname is the name of the course
        # credits is the number of credits the course is worth
        if cid not in self.courseOfferings:
            self.courseOfferings[cid] = Course(cid, cname, credits)
            return 'Course added successfully'
        else:
            return 'Course already added'

    def removeCourse(self, cid):
        # This method removes a course with the given id
        # cid is the id of the course to remove
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return 'Course removed successfully'
        else:
            return 'Course not found'


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, 'name',"zero credits"))
        'Invalid course'
        >>> semester.courses
        [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
    '''

    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = []

    def addCourse(self, course):
        # This method adds a course to courses if it is a valid course object
        # course is the course object to add to this semester
        if isinstance(course, Course):
            if isinstance(course.cid, str) != isinstance(course.cname, str) != isinstance(course.credits, int):
                return 'Invalid course'
            if course in self.courses:
                return 'Course already added'
            if course not in self.courses:
                self.courses.append(course)
        else:
            return 'Invalid course'

    def dropCourse(self, course):
        if type(course) == Course:
            if course in self.courses:
                self.courses.remove(course)
            else:
                return 'No such course'
        else:
            return 'Invalid course'

    @property
    def totalCredits(self):
        maxcredits = 0
        for course in self.courses:
            maxcredits += course.credits
        return maxcredits

    @property
    def isFullTime(self):
        if (self.totalCredits >= 12):
            return True
        else:
            return False

    def __str__(self):
        if len(self.courses) > 0:
            return ', '.join([course.cid for course in self.courses])
        if len(self.courses) == 0:
            return 'No courses'

    __repr__ = __str__


class Loan:
    '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''

    def __init__(self, amount):
        self.loan_id = self.__loanID  # the id for the loan
        self.amount = amount  # amount for the loan

    def __str__(self):
        return '${}'.format(self.amount)

    def __repr__(self):
        return '${}'.format(self.amount)

    @property
    def __loanID(self):
        return random.randint(10000, 99999)


class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
    '''

    def __init__(self, student):
        self.student = student
        self.balance = 0  # balance student has to pay
        self.loans = {}
        self.pricepercredit = 1000


    def __str__(self):
        return 'Name: {} \n ID: {} \n Balance: ${}'.format(self.student.name, self.student.id, self.balance)


    __repr__ = __str__


    def makePayment(self, amount):
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount):
        self.balance += amount
        return self.balance


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def get_ssn(self):
        return self.ssn

    def __str__(self):
        return 'Person({}, ***-**-{})'.format(self.name, self.get_ssn()[-4:])

    def __repr__(self):
        return 'Person({}, ***-**-{})'.format(self.name, self.get_ssn()[-4:])

    def __eq__(self, other):
        if self.get_ssn() == other.get_ssn():
            return True
        else:
            return False


class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''

    def __init__(self, name, ssn, supervisor=None):
        Person.__init__(self, name, ssn)
        self.supervisor = supervisor
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return 'Staff({}, {})'.format(self.name, self.id)

    __repr__ = __str__

    @property
    def id(self):
        ssn = self.get_ssn()[-4:]
        lowercase_first_initials = self.name.split()[0][0].lower()
        lowercase_second_initials = self.name.split()[1][0].lower()
        return '905{}{}{}'.format(lowercase_first_initials,lowercase_second_initials,ssn)

    @property
    def getSupervisor(self):
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        if type(new_supervisor) == Staff:
            self.supervisor = new_supervisor
            return 'Completed!'
        else:
            return None

    def applyHold(self, student):
        if type(student) == Student:
            student.hold = True
            return 'Compelted!'
        else:
            return None

    def removeHold(self, student):
        if type(student) == Student:
            student.hold = False
            return 'Compelted!'
        else:
            return None

    def unenrollStudent(self, student):
        if type(student) == Student:
            student.active = False
            return 'Completed!'
        else:
            return None


class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''

    def __init__(self, name, ssn, year):
        random.seed(1)
        Person.__init__(self, name, ssn)
        self.year = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()

    def __str__(self):
        return 'Student({}, {}, {})'.format(self.name, self.id, self.year)

    __repr__ = __str__

    @property
    def id(self):
        name = self.name.split()
        return '{}{}'.format(name[0][0].lower() + name[1][0].lower(), self.get_ssn()[-4:])

    def __createStudentAccount(self):
        return StudentAccount(self)

    def registerSemester(self):
        if (not self.active or self.hold):
            return 'Unsuccessful operation'
        else:
            length = len(self.semesters) + 1
            self.semesters[length] = Semester(length)
            if length in [1,2]:
                self.year = 'Freshman'
            if length in [3,4]:
                self.year = 'Sophomore'
            if length in [5,6]:
                self.year = 'Junior'
            if length >=7:
                self.year = 'Senior'




    def enrollCourse(self, cid, catalog,semester_num):#changed semester to semester_num to keep sanity
        if not self.active or self.hold:
            return 'Unsuccessful operation'
        if cid in catalog.courseOfferings:
            course = catalog.courseOfferings[cid]
            if course in self.semesters[semester_num].courses:
                return 'Course already enrolled'
            semester = self.semesters[semester_num]
            semester.addCourse(course) #adds course for the semesters to the student
            self.account.chargeAccount(self.account.pricepercredit*course.credits)
            return 'Course added successfully'
        return 'Course not found'


    def dropCourse(self, cid, semester_num):  # REVISIT
        if not self.active or self.hold:
           return 'Unsuccessful operation'
        semester = self.semesters[semester_num] #look for the semester number
        for course in semester.courses: #loop through and find the course
            if cid == course.cid: #if the couse id matches
                semester.dropCourse(course)
                return 'Course dropped successfully'
        return 'Course not found'


    def getLoan(self, amount):
        loan = Loan(amount)
        if not self.active:
            return 'Unsuccessful operation'
        if not self.semesters[(len(self.semesters))].isFullTime:
            return 'Not full-time'
        if loan.loan_id not in self.account.loans: #checks dictionary using in
            self.account.loans[loan.loan_id] = loan
            self.account.makePayment(loan.amount)







####################### STAND ALONE FUNCTION ###############################################


def createStudent(person):
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
        >>> isinstance(s, Student)
        True
    """
    return Student(person.name, person.get_ssn(), 'Freshman')

