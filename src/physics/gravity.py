class Gravity:

    """
    Given two masses and their
    distance, it calculates the
    Gravity force between them
    """

    def __init__(self, **options):
        """
        It calculates the gravity force
        by using the parameters given into
        options
        """
        if 'earth' in options and 'mass' in options:
            if options['earth'] is True:
                universalGravityConstant = 6.67e-11
                earthMass = 5.972e24
                self.distance = 6400
                self.mass = options['mass']
                self.gravity_force = universalGravityConstant * \
                    (earthMass * self.mass / ((self.distance)**2))
                return
        if 'mass' in options and 'second_mass' in options and 'distance' in options:
            universalGravityConstant = 6.67e-11
            self.mass = options['mass']
            self.second_mass = options['second_mass']
            self.distance = options['distance']
            self.gravity_force = universalGravityConstant * \
                (self.second_mass * self.mass / ((self.distance)**2))
            return
        raise MissingNeededParameters()


class MissingNeededParameters(Exception):

    """
    This exception is called when
    there are some missing parameters
    """

    def __init__(self):
        Exception.__init__(
            self,
            "There are some missing parameters, it is impossible to calculate the Gravity force")
