FROM atmoz/sftp

RUN mkdir -p /home/enmuser/data/Store/Deliverables/
VOLUME /home/enmuser/data/Store/Deliverables/
ADD CASFiles/* /home/enmuser/data/Store/Deliverables/

ADD keys/sftp_key.pub /home/enmuser/.ssh/keys/sftp_key.pub
CMD ["enmuser::"]


