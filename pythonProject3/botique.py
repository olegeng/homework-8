import os
def finder_file(name_file,way):
    for filename in os.listdir(way):
        ff=os.path.join(way,filename)
        if os.path.isfile(ff):
            if ff==way+'\\'+name_file+'.txt':
                file=open(ff,'w')
                file.write('NEW OLEG')
                file.close()
def finder_dir(name_dir,way='D:\\'):
    #global link
    for filename in os.listdir(way):
        f=os.path.join(way,filename)
        if os.path.isdir(f):
            if f==way+name_dir:
                return f
finder_file('PS',finder_dir('AAA'))