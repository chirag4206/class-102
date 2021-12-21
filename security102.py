import cv2
import dropbox
import time
import random
startTime=time.time()

def takeSnapshot():
    number=random.randint(0,100)
    videocaptureobject =cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False
    return imagename
    print("snapshottaken")
    videocaptureobject.release()
    cv2.destroyAllWindows()

def uploadfile(imagename):
    accesstoken="bqmix-WTwRQAAAAAAAAAATmoPOZM0STuD31vfijs_qrEj-OQpn2UFLUhWT7n6uhB"
    file=imagename
    filefrom=file
    fileto="Dropbox/a/"
    dbx=dropbox.Dropbox(accesstoken)
    with open(filefrom,"rb") as f:
        dbx.files_upload(f.read(),fileto,mad=dropbox.files.Writemod.overwrite)
        print("fileUploaded")

def main():
    while(True):
        if((time.time()-startTime)>=300):
            name=takeSnapshot()
            uploadfile(name)

main()