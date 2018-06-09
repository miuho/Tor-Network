import io
import pycurl
import time
import stem.process
from stem.util import term
# reference: https://stem.torproject.org/tutorials/to_russia_with_love.html

SOCKS_PORT = 7000

def query(url):
  output = io.BytesIO()
  # connect to webserver with pycurl
  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
    # return the query output from webserver
    return output.getvalue()
  # query failed with exception
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)

# print bootstrap info
def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    term.format(line, term.Color.BLUE)

# Time the query without tor
print "Connecting to www.cmu.edu without tor..."
start_time = time.time()
query("http://www.cmu.edu")
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Start tor instance with exit node at Russia
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{ru}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "Connecting to www.cmu.edu with tor..."
start_time = time.time()
term.format(query("http://www.cmu.edu"), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()
