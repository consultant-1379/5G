x=$(docker ps | grep atmoz/sftp | head -n 2 | tail -1 | awk {'print $1'}); docker kill $x;

docker run \
    -v $(pwd)/keys/sftp_key.pub:/home/enmuser/.ssh/keys/sftp_key.pub:ro \
    -v $(pwd)/keys/sftp_key:/home/enmuser/.ssh/keys/sftp_key:ro \
    -v $(pwd)/CASFiles:/home/enmuser/data/Store/Deliverables \
    -p 2222:22 --ulimit nofile=90000:90000 -d atmoz/sftp enmuser::