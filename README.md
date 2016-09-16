
Place files so the structure looks like 
 * /root/sites/site1
 * /root/sites/site2
 * /root/sites/lb

Install nginx and stop the default instance (blocks port 80)
* nginx -s stop

Disable autostart for default nginx
* update-rc.d nginx disable

Load shortcuts
* . /root/sites/shortcuts

Use
* example_init (use if neccessary - creates symlinks)
* lb_start
* lb_reload
* w1_start
* w1_stop
* w2_start
* w2_stop
