# Preventing loops from happening

As I've mentioned it [here](../README.md), the following methods are going to try and prevent forwarding loops from happening with increasingly difficult (and hopefully efficient) solutions.

## Blocking a port

The file [solution1.py](solution1.py) demonstrates how this can be achieved.

To summarize, out of all the switches in the topology one is selected (the first one in my program for convenience sake) in order to deactivate one of its two connections with other switches.

It solves the problem since it essentially "cuts" the ring in order to form a linear network in which loops can't occur.

This solution is not really good since it is not robust: if a link were to fall then the network would be split into two since the first switch would not be "smart" enough to reactivate its deactivated port.

## Using STP

The Spanning Tree Protocol corrects this issue since it will automatically block a port if it detects a loop.

Additionally, it is robust since the disappearance of a link will cause the blocked port to change its state to forwarding, and the network will not be split into two.

In order to achieve that, I have used a custom topology
([solution2.py](solution2.py)) that creates a ring with more than 2 switches in
order to create a situation where loops will occur.

However, the simulation that has been started with the following command works
because it uses STP:

`sudo mn --custom mininet/custom/solution2.py --topo ring --switch ovsbr,stp=1
--test pingall`

The first part is to indicate that a custom file is present and that the
topology used in this example should be the one defined in
[solution2.py](solution2.py)

## Using a learning switch
