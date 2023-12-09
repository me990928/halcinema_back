pid_8000=$(lsof -ti :8000)

if [ -n "$pid_8000" ]; then
    for pid in $pid_8000
    do
        kill -9 $pid
        echo "killed $pid"
    done
else
    echo "no process on port 8000"
fi

pid_8005=$(lsof -ti :8005)

if [ -n "$pid_8005" ]; then
    for pid in $pid_8005
    do
        kill -9 $pid
        echo "killed $pid"
    done
else
    echo "no process on port 8005"
fi