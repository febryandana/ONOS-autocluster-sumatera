#!/usr/bin/env python

" Custom Topology to use ONOS Controller"

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create Sumatra Education Network topology..."
        
        # Inisialisasi Topology
        Topo.__init__( self )

        # Tambahkan node, switch, dan host

        info( '*** Add switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')

        info( '*** Add hosts\n')
        h1 = self.addHost('h1', ip='10.1.0.1')
        h2 = self.addHost('h2', ip='10.2.0.2')
        h3 = self.addHost('h3', ip='10.2.0.3')
        h4 = self.addHost('h4', ip='10.3.0.4')
        h5 = self.addHost('h5', ip='10.4.0.5')
        h6 = self.addHost('h6', ip='10.4.0.6')
        h7 = self.addHost('h7', ip='10.4.0.7')
        h8 = self.addHost('h8', ip='10.5.0.8')
        h9 = self.addHost('h9', ip='10.6.0.9')
        h10 = self.addHost('h10', ip='10.7.0.10')
        h11 = self.addHost('h11', ip='10.7.0.11')
        h12 = self.addHost('h12', ip='10.8.0.12')
        h13 = self.addHost('h13', ip='10.8.0.13')

        info( '*** Add links\n')
        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s2, h3)
        self.addLink(s3, h4)
        self.addLink(s4, h5)
        self.addLink(s4, h6)
        self.addLink(s4, h7)
        self.addLink(s5, h8)
        self.addLink(s6, h9)
        self.addLink(s7, h10)
        self.addLink(s7, h11)
        self.addLink(s8, h12)
        self.addLink(s8, h13)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s5)
        self.addLink(s5, s7)
        self.addLink(s7, s8)
        self.addLink(s4, s6)
        self.addLink(s6, s8)
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
    
if __name__ == '__main__':
    from onosnet import run
    run( MyTopo() )
