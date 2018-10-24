#!/usr/bin/python2
# encoding: utf-8
# this is a smith configuration file - http://scripts.sil.org/smith

APPNAME = "TaiLeMongKawng"
FAMILY = APPNAME
DESC_SHORT = "Unicode font for Tai Le with marking tones"


getufoinfo('source/TaiLeMongKawng-Regular.ufo')
BUILDLABEL = "alpha"

font(target = 'TaiLeMongKawng.ttf',
        source = 'source/TaiLeMongKawng.ufo',
        opentype = fea('TaiLeMongKawng.fea',
                master = 'source/taile.fea'),
        fret = fret(params='-r -oi'),
        woff = woff('web/TaiLeMongKawng-Regular.woff', params = '-v ' + VERSION + ' -m ../source/TaiLeMongKawng-WOFF-metadata.xml'),
        script = ['Tale'])
