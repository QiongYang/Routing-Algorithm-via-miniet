#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import Controller 
from mininet.cli import CLI
from functools import partial
from mininet.node import RemoteController
import os
class MyTopo( Topo ):
 "Shanghai Metro Line Topology."
 def __init__(self):

        Topo.__init__(self)
        switches=[]
#        hosts=[]
        for i in range (303):
        	switch=self.addSwitch('s%s'%i)
        	switches.append(switch)
#        	host=self.addHost('h%s'%i)
#        	hosts.append(host)
#        	self.addLink(switch, host, delay='1ms', max_queue_size=1000, use_htb=True)
        line1=range(28)
        delay1=[2,2,3,3,2,3,2,3,3,2,2,3,1,2,2,3,2,2,2,2,3,2,3,3,3,3,3]
        for i in range(27):
        	self.addLink(switches[line1[i]], switches[line1[i+1]], bw=10, delay=delay1[i], max_queue_size=1000, use_htb=True)
        	
        line2=range(28,39)+[15]+range(39,57)
        delay2=[3,2,7,2,2,3,3,2,3,2,3,2,3,2,2,3,2,2,4,3,2,12,3,4,3,5,5,7,3]
        for i in range(29):
        	self.addLink(switches[line2[i]], switches[line2[i+1]], bw=10, delay=delay2[i], max_queue_size=1000, use_htb=True)		

        line3=range(57,64)+[35]+range(64,68)+[12]+range(68,84)
        delay3=[2,3,2,2,2,3,2,2,2,3,2,3,3,2,3,2,2,3,2,3,2,3,2,2,3,2,2,3]
        for i in range (28):
        	self.addLink(switches[line3[i]], switches[line3[i+1]], bw=10, delay=delay3[i], max_queue_size=1000, use_htb=True)		

        line4=[61]+[21]+range(84,93)+[42]+range(93,98)+[68]+[12]+[67]+[66]+[65]+[64]+[35]+[63]+[62]
        delay4=[3,2,2,1,2,3,2,3,2,2,2,3,2,2,3,2,3,3,3,2,3,1,3,2,2]
        for i in range(25):
        	self.addLink(switches[line4[i]], switches[line4[i+1]], bw=10, delay=delay4[i], max_queue_size=1000, use_htb=True)
        self.addLink(switches[61], switches[62], bw=1, delay='2ms', max_queue_size=1000, use_htb=True)		

        line5=[28]+range(98,108)
        delay5=[2,2,4,3,3,2,3,2,3,2]
        for i in range(10):
        	self.addLink(switches[line5[i]], switches[line5[i+1]], bw=10, delay=delay5[i], max_queue_size=1000, use_htb=True)

        line6=range(108,124)+[42]+[124]+[91]+range(125,134)
        delay6=[2,3,3,3,2,2,2,2,3,2,2,3,2,2,3,2,3,2,3,2,3,2,3,2,2,2,2]
        for i in range(27):
        	self.addLink(switches[line6[i]], switches[line6[i+1]], bw=10, delay=delay6[i], max_queue_size=1000, use_htb=True)
        line7=[134]+[45]+range(135,138)+[127]+range(138,143)+[85]+[143]+[18]+[37]+range(144,146)+[66]+range(146,158)
        delay7=[3,2,3,2,3,2,2,2,2,3,2,2,3,2,3,2,2,3,2,2,3,6,9,2]
        for i in range(24):
        	self.addLink(switches[line7[i]], switches[line7[i+1]], bw=10, delay=delay7[i], max_queue_size=1000, use_htb=True)
        line8=range(158,164)+[133]+range(164,166)+[139]+[166]+[89]+range(167,170)+[15]+range(170,173)+[70]+range(173,183)
        delay8=[2,2,2,4,3,4,2,2,2,2,3,2,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2]
        for i in range(29):
        	self.addLink(switches[line8[i]], switches[line8[i+1]], bw=10, delay=delay8[i], max_queue_size=1000, use_htb=True)	
        line9=[183,42,184,185,170,186,187,188,143,20,61]+range(189,204)
        delay9=[4,2,4,3,2,2,2,2,3,3,3,3,2,3,3,3,4,6,5,3,4,4,3,3,3]
        for i in range(25):
        	self.addLink(switches[line9[i]], switches[line9[i+1]], bw=10, delay=delay9[i], max_queue_size=1000, use_htb=True)
        line10=range(204,211)+[174,211,97,212,213,39,214,168,215,17,216,217,62]+range(218,223)+[30,29]+[224,225,226]
        delay10=[1,2,2,2,2,2,2,2,2,2,2,3,2,2,2,3,2,2,3,2,1,3,2,2,3,3]
        for i in range(26):
        	self.addLink(switches[line10[i]], switches[line10[i+1]], bw=10, delay=delay10[i], max_queue_size=1000, use_htb=True)
        self.addLink(switches[221], switches[224], bw=10, delay='3ms', max_queue_size=1000, use_htb=True)
        self.addLink(switches[224], switches[225], bw=10, delay='2ms', max_queue_size=1000, use_htb=True)
        self.addLink(switches[225], switches[226], bw=10, delay='3ms', max_queue_size=1000, use_htb=True)
        line11=range(227,234)+[134]+range(234,238)+[20,217,36,238,65]+range(239,258)
        delay11=[2,2,3,5,3,2,5,3,2,2,3,3,3,3,2,2,2,2,3,2,3,2,2,5,3,3,4,2,4,6,3,3,2,3,2]
        for i in range (28):
        	self.addLink(switches[line11[i]], switches[line11[i+1]], bw=10, delay=delay11[i], max_queue_size=1000, use_htb=True)
        self.addLink(switches[248],switches[252],bw=10,delay='4ms',max_queue_length=1000,use_htb=True)
        self.addLink(switches[252],switches[253],bw=10,delay='4ms',max_queue_length=1000,use_htb=True)
        self.addLink(switches[253],switches[254],bw=10,delay='4ms',max_queue_length=1000,use_htb=True)
        self.addLink(switches[254],switches[255],bw=10,delay='4ms',max_queue_length=1000,use_htb=True)
        self.addLink(switches[255],switches[256],bw=10,delay='4ms',max_queue_length=1000,use_htb=True)
        self.addLink(switches[256],switches[257],bw=10,delay='4ms',max_queue_length=1000,use_htb=True)
        self.addLink(switches[257],switches[258],bw=10,delay='4ms',max_queue_length=1000,use_htb=True)

        line12=range(259,263)+[115]+range(263,269)+[95,269,270,213,170,38,13,17,188,85,142,236,59,22]+range(271,278)
        delay12=[4,2,2,3,2,3,2,3,3,2,2,2,2,3,3,3,3,3,2,3,2,3,3,2,2,2,3,2,3,2,2]
        for i in range(31):
        	self.addLink(switches[line12[i]], switches[line12[i+1]], bw=10, delay=delay12[i], max_queue_size=1000, use_htb=True)
        line13=range(278,284)+[64,238,284,145,285,13,286,37,287,213,186,288,289]
        delay13=[2,4,3,2,3,4,2,3,2,2,3,1,3,2,3,2,2,3]
        for i in range(18):
        	self.addLink(switches[line13[i]], switches[line13[i+1]], bw=10, delay=delay13[i], max_queue_size=1000, use_htb=True)
        line16=range(290,302)+[45]
        delay16=[3,6,9,5,8,7,6,4,6,7,4,5]
        for i in range(12):
        	self.addLink(switches[line16[i]], switches[line16[i+1]], bw=10, delay=delay16[i], max_queue_size=1000, use_htb=True)


topos = { 'mytopo': ( lambda: MyTopo() ) }