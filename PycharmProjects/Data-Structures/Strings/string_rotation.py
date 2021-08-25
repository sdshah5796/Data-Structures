def rotateString(s, goal):
    if len(s) == len(goal) and len(s) > 0:
        updated_string = s + s

        return goal in updated_string