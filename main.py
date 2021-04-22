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
        user_answer = screen.textinput(f"{correct_answers}/50 States Correct", "Name A State").title()

        if user_answer is None or user_answer == 'exit':
            to_be_stored = {
                'name': 'States',
                'states': user_answers
            }
            to_be_stored = pandas.DataFrame(to_be_stored)
            to_be_stored.to_csv('correct_answers.csv')
            break
        elif user_answer in states:
            if user_answer in user_answers:
                continue
            correct_answers += 1
            user_answers.append(user_answer)
            current_state = states_dataframe[states_dataframe.state == user_answer]
            locator.goto((int(current_state.x), int(current_state.y)))
            locator.write(user_answer)
        else:
            break


main()
screen.exitonclick()
