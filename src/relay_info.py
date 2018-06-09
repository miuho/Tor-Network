from stem import CircStatus
from stem.control import Controller
# Reference: https://stem.torproject.org/tutorials/examples/

# open controller connection at port 9151
with Controller.from_port(port = 9151) as controller:
  controller.authenticate()
  # get the circuit
  for circ in sorted(controller.get_circuits()):
    if circ.status != CircStatus.BUILT:
      continue

    print("")
    print("Circuit %s (%s)" % (circ.id, circ.purpose))
    # get the relay of this circuit
    for i, entry in enumerate(circ.path):
      div = '+' if (i == len(circ.path) - 1) else '|'
      fingerprint, nickname = entry
      # get info for this relay
      desc = controller.get_network_status(fingerprint, None)
      # get ip address
      address = desc.address if desc else 'unknown'
      # get bandwidth
      bandwidth = desc.bandwidth if desc else 'unknown'
      # get location
      locale = controller.get_info("ip-to-country/%s" % address, 'unknown') if desc else 'unknown'
      print(" %s- IP:%s, locale:%s, bandwidth:%s(kb/s)" % (div, address, locale, bandwidth))
