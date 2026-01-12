# Garage Door Opener

For this project, I removed the button from my garage door clicker and soldered a MOSFET in its place. The gate was connected to a GPIO pin on a Raspberry Pi, which hosted a Flask server. The server serves a webpage that takes a password. If the user enters the correcct password, the garage door opens. There is also a Flask App that serves the same interface for Android phones.
