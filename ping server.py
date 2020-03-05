from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause

green = LED(5)
red = LED(5)
green = LED(4)
red = LED(6)

google = PingServer('google.com')

green.source = google
green.source_delay = 20
red.source = negated(green)

pause()