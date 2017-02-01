# Copyright 2017 Lorenzo Rizzello
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

class UT():

    def __init__(self):
        self.tests = []
        self.run_n = 0
        self.succ_n = 0

    def add(self, fn, args, res):
        self.tests.append([fn, args, res])

    def run(self):
        for t in self.tests:
            print('> testing :')
            print(' - fn: ',  t[0].__name__)
            print(' - args: ', t[1])
            res = t[0](*t[1])
            if res == t[2]:
                print('> test succeded')
                self.succ_n += 1
            else:
                print('> test failed')
                print('> returned: ', res)
            print('---')
            self.run_n += 1
        print('> ', self.succ_n, '/', self.run_n)

ut = UT()

def add(fn, args, res):
    ut.add(fn, args, res)

def run():
    ut.run()
