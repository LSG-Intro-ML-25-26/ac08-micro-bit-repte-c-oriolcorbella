radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber > dauA) {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    }
    if (receivedNumber < dauA) {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    } else {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            `)
    }
})
input.onButtonPressed(Button.A, function () {
    dauA = randint(1, 6)
    basic.showNumber(dauA)
    radio.sendNumber(dauA)
})
let dauA = 0
radio.setGroup(1)
