import logging

import threading

import time


def thread_function(name):

    logging.info("Thread %s: starting", name)

    time.sleep(2)

    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), ) #daemon = True
    logging.info("Main    : before running thread")
    x.start()
    #x.join() #join mean the thread will run
    logging.info("Main    : wait for the thread to finish")
    x.join() #=>Now it will have to wait until it finish sleep to run all done
    logging.info("Main    : all done")