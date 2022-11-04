class Particle:
    def __init__(self,name,spin):
        self.name=name
        self.spin=spin
        
    def is_up_or_down(self):
        if self.spin==0.5:
            return('up')
        elif self.spin==-0.5:
            return('down')
        else:
            print('error, spin not (-)1/2')
        
    def flip(self):
        self.spin= self.spin*-1
        return (self.spin)
    
proton = Particle('mooi proton', 0.5)

quark = Particle('mooi quark', 0.4)
print(proton.is_up_or_down())
print(proton.flip())
print(proton.is_up_or_down())
proton.name
quark.name
quark.flip()
quark.is_up_or_down()