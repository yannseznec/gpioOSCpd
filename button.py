from gpiozero import Button
button = Button(2)
button.wait_for_press()
print('You pushed me')