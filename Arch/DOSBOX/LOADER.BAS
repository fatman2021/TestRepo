' NewImage = ImageScale(SourceImage,width,height)

' mode = ScreenList(32)
' While (mode <> 0)
'    w = HiWord(mode)
'    h = LoWord(mode)
'    mode = ScreenList()
' Wend
' ScreenRes 640, 480, 32, , &H01 : Cls ' And &H40 And &H80 : Cls
' ImageCreate only works, if graphic's screen is defined first!!!
' Dim As Any Ptr img1 = ImageCreate(640, 480)
' Dim As Any Ptr img2 = ImageCreate(640, 480)

' Bload "Podloga.bmp", img1  : Put (0,0), Img1, Pset
' Bload "snowman.bmp", img2 : Put Img1, (0, 0), Img2, Alpha 
' Put (0,0), Img2, Alpha
'
' Put (0, 0), img1, Pset
' Print w;"x"; Ltrim$(Str$(h)); " 32-bit(RGBA)"
' While Inkey = ""
'    Sleep 10, 1  ' prevent CPU *hogging*
' Wend
ScreenRes 640, 480, 32, , &H1: Cls
Dim As Integer Index
For Index = 1 to 150
   Bload "..\..\MEDIA\FLUID~1.SIM\FRAMES\" + Ltrim(Str$(Index)) + ".bmp", 0 ' LoadingScreen(Index)
Next Index
For Index = 1 to 150
   Bload "..\..\MEDIA\LANDSC~1\FRAMES\" + Ltrim(Str$(Index)) + ".bmp", 0 ' LoadingScreen(Index)
Next Index
For Index = 1 to 150
   Bload "..\..\MEDIA\LIVING~1.ROO\FRAMES\" + Ltrim(Str$(Index)) + ".bmp", 0 ' LoadingScreen(Index)
Next Index
For Index = 1 to 150
   Bload "..\..\MEDIA\MODERN~1.WOH\FRAMES\" + Ltrim(Str$(Index)) + ".bmp", 0 ' LoadingScreen(Index)
Next Index
For Index = 1 to 150
   Bload "..\..\MEDIA\WATER~1.HOL\FRAMES\" + Ltrim(Str$(Index)) + ".bmp", 0 ' LoadingScreen(Index)
Next Index
End

