#实现近似使用坐标对Raster对象访问的一些功能

import mmap
#import Convert
class RasterMap:
    def __init__(self, o_r, o_a):
        self.origin_raster = o_r
        self.origin_ascii = o_a
        #self.raster_properties = Convert.raster_properties(o_r)
        self.ascii_info = self.ASCII_info()
        f = open(self.origin_ascii, "r+b")
        self.map_obj = mmap.mmap(f.fileno(),0)

def ASCII_info(self):
        oa = open(self.origin_ascii, 'r')
        line_length = len(oa.readline())
        line_count = 1
        try:
            while True:
                oa.next()
                line_count += 1
        except StopIteration:
            pass
        oa.seek(0)
        return {'line_length': line_length, 'line_count': line_count}

def read(self, x, y):
        width = int(self.raster_properties['width'])
        line_length = int(self.ascii_info['line_length'])
        offset = (x * width + y) * (line_length + 1)
        self.map_obj.seek(offset)
        line = int(self.map_obj.readline())
        self.map_obj.seek(0)
        return line

def write(self, x, y, value):
        width = int(self.raster_properties['width'])
        line_length = int(self.ascii_info['line_length'])
        offset = (x * width + y) * (line_length + 1)
        self.map_obj.seek(offset)
        self.map_obj.write(str(value))
        self.map_obj.write(" " * (12-len(str(value))))
        self.map_obj.seek(0)