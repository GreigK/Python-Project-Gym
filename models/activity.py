class Activity:
    def __init__(self, name, activity_type, id=None):
        self.name = name
        self.activity_type = activity_type
        self.id = id


    def check_activity_name(self):
        return self.name