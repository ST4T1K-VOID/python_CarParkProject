class Display:
    def __init__(self, id, car_park, message="", is_on=False, ):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def update(self, display_info):
        for key, value in display_info:
            print(f"{key}: {value}")
    
    def __str__(self):
        return f"Display {self.id} >>> {self.message})"
