import matplotlib.pylab as plt

class Route():

    def __init__(self, points):
        self.points = self.set_points(points)

    def set_points(self, points):
        return [complex(point[0], point[1]) for point in points]

    def get_points(self):
        return [(point.real, point.imag) for point in self.points]

    def get_total_distance(self):
        distance = 0
        for k in range(1, len(self.points)):
            p1 = self.points[k-1]
            p2 = self.points[k]
            distance += abs(p2 - p1)
        return distance

    def get_aerial_distance(self):
        return abs(self.points[0] - self.points[-1])

    def __repr__(self):
        return "Total distance: {}, aerial distance: {}".format(
            self.get_total_distance(),
            self.get_aerial_distance(),
        )

    def plot(self):
        x = [i[0] for i in self.get_points()]
        y = [i[1] for i in self.get_points()]
        plt.title("Route")
        plt.plot(x, y, "b", label=f"Total distance:  {self.get_total_distance()} km")
        plt.plot(x, y, "or")
        plt.plot((x[0], x[-1]), (y[0], y[-1]) , "g", label=f"Aerial distance: {self.get_aerial_distance()} km")
        plt.legend()
        plt.xlabel("x [km]")
        plt.ylabel("y [km]")
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    p = [(8, 10), (6, -3), (8, -10), (-1, 5), (-5, -4), (10, -5), (15, -7)]
    r = Route(p)
    r.plot()
    print(r)
    print(r.get_points())