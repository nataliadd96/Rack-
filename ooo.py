from gpiozero import LED,PingServer
from gpiozero.tools import negated
from signal import pause

green = LED(19)
red = LED(26)

google = PingServer('google.com')

green.source = google
green.source_delay = 20
red.source = negated(green)

pause()