from flask import Flask, send_from_directory, render_template
from multiprocessing import Process
import os

app = Flask(__name__)

@app.route("/live.m3u8")
def api():
	return send_from_directory("hls", filename="live.m3u8")

@app.route("/live<num>.ts")
def apiseg(num):
	fname = "live" + num + ".ts"
	return send_from_directory("hls", filename=fname)


@app.route("/view")
def view():
	return render_template("view.html")

def encode():
	os.system("sudo bash encode.sh")

if "__main__" in __name__:
	p = Process(target=encode)
	p.start()
	app.run(host="0.0.0.0", port=80)
	p.stop()
