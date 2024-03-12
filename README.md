# 基本操作
1. 创建并启动容器
```
docker compose up
```
2. 如果需要运行 migration 等操作，需要进入 Django 容器
```
docker exec -ti peidi-django /bin/bash
```
3. 停止并移除容器
```
docker compose down
```

# 环境变量
所有环境变量全部放入`.env`文件，修改`docker-compose.yml`文件，在 Django 部分添加相关环境变量，使用时通过```os.environ.get('NAME')```获取值

