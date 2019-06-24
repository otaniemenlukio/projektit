#!/usr/bin/python3
import iot


@iot.listen("It's too hot")
def full_speed():
    iot.say("OK, turning the fan on")
    iot.publish("tuuletin","full")


@iot.listen("half power")
def half_speed():
    iot.say("OK, turning the fan off")
    iot.publish("tuuletin","half")


@iot.listen("It's too cold")
def off():
    iot.say("OK, turning the fan off")
    iot.publish("tuuletin","off")


iot.run("puheohjaus","aalto-shiftr-testi","aalto-shiftr-testi")


