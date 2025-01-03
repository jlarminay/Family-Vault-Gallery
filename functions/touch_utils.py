import evdev
from config import TOUCHSCREEN_DEVICE

def open_touchscreen_device():
    """Open the touchscreen device"""
    return evdev.InputDevice(TOUCHSCREEN_DEVICE)

def touch_detected(device):
    """Check if a touch event is detected"""
    for event in device.read():
        if event.type == evdev.ecodes.EV_ABS:
            return True
    return False
