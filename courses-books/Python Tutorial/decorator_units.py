import functools
import pint


def use_unit(unit):
    use_unit.ureg = pint.UnitRegistry()

    def _use_unit_decorator(func):
        @functools.wraps(func)
        def _use_unit(*args, **kwargs):
            return func(*args, **kwargs) * use_unit.ureg(unit)
        _use_unit.unit = unit
        return _use_unit
    return _use_unit_decorator


class Runner:
    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    @use_unit('meters per second')
    def average_speed(self):
        return self.distance / self.duration
    

class Plane:
    def __init__(self, distance, duration):
        self.distance = distance
        self.duration = duration

    @use_unit('km per hour')
    def average_speed(self):
        return self.distance / self.duration


bolt = Runner(100, 9.58)
osl_pit = Plane(6261, 9)

print(bolt.average_speed())
print(osl_pit.average_speed())

ratio = osl_pit.average_speed() / bolt.average_speed()
print(ratio.to_base_units())
