#!/usr/env/bin python
import netfilterqueue

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()