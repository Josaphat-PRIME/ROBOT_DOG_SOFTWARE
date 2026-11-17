
import time


def interpolate_xz(start, end, duration=1.0, frequency=50):

    x0, z0 = start
    x1, z1 = end

    steps = max(1, int(duration * frequency))

    for i in range(steps + 1):

        t = i / steps

        # Interpolation lineaire
        x = x0 + t * (x1 - x0)
        z = z0 + t * (z1 - z0)

        yield x, z

        if i < steps:
            time.sleep(1 / frequency)
