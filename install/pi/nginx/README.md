# NGINX howto

## Expose port 80 for nginx

```shell
$ sudo apt install nginx
```

- On the router, port-forward port 80 for certbot/letsencrypt
- port-forward 443 for web app
- port-forward 22 for ssh to pi

## Get certificate for nginx on Ubuntu

```shell
$ sudo apt search snapd
$ sudo apt install snapd
$ sudo snap install core; sudo snap refresh core
$ sudo apt  remove certbot
$ sudo snap install --classic certbot
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot
$ sudo certbot certonly --nginx
```
- then follow instructions for certbot utility


## Nginx config file for web app
- copy the file `golfapp` to `/etc/nginx/sites-available`
- symlink `/etc/nginx/sites-available/golfapp` to `/etc/nginx/sites-enabled/`
- remove `/etc/nginx/sites-enabled/default`


## Gunicorn
Install a production web server
```shell
$ pip install gunicorn # with python3 -- may need to install an upgraded version of python3
```
#### Add a system service for the webapp
Put the following in `/etc/systemd/system/golf-scoring-webapp.service`
```
[Unit]
Description=Gunicorn instance for a golf scoring webapp
After=network.target
[Service]
User=pi4
Group=www-data
WorkingDirectory=/home/pi4/project/golf-scoring
ExecStart=/home/pi4/.local/bin/gunicorn --log-level debug -b localhost:8000 scoringapp:app
Restart=always
[Install]
WantedBy=multi-user.target
```

#### Enable the service
```
$ sudo systemctl enable golf-scoring-webapp
```
