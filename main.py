import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. State Game')

screen.bgpic('blank_states_img.gif')
# counts the score of user
correct_answers = 0
# stores the correct answers of the user
user_answers = []


def main():
    global correct_answers
    locator = turtle.Turtle()
    locator.penup()
    locator.hideturtle()
    states_dataframe = pandas.read_csv('50_states.csv')
    states = list(states_dataframe.state)

    while correct_answers < 50:
        user_answer = screen.textinput(f"{correct_answers}/50 States Correct", "Name A State")
        if user_answer is None or user_answer.lower() == 'exit' or user_answer.title() not in states:
            to_be_stored = {
                'name': ['Guessed States', 'Missed States'],
                'count': [len(user_answers), len([state for state in states if states not in user_answers])],
                'states': [user_answers, [state for state in states if states not in user_answers]]
            }
            to_be_stored = pandas.DataFrame(to_be_stored)
            to_be_stored.to_csv("correct_answers", index=False,header=False)
            break

        else:
            user_answer = user_answer.title()
            if user_answer in user_answers:
                continue
            correct_answers += 1
            user_answers.append(user_answer)
            current_state = states_dataframe[states_dataframe.state == user_answer]
            locator.goto((int(current_state.x), int(current_state.y)))
            locator.write(user_answer)


main()
screen.exitonclick()
