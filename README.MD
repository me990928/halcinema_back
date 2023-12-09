# BACKEND START SETUP!!

### スクリプトによる起動
```bash
bash run.sh
```

### 手動で起動
```bash
# cd root/src/app
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# cd root/images
python3 main.py
```