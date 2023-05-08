#!/bin/sh
pkg install -y python py39-pip py39-matplotlib
pip install -r ../requirements.txt

cat > /usr/local/sbin/attendance << EOF
#!/bin/sh
#
# PROVIDE: attendance
# REQUIRE: DAEMON
# KEYWORD: shutdown

. /etc/rc.subr

name=attendance
rcvar=attendance_enable

command="/usr/local/sbin/attendance"

load_rc_config $name

#
# DO NOT CHANGE THESE DEFAULT VALUES HERE
# SET THEM IN THE /etc/rc.conf FILE
#
attendance_enable=${attendance_enable-"NO"}
pidfile=${attendance_pidfile-"/var/run/attendance.pid"}

run_rc_command "$1"
EOF

chmod +x /usr/local/sbin/attendance
service attendance start
