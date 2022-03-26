ffmpeg -y \
    -input_format h264 -i /dev/video0 \
    -c:v copy \
    -f hls \
    -hls_time 1 \
    -hls_list_size 30 \
    -hls_flags delete_segments \
    /dev/shm/hls/live.m3u8
