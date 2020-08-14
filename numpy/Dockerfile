FROM centos
RUN yum install python36 -y
RUN yum install wget -y
RUN yum install curl -y
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN yum install epel-release -y
RUN python3 get-pip.py
RUN pip install pillow
RUN pip install seaborn
RUN pip install opencv-python
RUN pip install pandas
RUN pip install numpy
RUN pip install scikit-learn
RUN pip install matplotlib
CMD /bin/bash
