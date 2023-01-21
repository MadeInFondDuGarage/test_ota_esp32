

class ReadTemp:
    
    def __init__(self,pin):
        import machine
        import onewire
        import ds18x20
        dat = machine.Pin(12)
        ds = ds18x20.DS18X20(onewire.OneWire(dat))
        roms = ds.scan()
        print('found devices:', roms)

    def Read(self):
        _Temp=0
        _Error=""
        try:
            ds.convert_temp()
        except:
            _Temp= -100
            _Error='Erreur de connection'
        try:
            _Temp=ds.read_temp(roms[0])
        except:
            _Temp=-100
            _Error='Erreur de lecture'
        return _Temp, _Error
