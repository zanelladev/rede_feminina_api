# create a firebase instance factory


class FirebaseFactory:
    def __init__(self):
        self.firebase = None

    def get_firebase(self):
        if self.firebase is None:
            self.firebase = Firebase()
        return self.firebase
