import os
def finder_dir(name_dir,name_file, way='D:\\' ):
    # def finder_file(name_1):
    #     for filename in os.listdir(way):
    #         f=os.path.join(way,filename)
    #         if os.path.isfile(f):
    #             if f==way+name_dir+'\'+name_dir:
    #                 file=open(f,'r')
    #                 file.read()
    #                 file.close()
    for filename in os.listdir(way):
        f=os.path.join(way,filename)
        if os.path.isdir(f):
            if f==way+name_dir:
                finder_file(name_file)
finder_dir('Test','PS')
