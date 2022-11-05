import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()


class Text(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")

    def go_to_map(self, missed_states):
        self.goto(0, 0)
        text.write("Here are the states you missed...", align="center", font=("Arial", 24, "normal"))
        time.sleep(2)
        text.clear()
        for state in missed_states.state:
            x_cor = int(missed_states[missed_states.state == state].x)
            y_cor = int(missed_states[missed_states.state == state].y)

            with open("red_states.txt") as red_states:
                for line in red_states:
                    if line.strip() == state:
                        text.color("red")

            with open("blue_states.txt") as blue_states:
                for line in blue_states:
                    if line.strip() == state:
                        text.color("blue")
            text.goto(x_cor, y_cor)
            text.write(state)


def get_missed_states():
    missing_states = pandas.read_csv("50_states.csv")
    for state in correct_guesses:
        delete_row = missing_states[missing_states.state == state].index
        # drop a specific row in dataframe
        missing_states = missing_states.drop(delete_row)
        missing_states.to_csv("states_to_learn.csv", index=False)
    return missing_states


correct_guesses = []
while len(correct_guesses) < 50:
    text = Text()
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(states)} States Correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missed_states = get_missed_states()
        time.sleep(1)
        display_missing_states = screen.textinput(title=f"{len(correct_guesses)}/{len(states)} States Correct",
                                                  prompt="Would you like to see the states you've missed? "
                                                         "Type 'y' or 'n'").lower()
        if display_missing_states == 'y':
            text = Text()
            text.go_to_map(missed_states)
            break
        else:
            text.goto(0, 0)
            text.write("Goodbye", align="center", font=("Arial", 24, "normal"))
            break

    if answer_state in states and answer_state not in correct_guesses:
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        text.goto(x, y)
        text.write(arg=answer_state, align="center")
        correct_guesses.append(answer_state)

turtle.mainloop()
