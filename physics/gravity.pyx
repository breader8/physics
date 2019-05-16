# This file is a part of physics
#
# Copyright (c) 2019 The physics Authors (see AUTHORS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
physics.gravity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
It contains the Gravity class.

It could be used to get the gravity force of
some objects.
"""

cdef float GravitationalConstant = 6.67408e-11
cdef float Earth = 5.9722e24
cdef float EarthRadius = 6371.0

cpdef float calculate_gravity(float mass, float second_mass = Earth, float distance = EarthRadius):
    """
    Given two masses and their
    distance, it calculates the
    Gravity force between them.
    
    :param mass: The first mass.
    :param second_mass: The second mass. By default, the earth mass is used.
    :param distance: The distance between the two masses. By the default, the radius of the earth is used.
    :type mass: float
    :type second_mass: float
    :type distance: float
    :returns: The gravity force.
    :rtype: float
    """
    return GravitationalConstant * mass * second_mass / distance**2
