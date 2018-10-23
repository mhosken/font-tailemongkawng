APPNAME="TaiLeMongKawng"
getufoinfo('source/TaiLeMongKawng.ufo')

font(target = 'TaiLeMongKawng.ttf',
        source = 'source/TaiLeMongKawng.ufo',
        opentype = fea('TaiLeMongKawng.fea',
                master = 'source/taile.fea'),
        script = ['Tale'])
