#-*-coding:utf8-*-
import cv2, base64, urllib.request, urllib.parse
import os
import traceback, numpy
import time
from PyQt5 import QtGui
from UI import image_recogntion as img
from CommonClass import Common
import face_SDK

class getPhoto():
    sdk = face_SDK.Face_SDK()
    def getP(self, imgPath):
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()

        image = get_file_content(imgPath)

        """ 调用人脸检测 """
        A = Common()
        client = A.new_AipFace()
        # client.detect(image)

        """ 如果有可选参数 """
        options = {}
        options["face_fields"] = "qualities"
        # options["face_fields"] = "age"

        """ 带参数调用人脸检测 """
        content = client.detect(image,options)
        print (content)



        request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"
        f = open(imgPath, 'rb')
        self.img = base64.b64encode(f.read())
        f.close()
        params = {"face_fields": "expression,faceshape,gender,race",
                  "image": self.img, "max_face_num": 5}
        params = urllib.parse.urlencode(params).encode(encoding='UTF8')
        A = Common()
        access_token = A.getAccess_token()
        print (type(access_token))
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            content = content.decode()
            content = eval(content)
            print(type(content))
            return content['location']

        try:
            cascade = cv2.CascadeClassifier("Source/haarcascade_frontalface_alt2.xml")
            cascade.load("E:/jsjsj/cascades/haarcascade_frontalface_alt.xml")

            self.img = cv2.imdecode(numpy.fromfile(imgPath, dtype=numpy.uint8), -1) # 读取图像
            gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            rect = cascade.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=5,minSize=(32,32),flags=cv2.CASCADE_SCALE_IMAGE)
            roi = []
            if not rect is ():
                i = 0
                for x, y, z, w in rect:
                    roiImg = cv2.resize(gray[y:(y + w), x:(x + z)], (200, 200))
                    roi.append(roiImg)
                    cv2.rectangle(self.img, (x, y), (x + z, y + w), (0, 0, 255), 2)
                    i += 1
            self.save_path ="E:\Face\\Graduation-design\\Source\\image\\img_dealed.jpg" # 检测后原图的存放地址
            if os.path.exists(self.save_path):
                os.remove(self.save_path)
            else:
                pass
            cv2.imwrite(self.save_path, self.img)
            return self.save_path, roi
        except:
            # 输出异常信息
            traceback.print_exc()


#
if __name__ == '__main__':
    photo = getPhoto()
    photo.getP(r'./UI/1.jpg')