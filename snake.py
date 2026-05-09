"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import (
    clear,
    done,
    hideturtle,
    listen,
    onkey,
    ontimer,
    setup,
    tracer,
    update,
)

from freegames import square, vector

# Position of the food.
food = vector(0, 0)

# Initial snake body.
snake = [vector(10, 0)]

# Initial movement direction.
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head is inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    # End game if snake hits the wall or itself.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)

    # Check if snake eats the food.
    if head == food:
        print("Snake:", len(snake))

        # Move food to a random position.
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # Remove tail segment if no food is eaten.
        snake.pop(0)

    clear()

    # Draw the snake in green.
    for body in snake:
        square(body.x, body.y, 9, "green")

    # Draw the food in red.
    square(food.x, food.y, 9, "red")

    update()

    # Repeat movement every 100 milliseconds.
    ontimer(move, 100)


# Configure the game window.
setup(420, 420, 370, 0)

# Hide default turtle cursor.
hideturtle()

# Disable automatic screen updates.
tracer(False)

# Listen for keyboard input.
listen()

# Movement controls.
onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")

# Start the game.
move()

# Keep window open.
done()
