import io
import pycurl
import time
import stem.process
from stem.util import term
# reference: https://stem.torproject.org/tutorials/to_russia_with_love.html

url = "https://duckduckgo.com/"

SOCKS_PORT = 7000

def query():
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
print "1. Connecting to %s with tor exit node at Russia..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at Australia
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{au}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "2. Connecting to %s with tor exit node at Australia..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at Ukraine
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{ua}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "3. Connecting to %s with tor exit node at Ukraine..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at France
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{fr}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "4. Connecting to %s with tor exit node at France..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at Romania
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{ro}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "5. Connecting to %s with tor exit node at Romania..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at Germany
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{de}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "6. Connecting to %s with tor exit node at Germany..." %url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at USA
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{us}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "7. Connecting to %s with tor exit node at USA..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at Japan
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{jp}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "8. Connecting to %s with tor exit node at Japan..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at Hong Kong
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{hk}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "9. Connecting to %s with tor exit node at Hong Kong..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

# Start tor instance with exit node at Singapore
term.format("Starting Tor:\n", term.Attr.BOLD)
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{sg}',
  },
  init_msg_handler = print_bootstrap_lines,
)
term.format("\nChecking our endpoint:\n", term.Attr.BOLD)

# Time the query with tor
print "10. Connecting to %s with tor exit node at Singapore..." % url
start_time = time.time()
term.format(query(), term.Color.BLUE)
end_time = time.time()
print "Spent %s seconds" % (end_time - start_time)

# Stop tor instance
tor_process.kill()

