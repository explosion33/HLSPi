sudo mkdir /dev/shm/hls
sudo cp hls.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo system ctl enable hls.service
