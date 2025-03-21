# NetworkSecurityML

## This is my Network security project for Phising Data

![image](https://github.com/user-attachments/assets/ed8ecaa3-ca88-49cd-a8d8-a309ef69eb3d)

![image](https://github.com/user-attachments/assets/b67fec99-6830-4f93-bb34-b78501d4a387)

![image](https://github.com/user-attachments/assets/281e2368-c958-4686-a823-8273e58762f3)

![image](https://github.com/user-attachments/assets/5461a5e1-2c25-4b5a-baa3-ad9a17b58c0f)

![image](https://github.com/user-attachments/assets/1d5bf9a2-2bdb-4727-a69c-b016b6209730)

![image](https://github.com/user-attachments/assets/4b65f0b9-7682-4830-9092-abc9298660e0)

![image](https://github.com/user-attachments/assets/435b1999-f7de-4ae5-88e2-94d6865f53d0)


Initial Setup
To create env:
```
conda create -p venv python==3.10 -y
```
```
conda activate venv\
```
```
pip install -r requirements.txt
```
```
python app.py
```
Docker Setup In EC2 commands to be Executed

### Optional
```
sudo apt-get update -y
```
```
sudo apt-get upgrade
```
### Required
```
curl -fsSL https://get.docker.com -o get-docker.sh
```
```
sudo sh get-docker.sh
```
```
sudo usermod -aG docker ubuntu
```
```
newgrp docker
```

### Create a runner from settings->actions->runners and follow the prompts. enter 'self-hosted' as runnner name when prompted.
### Add a in-bound rules from network settings in instance, selecting port as 8080 and custom ip.
