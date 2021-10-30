def Main():
    import datetime
    #*** Create logs file***
    Path="C:\\Users\\qiany\\Documents\\NetSarang Computer\\7\\Xshell\\Logs\\"
    logFileName=str("TestLog_"+datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")+".log")
   
    #*** Start log***
    xsh.Session.LogFilePath = (Path+logFileName)
    xsh.Session.StartLog()
    
    #*** Send command***
    for line in open("C:\\Users\\qiany\\Documents\\NetSarang Computer\\7\\Xshell\\Scripts\\CommandManager\\TestScript.txt"):
        xsh.Screen.Send(line)
        xsh.Screen.Send('\r')
        xsh.Session.Sleep(1000)
    xsh.Session.Sleep(2000)
    xsh.Session.StopLog()
    #xsh.Screen.Clear()
