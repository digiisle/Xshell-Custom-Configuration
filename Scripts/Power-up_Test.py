def Main():
    #*** Start log***
    #xsh.Session.LogFilePath = "C:\\Users\\qianyunkang\\Documents\\NetSarang Computer\\6\\Xshell\Logs\\MDF2-10_12804.log"
    #xsh.Session.StartLog()
    #*** Send command***
    for line in open("C:\\Users\\qianyunkang\\Documents\\NetSarang Computer\\6\\Xshell\\Scripts\\Command Line\\Power-up_Test.txt"):
        xsh.Screen.Send(line)
        xsh.Screen.Send('\r')
        xsh.Session.Sleep(1000)
    #xsh.Session.StopLog()
    #xsh.Screen.Clear()