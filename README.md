# Xu Guanzhou's Website
* A personal website that to sharpen my "Full Stack" capabilities
* This website showcases some of my coding/design/engineering capabilities
* Built with an rotation of various technologies I've come across and wish to try
* More feature surely to come...

# About
This website contains the following:
* My resume
* A portfolio detailing some projects
* A blog containing my thoughts
* A way to contact me

# Front End
* Full refactor from Ruby(Jekyll) to Python(Pelican)
* I "handcraft" my own templates using CSS, HTML5, and Bootstrap
  * Thinking about rewriting the entire application in React? or Flask?
* The template inspiration I credit to a fellow computer scientist

# Hosting/Backend
* This website is now hosted on an Amazon EC2 Container - modeled off of LAMP software architecture
* Originally hosted as a github.io page
* Potentially will migrate this onto a Amazon S3
  * Thinking about wrapping the whole application into a deployable DOCKER cluster
* HTTPD
  * /sbin/service httpd start
  * /sbin/service httpd stop

# Git Hook Methodology
* This needs to be re-enabled after the EC2 migration
  * Need to be able to deploy and edit this website from any remote internet location
  * Connection
    * Public: 3.82.170.186
	* Private: 172.31.95.201
  * Needs to be incorporated into a CICD pipeline

# Dev Notes (Testing)
* ```python3 -m pip install -r requirements.txt```
* ```pelican content -s pelicanconf.py -t ./themes/xuguanzhou/```
* ```pelican --listen```

# Deploy Notes
* ```rsync -avc --delete output/ /var/www/html```
