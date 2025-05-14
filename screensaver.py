import hid
import time

try:

    VENDOR_ID_STEELSERIES = 0x1038
    PRODUCT_ID_ARCTIS_NOVA_PRO_WIRELESS = 0x12e0
    INTERFACE_NUMBER = 4

    SCREEN_WIDTH = 128
    SCREEN_HEIGHT = 64

    REPORT_SIZE_SCREEN = 1024

    device_list = hid.enumerate(VENDOR_ID_STEELSERIES, PRODUCT_ID_ARCTIS_NOVA_PRO_WIRELESS)

    # filter device_list by interface_number
    device_list = [device for device in device_list if device['interface_number'] == INTERFACE_NUMBER]

    device_in = device_list[0] if device_list else None
    if device_in:
        print("IN Device found")

        h = hid.device()
        h.open_path(device_in['path'])

        # enable non-blocking mode
        h.set_nonblocking(1)

        # check status
        report = [0] * 32
        report[0] = 0x00
        report[1] = 0x06 # hid report id
        report[2] = 0xb0 # command id
        h.write(report)

        # wait
        time.sleep(0.05)

        connected = None

        # read device status
        response = h.read(16)
        if response and response[0] == 0x06 and response[1] == 0xb0:
            connected = (response[14] == 8)

        if not connected:
            print("Clear the screen")
            SPLITS = 4
            FILL_WIDTH = SCREEN_WIDTH // SPLITS
            for i in range(0, SPLITS):
                report = [0] * REPORT_SIZE_SCREEN
                report[0] = 0x00
                report[1] = 0x06 # hid report id
                report[2] = 0x93 # command id
                report[3] = i * (FILL_WIDTH) # x
                report[4] = 0 # y
                report[5] = FILL_WIDTH # width
                report[6] = SCREEN_HEIGHT # height
                report[7] = 0b000000000
                h.send_feature_report(report)

        print("Closing the device")
        h.close()

except IOError as ex:
    print(ex)
    print("hid error:")
    print(h.error())
