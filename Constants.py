class constants :
    name = "seashark"
    xboxmac = "98:7A:14:6D:9D:D4"
    bitdomac = "E4:17:D8:1A:87:0E"
    imageFolder="/home/pi/seashark/captures/image"
    fileNameLength = 6
    
    BUTTON_MAP = {
    304: "B",
    305: "A",
    306: "Y",
    307: "X",
    308: "LB",
    309: "RB",
    310: "-",
    311: "+",
    139: "MENU"
}
    
    AXIS_MAP = {
    "ABS_HAT0X": {
        -1: "LDpad",
         1: "RDpad"
    },
    "ABS_HAT0Y": {
        -1: "UDpad",
         1: "DDpad"
    },
    "ABS_Z": {
        1023: "LT"
    },
    "ABS_RZ": {
        1023: "RT"
    },
    "ABS_X": {
         0: "JL",
    65535: "JR"
    },
    "ABS_Y": {
         0: "JU",
    65535: "JD"
    }
}