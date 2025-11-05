import cv2, os

class CameraFootage:
    idx = 0
    base_dir = ""
    video_capture = None

    def __init__(self, dir="/home/aero/ben_test/photos/"):
        self.video_capture = cv2.VideoCapture(0)
        self.base_dir = dir


    def clear_folder(self):
        photos = [name for name in os.listdir(self.base_dir)]
        for i in photos:
            os.remove(self.base_dir+i)


    def save_frame(self):
        name = "p_"+str(self.idx)+".jpg"
        dir = '{}{}'.format(self.base_dir, name)

        result, frame = self.video_capture.read()  #read frames from video
        if result is False:
            return  #terminate if frame is not read successfully
        
    #    cv2.imshow("Video Output", video_frame)
        cv2.imwrite(dir, frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            return
        
        self.idx += 1

        return name

    def stop_recording(self):
        self.video_capture.release()
        cv2.destroyAllWindows()