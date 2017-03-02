# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:58:54 2017

@author: chinmay

The script can be used to merge raster tiles together.
"""
import os

"""The general directory tree structure and actual filename for which script was written goes like: 
~/testdata/h*v*/test_01.01.2003.tif"""

"""list different tile folders from which tiles need to me merged"""

Tiles=['h25v6', 'h25v7', 'h26v6', 'h26v7', 'h26v7','h26v8',\
       'h27v6', 'h27v7', 'h27v8', 'h28v6', 'h28v7', 'h28v8'] 

"""directory containing all the aforementioned tiles"""

Dir='/home/chinmay/github/merge_tiffs/testdata'                                              

"""set path to gdal_merge.py depending upon your installation"""
gdal_merge=' /usr/bin/gdal_merge.py'                

"""Define output directory"""
DirOut=os.path.join(Dir,'Merged')

if not os.path.exists(DirOut):
    os.makedirs(DirOut)

"""loop over tiles and merge different tiles with same date"""    
    
for year in range(2003,2015):
    for month in range(1,13):
        """create output name and path"""
        name='Mergedtile-' + str(year) + '.' + str(month).zfill(2) + '.01.tif'
        NameOut=os.path.join(DirOut,name)
        
        
        TotInFiles=' '.join(['python',gdal_merge])
        
        datatile='test_01.'+ str(month).zfill(2) + '.'+ str(year) + '.tif'
        
        for i in range(0,len(Tiles)):
            
            inTiles=os.path.join(Dir,Tiles[i],datatile)
            TotInFiles=' '.join([str(TotInFiles), str(inTiles)])
        
        
        TotInFiles=' '.join([str(TotInFiles), str(inTiles)])
        
        fullCmd = ' '.join(['%s' % (TotInFiles), '-o %s' % (NameOut)])
        os.system(fullCmd)
