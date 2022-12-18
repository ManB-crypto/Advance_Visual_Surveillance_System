import cv2
from sendtele import *
classes = []


with open('coco.names','rt') as f:
    classes = f.read().rstrip('\n').split('\n')

net = cv2.dnn_DetectionModel('frozen_inference_graph.pb', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)


def objects(image,objectlist = []):
    classIds,confs,bbox = net.detect(image,confThreshold = 0.65)
    global count
    if len(objectlist) == 0:
        objectlist = classes
    if len(classIds) !=0:
        for classID, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            classname = classes[classID - 1]
            objectlist.append([box, classname])

            if classname in objectlist:
                #cv2.waitKey(10)
                cv2.rectangle(image, box, color=(160, 32, 240), thickness=1)
                cv2.putText(image, classname.upper(), (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (160, 32, 240), 2)
                if count == 1:
                    print("image saved" + str(count + 1))
                    file = r"/home/manb/flask/evidence/image.jpg"
                    cv2.imwrite(file, image)
                    sendnoty()
                elif count == 50:
                    count =0
                    
                print("On Cooldown"+str(count))
                count += 1
                    
                    







    return image,objectlist

if __name__ == "__main__":
    cap = cv2.VideoCapture(-1)
    cap.set(3, 640)
    cap.set(4, 480)
    count = 0
    while True:
        success, image = cap.read()
        result, objectlist = objects(image, objectlist=['person'])  # to add specific object list to detect
        print(objectlist)
        #cv2.imshow('Raw Webcam Feed', image)
        cv2.waitKey(2)









