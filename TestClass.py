import sys

class person():
    name='wangcl'
    def __init__(self, *args, **kwargs): 
        print >> sys.stderr, 'counting movies number and popularity...'
        print "--------init--------"
        #super(person, self).__init__(*args, **kwargs)
    def __new__(cls, *args, **kwargs):
        print "new", cls
        #return super(person, cls).__new__(cls, *args, **kwargs)
    def __call__(self,  *args, **kwargs):
        print "call"
        
p1=person()
print(p1.name)

print('-----------')
s1={}
s1.setdefault('k1',{})
s1.setdefault('k2',{})
s1['k1']['m1']='1'
s1['k1']['m2']='2'
s1['k2']['m1']='1'
s1['k2']['m2']='2'
print("s1:",s1)

p1()

start_urls=[]
district=["dongcheng","xicheng"]
    
for url in xrange(1,3):
    for dist in district:
        start_urls.append("http://bj.lianjia.com/ershoufang/"+dist+"/pg"+str(url)+"/")
print(start_urls)

print('================Python import mode==========================');
print ('The command line arguments are:')
for i in sys.argv:
    print (i)
print ('\n The python path',sys.path)