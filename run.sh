trap "cd ..; sh kill_pro.sh; exit" SIGINT

cd ./src/app
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
cd ../../
cd ./images/
python3 main.py &

while true; do
    sleep 1
done