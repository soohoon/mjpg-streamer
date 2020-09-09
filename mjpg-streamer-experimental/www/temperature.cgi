#!/bin/bash
echo HTTP/1.0 200 OK
echo Content-type: text/html
echo Connection: close
echo Server: MJPG-Streamer/0.2
echo Cache-Control: no-store, no-cache, must-revalidate, pre-check=0, post-check=0, max-age=0
echo Pragma: no-cache
echo Expires: Mon, 3 Jan 2000 12:34:56 GMT
echo
echo
echo -n "{cluNodeStat::"
echo "<pre>"
/opt/vc/bin/vcgencmd measure_temp
if ps ax | grep -v grep | grep socat > /dev/null; then
	echo Bluetooth Connected
else
	echo Bluetooth Not Connected
fi
DEV=`hcitool con | awk '/ACL/{print $3}'`
if [ ! -z "$DEV" ]; then
	hcitool tpl $DEV
	hcitool rssi $DEV
fi
if [ -f /tmp/discover ]; then
	bluetoothctl show
fi
echo
echo "</pre>"
echo "}"
