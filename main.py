def on_received_number(receivedNumber):
    if receivedNumber > dauA:
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    if receivedNumber < dauA:
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
    else:
        basic.show_leds("""
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global dauA
    dauA = randint(1, 6)
    basic.show_number(dauA)
    radio.send_number(dauA)
input.on_button_pressed(Button.A, on_button_pressed_a)

dauA = 0
radio.set_group(1)