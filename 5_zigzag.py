import time, sys

indent = 0
indentIncreasing = True

try:
    # Setup
    while True:
        print(' ' * indent, end='')
        print("********")
        # Speed
        time.sleep(0.1)

        # Moving right
        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False

        # Moving left
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()