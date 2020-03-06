import math
import pygame

from ozobotmapf.graphics.shapes import Point, Rectangle
from ozobotmapf.utils.constants import Colors


class Drawable:
    def draw(self, screen):
        pass


class Line(Drawable):
    def __init__(self, start, end, width=1, color=Colors.BLACK):
        self.start, self.end = Point(*start.to_list()), Point(*end.to_list())
        self.width = width
        self.color = color
        self.__elongate()

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start, self.end, self.width)

    def __elongate(self):
        if self.start.x == self.end.x:  # line is vertical
            if self.start.y < self.end.y:
                self.start.y = self.start.y - math.floor(self.width / 2)
                self.end.y = self.end.y + math.floor(self.width / 2)
            else:
                self.start.y = self.start.y + math.floor(self.width / 2)
                self.end.y = self.end.y - math.floor(self.width / 2)
        elif self.start.y == self.end.y:  # line is horizontal
            if self.start.x < self.end.x:
                self.start.x = self.start.x - math.floor(self.width / 2)
                self.end.x = self.end.x + math.floor(self.width / 2)
            else:
                self.start.x = self.start.x + math.floor(self.width / 2)
                self.end.x = self.end.x - math.floor(self.width / 2)


class Rect(Drawable):
    def __init__(self, rectangle, width=1, color=Colors.BLACK):
        self.rect = Rectangle(*rectangle.to_list())
        self.width = width
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, self.width)


class FillRect(Drawable):
    def __init__(self, rectangle, color=Colors.WHITE):
        self.rect = Rectangle(*rectangle.to_list())
        self.color = color

    def draw(self, screen):
        screen.fill(self.color, self.rect)


class FillChecker(Drawable):
    def __init__(self, rectangle, color1=Colors.WHITE, color2=Colors.BLACK, splits=10):
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