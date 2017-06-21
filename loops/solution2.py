#!/usr/bin/python

from __future__ import print_function

import sys

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel

#------------------------------------------------------------------------------

class Ring(Topo):
    def __init__(self, number_of_switches=3, number_of_hosts=2):
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

# Add the custom topology
topos = {'ring': (lambda: Ring())}
