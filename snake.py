from turtle import Screen, Turtle
import time
from enum import Enum

NORTH_HEADING = 90
EAST_HEADING = 0
SOUTH_HEADING = 270
WEST_HEADING = 180

# Snake Class
class Snake:
    def __init__(self, move_length, num_segs):
        self.starting_positions = []
        start_range = 0
        end_range = 0
        self.dictPositions = {}

        for i in range(num_segs):
            if i != 0:
                start_range = start_range - move_length
            self.starting_positions.append((start_range, end_range))
        self.segments = []
        for seg_num in range(len(self.starting_positions)):
            position = self.starting_positions[seg_num]
            self.add_segment(pos=position)
            self.dictPositions[position] = position
        print(self.dictPositions)
        self.head = self.segments[0]

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.dictPositions[seg_num] = self.segments[seg_num].position()
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != SOUTH_HEADING:
            self.head.setheading(NORTH_HEADING)

    def down(self):
        if self.head.heading() != NORTH_HEADING:
            self.head.setheading(SOUTH_HEADING)

    def left(self):
        if self.head.heading() != EAST_HEADING:
            self.head.setheading(WEST_HEADING)

    def right(self):
        if self.head.heading() != WEST_HEADING:
            self.head.setheading(EAST_HEADING)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fast")
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def detect_self_collision(self):
        return self.head.position() in self.dictPositions.values()
