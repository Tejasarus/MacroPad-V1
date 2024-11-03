import board
import digitalio
import usb_hid
import rotaryio
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Set up a keyboard/control devices
keyboard = Keyboard(usb_hid.devices)
control = ConsumerControl(usb_hid.devices)
encoder = rotaryio.IncrementalEncoder(board.GP17, board.GP16)
keyboard_layout = KeyboardLayoutUS(keyboard)
last_position = 0

#GPIO 0 Button
button_pin_zero = board.GP0
button_zero = digitalio.DigitalInOut(button_pin_zero)
button_zero.direction = digitalio.Direction.INPUT
button_zero.pull = digitalio.Pull.UP

#GPIO 1 Button
button_pin_one = board.GP1
button_one = digitalio.DigitalInOut(button_pin_one)
button_one.direction = digitalio.Direction.INPUT
button_one.pull = digitalio.Pull.UP

#GPIO 2 Button
button_pin_two = board.GP2
button_two = digitalio.DigitalInOut(button_pin_two)
button_two.direction = digitalio.Direction.INPUT
button_two.pull = digitalio.Pull.UP

#GPIO 3 Button
button_pin_three = board.GP3
button_three = digitalio.DigitalInOut(button_pin_three)
button_three.direction = digitalio.Direction.INPUT
button_three.pull = digitalio.Pull.UP

#GPIO 4 Button
button_pin_four = board.GP4
button_four = digitalio.DigitalInOut(button_pin_four)
button_four.direction = digitalio.Direction.INPUT
button_four.pull = digitalio.Pull.UP

while True:
    #Ctrl + C
    if not button_zero.value:  
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.C)
        while not button_zero.value:  
            pass
        
    #Ctrl + V
    if not button_one.value:  
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.V)
        while not button_one.value:  
            pass
    
    #mute
    if not button_two.value:  
        control.send(ConsumerControlCode.MUTE)
        while not button_two.value:  
            pass
    
    #play/pause
    if not button_three.value:  
        control.send(ConsumerControlCode.PLAY_PAUSE)
        while not button_three.value:  
            pass
    
    #new tab
    if not button_four.value:  
        keyboard.send(Keycode.CONTROL, Keycode.T)
        while not button_four.value:  
            pass
    
    #encoder 1
    current_position = encoder.position
    
    # Check if the position has changed
    if current_position != last_position:
        if current_position > last_position:
            control.send(ConsumerControlCode.VOLUME_INCREMENT)
            print(f"Volume up, Encoder position: {current_position}")
        elif current_position < last_position:
            control.send(ConsumerControlCode.VOLUME_DECREMENT)
            print(f"Volume down, Encoder position: {current_position}")
        last_position = current_position