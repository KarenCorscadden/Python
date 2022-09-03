"""
A module containing class CircularActor that models some of the basic properties and actions of
an "actor" in a game engine like Unreal Engine, specifically like a cell in the game Agar.io
See: https://agar.io/, https://en.wikipedia.org/wiki/Agar.io

The world in which CircularActors exist is a two-dimensional world with a Cartesian coordinate
system, i.e. each actor exists at a particular x/y coordinate and has a certain radius, thereby
covering a certain area of the world.
"""

__author__ = 'Karen Corscadden, a Cabrillo student for CS 12P, kmcorscadden@jeff.cis.cabrillo.edu'

import math


class CircularActor:
    """
    Represents a movable "circle" existing at a certain location in a two-dimensional world.
    """

    def __init__(self, name: str, location: tuple = (0, 0), radius: float = 5):
        """
        Constructs a new circle with a given name and radius at the specified coordinate.
        :param name: the name of the circle
        :param location: a tuple of two numeric values indicating the initial x/y coordinate
            location
        :param radius: the radius of the circle
        """

        self._name = str(name)
        if location and len(location) != 2:
            raise ValueError('Location not of length 2')
        self._x = location[0] if location else 0
        self._y = location[1] if location else 0
        self._radius = float(radius) if radius >= 0 else 5.0
        self._living = True

    def __contains__(self, other) -> bool:
        """
        Implements the "in" keyword: This actor is "in" another actor if their circles intersect.
        :param other: the other CircularActor object
        """
        return self - other is None

    def __iadd__(self, movement: tuple):
        """
        Implements the "+=" operator: Moves this actor by adding to its coordinate values.
        :param movement: a tuple of two numeric values indicating the change in x/y location
        """
        if len(movement) != 2:
            raise ValueError('Movement not of length 2')
        else:
            self._x += movement[0]
            self._y += movement[1]
        return self

    def __repr__(self) -> str:
        """
        Returns a printable representation of this actor, appropriate for eval().
        """
        if __name__ == '__main__':
            prefix = ''
        else:
            prefix = 'game_actor.'
        return f'{prefix}CircularActor(name={repr(self._name)}, location=({repr(self._x)}, '\
            f'{repr(self._y)}), radius={repr(self._radius)})'

    def __sub__(self, other):
        """
        Returns the distance between the edge of this actor and that of another.
        :param other: the other CircularActor object
        :return: the distance between the edge of this actor and that of another if the actors do
                 not intersect/overlap, otherwise None
        """
        center_distance = abs(math.sqrt((other._x - self._x) ** 2 + (other._y - self._y) ** 2))
        distance = center_distance - other._radius - self._radius
        if distance > 0:
            return distance
        else:
            return None

    def alive(self) -> bool:
        """
        Returns whether this actor is still alive,
        i.e. hasn't been "eaten" by another as a result of a collision.
        """
        return self._living

    def eat(self):
        """
        The act of "eating" increases the actor circle's radius by 1.
        """
        self._radius += 1
        return self

    def collide(self, other) -> bool:
        """
        If this actor and another intersect (i.e. have collided):
          1. If one actor has a larger size than the other, the larger will "eat" the smaller:
            The larger actor's size will increase by the smaller actor's size.
            The smaller actor will no longer be "alive", and its size will be zero.
          2. Otherwise, if the two actors have the same area, a collision will have no effect.
        :return: whether a collision occurred and one actor at the other
        """
        if self not in other:
            return False
        elif self._radius == other._radius:
            return False
        elif self._radius > other._radius:
            other._living = False
            self._radius = math.sqrt((self.size() + other.size()) / math.pi)
            other._radius = 0
            return True
        else:
            return other.collide(self)

    def location(self) -> tuple:
        """
        Returns the location of this actor.
        """
        return (self._x, self._y)

    def name(self) -> str:
        """
        Returns the name of this actor.
        """
        return self._name

    def radius(self) -> float:
        """
        Returns the radius of this actor.
        """
        return self._radius

    def size(self) -> float:
        """
        Returns the size of this actor, i.e. the area of its circle.
        """
        return math.pi * self._radius ** 2


if __name__ == '__main__':
    # Run some basic tests to make sure things work
    test1 = CircularActor('Test 1')
    assert test1.name() == 'Test 1'
    assert test1.location() == (0, 0)
    assert test1.radius() == 5
    assert abs(test1.size() - 78.540) < .001
    test2 = CircularActor('Test 2', location=(20, -50))
    assert test2.name() == 'Test 2'
    assert test2.location() == (20, -50)
    assert test2.radius() == 5
    assert abs(test2.size() - 78.540) < .001
    assert abs(test1 - test2 - 43.852) < .001
    assert test1 not in test2
    assert not test1.collide(test2)
    test1 += (20, -46)  # Move right by 20, down by 46
    assert test1 - test2 is None
    assert test1 in test2
    test2 += (0, -7)  # Move down by 7
    assert test2.location() == (20, -57)
    assert abs(test1 - test2 - 1) < .001
    assert test1 not in test2
    test2.eat()  # test2 will get bigger ...
    test2.eat()  # ... and collide with test1
    assert test1.collide(test2)  # test2 will eat test1
    assert abs(test2.size() - 232.478) < .001
