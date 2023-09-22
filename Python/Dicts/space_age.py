class SpaceAge:
    period = {'earth': 1, 'mercury': 0.2408467, 'venus': 0.61519726,
              'mars': 1.8808158, 'jupiter': 11.862615, 'saturn': 29.447498,
              'uranus': 84.016846, 'neptune': 164.79132}

    def __init__(self, seconds):
        self.seconds = seconds

    def transform(self, planet):
        return round(self.seconds / (31557600.0 * self.period[planet]), 2)

    def on_earth(self):
        return self.transform('earth')

    def on_mercury(self):
        return self.transform('mercury')

    def on_venus(self):
        return self.transform('venus')

    def on_mars(self):
        return self.transform('mars')

    def on_jupiter(self):
        return self.transform('jupiter')

    def on_saturn(self):
        return self.transform('saturn')

    def on_uranus(self):
        return self.transform('uranus')

    def on_neptune(self):
        return self.transform('neptune')
