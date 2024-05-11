class UserEntity:
    def __init__(self, road: str, neighborhood: str, city: str):
        if road is None or neighborhood is None or city is None:
            raise ValueError("road, neighborhood, city are required.")
        self.road = road
        self.neighborhood = neighborhood
        self.city = city
