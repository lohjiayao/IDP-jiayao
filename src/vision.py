import cv2

def capture_frame():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Cannot access webcam")
        return None
    
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        return frame
    return None

def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow('Webcam', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
