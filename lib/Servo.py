class myServo:
    '''pour le pilotage des servo de modélisme, freq de 50 pour un cycle de 20ms'''
    '''mini - maxi de mouvement d'un servo entre 1ms et 2ms'''
    ''' entre 50 et 120 pour 0 a 180'''
    
    def __init__(self,pin):
        self._freq=50
        self._pos=80
        self._pin=pin
        self._min=36
        self._max=145
        self._angle=0
        self._instance_()
    
    def _instance_(self):
        import machine
        self._servo=machine.PWM(machine.Pin(self._pin), freq=self._freq)
        self.set_Pos(self._pos)
        
    def set_Pos(self,pos):
        self._pos=pos
        if self._pos <self._min:
            self._pos=self._min
        if self._pos >self._max:
            self._pos=self._max
        self._servo.duty(int(self._pos))
        
    def get_Pos(self):
        return self._pos
        
    def set_Freq(self,freq):
        self._freq=freq
        self._instance_()
        
    def get_Freq(self):
        return self._freq
    
    def set_Off(self):
        self._servo.duty(0)
    
    def set_On(self):
        self.set_Pos(self._pos)
        
    def set_Max(self):
        self.set_Pos(self._max)
        
    def set_Min(self):
        self.set_Pos(self._min)
    
    def set_Angle(self,Angle):
        if Angle < 0:
            Angle=0
        if Angle > 180:
            Angle=180
        _myPos=self._map(Angle,180,0,self._max,self._min)
        self.set_Pos(_myPos)
            
    def get_Angle(self):
        '''position par rapport a l'angle en mode règle de 3'''
        return int(self._map(self._pos,self._max,self._min,180,0))
    
    def _map(self,x,in_max,in_min,out_max,out_min):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min