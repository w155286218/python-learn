#coding:utf-8
import random
class RanPlay:
    # music is a list which contains name of music and its score
    def __init__(self,musics):
        self.musics = musics
        self.region = {}
        self.counter = 0
        for music in musics:
            self.counter += music['score']
            self.region[self.counter] = music['name']
    def play(self):
        key = random.randint(0,int(self.counter * 10) )/ 10.0
        temp = filter(lambda x:key<x,self.region.keys())
        print key,temp
        if len(temp) !=0:
            played_music_key = min(temp)   
        else:
            played_music_key = max(self.region.keys())
        return self.region[played_music_key]

musics = [
    {
        "name":"平凡之路",
        "score":8.9
    },
    {
        "name":"夜空中最亮的星",
        "score":9.5,
    },
]
r = RanPlay(musics)
print r.play()
