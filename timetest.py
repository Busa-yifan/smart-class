import  cv2
import  threading
import  time


def music():
    print("我在听音乐")
    time.sleep(5)
    print("我看完了")

def movie():
    print("我在看电影")


threads = []
t1 = threading.Thread(target=music)
threads.append(t1)
t2 = threading.Thread(target=movie)
threads.append(t2)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(False)
        t.start()


    print("结束")