FROM centos
RUN yum install python36 -y
RUN yum install wget -y
RUN yum install curl -y
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN yum install epel-release -y
RUN python3 get-pip.py
RUN pip install pillow
RUN pip install numpy==1.18.1
RUN pip install seaborn
RUN pip uninstall opencv-python
RUN pip install opencv-contrib-python==3.3.0.9
RUN pip install tensorflow
RUN pip install pandas
RUN pip install keras
RUN pip install matplotlib
CMD mkdir /mnt
CMD /bin/bash
