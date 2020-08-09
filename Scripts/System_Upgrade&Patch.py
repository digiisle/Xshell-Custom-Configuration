def Main():
    #*** Send command***
    for line in open("C:\\Users\\qianyunkang\\Documents\\NetSarang Computer\\6\\Xshell\\Scripts\\Command Line\\System_Upgrade&Patch.txt"):
        xsh.Screen.Send(line)
        xsh.Screen.Send('\r')
        xsh.Session.Sleep(1000)
    #xsh.Screen.Clear()