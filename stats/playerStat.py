#-------------------------------------------------------------------------------
# Copyright (c) 2014 Gael Honorez.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#-------------------------------------------------------------------------------

class playerStat(object):
    def __init__(self, player=None, Id=None, army=None, mass = [], energy = [] ):
        
        self.playerName = player
        self.playerId = Id
        self.army = army
        self.energy = energy
        self.mass = mass
        
    def __str__(self):
        return "%i - %s - Energy : %f, Mass %f" % (self.playerId, self.playerName, self.energy[0], self.mass[0])
    
    def comBuilt(self) :
        return self.army.comBuilt()
    
    def comLost(self) :
        return self.army.comLost()
                                  
    def comKilled(self) :
        return self.army.comKilled()

    def getName(self):
        return self.playerName
    
    def getScore(self):
        return self.army.comKilled() - self.army.comLost()