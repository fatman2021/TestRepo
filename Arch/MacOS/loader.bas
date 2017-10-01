SCREEN _NEWIMAGE(640, 480, 32): _FULLSCREEN
DIM Index AS INTEGER, Handle AS LONG
Handle = _NEWIMAGE(640, 480, 32)
FOR Index = 1 TO 150
    Handle = _LOADIMAGE("../../Media/Living.Room/Frames/" + LTRIM$(STR$(Index)) + ".bmp")
    _PUTIMAGE (0, 0), Handle
    _LIMIT 15
NEXT Index
CLS
FOR Index = 1 TO 119
    Handle = _LOADIMAGE("../../Media/Water.Hole/Frames/" + LTRIM$(STR$(Index)) + ".bmp")
    _PUTIMAGE (0, 0), Handle
    _LIMIT 15
NEXT Index
CLS
FOR Index = 1 TO 50
    Handle = _LOADIMAGE("../../Media/Fluid.Simulation/Frames/" + LTRIM$(STR$(Index)) + ".bmp")
    _PUTIMAGE (0, 0), Handle
    _LIMIT 15
NEXT Index
CLS
FOR Index = 1 TO 17
    Handle = _LOADIMAGE("../../Media/Landscape/Frames/" + LTRIM$(STR$(Index)) + ".bmp")
    _PUTIMAGE (0, 0), Handle
    _LIMIT 15
NEXT Index
CLS
FOR Index = 1 TO 145
    Handle = _LOADIMAGE("../../Media/Modernes.Wohnzimmer/Frames/" + LTRIM$(STR$(Index)) + ".bmp")
    _PUTIMAGE (0, 0), Handle
    _LIMIT 15
NEXT Index

SYSTEM
