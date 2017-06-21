#!/usr/bin/python

from __future__ import print_function

import sys

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel

#------------------------------------------------------------------------------

class Ring(Topo):
    def __init__(self, number_of_switches, number_of_hosts):
        """ Creates a ring with a variable amount of hosts and switches. """

        self.number_of_switches = number_of_switches
        super(Ring, self).__init__(n=number_of_hosts)

    #--------------------------------------------------------------------------

    def build(self, n=1):
        """ Build the topology with n hosts attached to each switch. """
        
        # Create a list of self.number_of_switches switches
        switches = [self.addSwitch('s{}'.format(i + 1)) for i in
                range(self.number_of_switches)]

        for index, switch in enumerate(switches):
            # Create n hosts
            for host_number in range(n):
                host = self.addHost('h{}'.format(index * n + host_number + 1))
                self.addLink(host, switch)

            # Connect the switch to other switches
            # (links are bidirectional)
            if self.number_of_switches == 2:
                if index == 0:
                    self.addLink(switch, switches[1])
            elif self.number_of_switches > 2:
                self.addLink(switch, switches[(index + 1)
                    % self.number_of_switches])

#------------------------------------------------------------------------------

def create_topology(number_of_switches, number_of_hosts):
    """ Create a topology with n switches connected to m hosts. """

    topology = Ring(number_of_switches, number_of_hosts)
    net = Mininet(topology)

    net.start()

    # Down a link in order to fix the circular problem
    net.configLinkStatus('s1', 's2', 'down')
    
    net.pingAll() # Test if all hosts can communicate
    net.stop()

#------------------------------------------------------------------------------

if __name__ == '__main__':
    """ Creates a ring of N switches that have M hosts connected to them, with:
        - N: the first argument, number of switches: 3 minimum 
        - M: the second argument, or 3 host per switch
    """
    # Set the output level; change to debug if necessary
    setLogLevel('info')

    number_of_switches= int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]
            > 2) else 3
    number_of_hosts = int(sys.argv[2]) if (len(sys.argv) > 2) else 3

    create_topology(number_of_switches, number_of_hosts)
