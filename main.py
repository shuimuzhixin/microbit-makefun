basic.show_icon(IconNames.HEART)
sensors.basic_piano_pin(DigitalPin.P12, DigitalPin.P8)

def on_forever():
    sensors.basic_piano_play()
    basic.show_icon(IconNames.DUCK)
basic.forever(on_forever)
