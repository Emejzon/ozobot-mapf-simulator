import math
import pygame

from ozobotmapf.graphics.shapes import Point, Rectangle
from ozobotmapf.utils.constants import Colors, Directions


class Drawable:
    """Abstract class wrapping several pyGame objects that can be drawn to the screen."""

    def draw(self, screen):
        """Method supporting drawing to the screen."""
        pass


class Line(Drawable):
    def __init__(self, start: Point, end: Point, width: int = 1, color=Colors.BLACK):
        self.start, self.end = Point(*start.to_list()), Point(*end.to_list())
        self.width = width
        self.color = color
        self.__elongate()

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)

    def __elongate(self):
        if self.start.x == self.end.x:  # line is vertical
            if self.start.y < self.end.y:
                self.start.y = self.start.y - math.floor(self.width / 2 - 1)
                self.end.y = self.end.y + math.floor(self.width / 2 - 1)
            else:
                self.start.y = self.start.y + math.floor(self.width / 2 - 1)
                self.end.y = self.end.y - math.floor(self.width / 2 - 1)
        elif self.start.y == self.end.y:  # line is horizontal
            if self.start.x < self.end.x:
                self.start.x = self.start.x - math.floor(self.width / 2 - 1)
                self.end.x = self.end.x + math.floor(self.width / 2 - 1)
            else:
                self.start.x = self.start.x + math.floor(self.width / 2 - 1)
                self.end.x = self.end.x - math.floor(self.width / 2 - 1)


class Rect(Drawable):
    def __init__(self, rectangle: Rectangle, width: int = 1, color=Colors.BLACK):
        self.rect = Rectangle(*rectangle.to_list())
        self.width = width
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, self.width)


class FillRect(Drawable):
    def __init__(self, rectangle: Rectangle, color=Colors.WHITE):
        self.rect = Rectangle(*rectangle.to_list())
        self.color = color

    def draw(self, screen):
        screen.fill(self.color, self.rect)


class FillChecker(Drawable):
    def __init__(self, rectangle: Rectangle, color1=Colors.WHITE, color2=Colors.BLACK, splits=10):
        self.rect = Rectangle(*rectangle.to_list())
        self.colors = [color1, color2]
        self.splits = splits
        self.part_width = rectangle.width / splits
        self.part_height = rectangle.height / splits

    def draw(self, screen):
        current_color = 0
        for part_x in range(self.splits):
            for part_y in range(self.splits):
                x = self.rect.origin.x + part_x * self.part_width
                y = self.rect.origin.y + part_y * self.part_height
                screen.fill(self.colors[current_color], [x, y, self.part_width, self.part_height])
                current_color = 1 - current_color
            current_color = 1 - current_color


class FullArrow(Drawable):
    def __init__(self, center: Point, direction: Directions, width: int, color=Colors.BLACK):
        self.corners = self.__compute_corners(center, direction, width)
        self.color = color

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.corners)

    @staticmethod
    def __compute_corners(center: Point, direction: Directions, width: int):
        half = int(width / 2)
        if direction == Directions.UP:
            return [center.moved(half, half), center.moved(-half, half), center.moved(0, -half)]
        elif direction == Directions.RIGHT:
            return [center.moved(-half, half), center.moved(-half, -half), center.moved(half, 0)]
        elif direction == Directions.DOWN:
            return [center.moved(-half, -half), center.moved(half, -half), center.moved(0, half)]
        elif direction == Directions.LEFT:
            return [center.moved(half, -half), center.moved(half, half), center.moved(-half, 0)]


class Arc(Drawable):
    def __init__(self, bounding_box: Rectangle, start_angle: int, end_angle: int, width: int = 1, color=Colors.BLACK):
        self.bounding_box = bounding_box
        self.starting_angle = math.radians(start_angle)
        self.end_angle = math.radians(end_angle)
        self.width = width
        self.color = color

    def draw(self, screen):
        pygame.draw.arc(screen, self.color, self.bounding_box, self.starting_angle, self.end_angle, self.width)


class Circle(Drawable):
    def __init__(self, origin: Point, radius: int, color=Colors.BLACK):
        self.origin = origin
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.origin, self.radius)


class DrawableGroup(Drawable):
    def __init__(self):
        self.list = []

    def draw(self, screen):
        for drawable in self.list:
            drawable.draw(screen)

    def add_drawable(self, drawable: Drawable):
        self.list.append(drawable)

    def clear(self):
        self.list.clear()
