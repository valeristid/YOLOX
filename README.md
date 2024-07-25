Cоздаем докер-образ
docker build –no-cache -t my-yolox-app .

Запускаем
docker run -it --rm my-yolox-app
Команды для запуска
CMD ["python","yoloxp"]

Пример
python tools/demo.py image -f exps/default/yolox_tiny.py -c /home/valerist/YOLOX/yolox_tiny.pth --path /home/valerist/YOLOX/frame_100.jpg --conf 0.25 --nms 0.45 --tsize 640 --save_result --device cpu
