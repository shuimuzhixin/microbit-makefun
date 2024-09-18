basic.forever(function () {
    sensors.actuator_motor_run(AnalogPin.P1, AnalogPin.P2, run_turn.forward, 0)
})
