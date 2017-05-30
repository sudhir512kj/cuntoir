import getLib
import authLib
import taskLib

def handlePostRequest(dataDict):
    returnCode = 0
    method = dataDict["method"]
    if(method == "login"):
        returnCode = authLib.createAuthCode(dataDict["username"], dataDict["userPass"])
    if(method == "createUser"):
        returnCode = authLib.createUser(dataDict)
    if(method == "authUser"):
        returnCode = authLib.checkAuthCode(dataDict)
    if(method == "addTask"):
        returnCode = taskLib.addTask(dataDict)
    if(method == "completeTask"):
        returnCode = taskLib.completeTask(dataDict)
    if(method == "getAll"):
        returnCode = getLib.getAll(dataDict)
    return(returnCode)

def handleGetRequest(dataDict):
    returnString = "null"
    method = dataDict["method"]
    if(method == "getOne"):
        returnString = getLib.getOne(dataDict)
    return(returnString)