class Student:

    def __init__(self, name, categories={}):
        """
        Makes an object that represents a student
        name=the name of the student
        categories=empty dictionary by default otherwise categories with ranks
        """

        self.name=name
        self.cats=categories

    def addRank(self, cat, value):
        """
        Adds another rank or updates a current in rank in the student's dictionary
        cat=The name of the category to add or update
        value=The rank in the category that is being added or updated
        """

        self.cats[cat]=value

    def getName(self):
        """
        Returns the name of the student
        """

        return self.name

    def getCategories(self):
        """
        Returns the dictionary of categories and ranks
        """

        return self.cats

    def __str__(self):
        """
        Returns the name with all of the student's categories and scores as a string
        """

        return self.name + " " + " = " + " "+str(self.cats)
