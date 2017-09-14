import multiprocessing as mp
import subprocess as sp

class SingleAtkin(object):
    def __init__(self, p, AtkinPath):
        self.p_res = -1
        self.p = p
        self.AtkinPath = AtkinPath

    def __call__(self):
        with sp.Popen([self.AtkinPath], stdin=sp.PIPE, stdout=sp.PIPE) as fp:
        #                fp.communicate(str(int(self.ui.lineEdit.text(), base = 16))+'\n')
            text = self.p
            text = format('%s' % text)
            text = str(int(text, base=16)) + '\n'
            fp.communicate(bytes(text, 'UTF-8'))
            self.p_res = fp.returncode
#        return self.p_res


def AtkinTest(p, q, AtkinPath):
    th1 = SingleAtkin(p, AtkinPath)
    th2 = SingleAtkin(q, AtkinPath)
    thread1 = mp.Process(target = th1)
    thread2 = mp.Process(target = th2)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    return (th1.p_res, th2.p_res)
