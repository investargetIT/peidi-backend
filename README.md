# TODO
- [x] 运行 `docker compose up` 后，`peidi-django` 这个容器没有自动运行
- [ ] 安装 phpmyadmin

# 基本操作
复制 .env.example 文件，并修改相应环境变量的值
```
cp .env.example .env
```
创建并启动容器
```
docker compose up
```
如果需要运行 Django 相关命令，需要进入 Django 容器
```
docker exec -ti peidi-django /bin/bash
```
如果要运行 MySQL 相关命令，需要进入 MySQL 容器
```
docker exec -ti peidi-mysql /bin/bash
```
停止并移除容器
```
docker compose down
```
清空数据库，MySQL 数据全部保存在`mysql/data`这个目录，删除这个目录相当于重置了 MySQL
```
sudo rm -rf mysql/data
```

# 环境变量
所有环境变量全部放入`.env`文件，修改`docker-compose.yml`文件，在 Django 部分添加相关环境变量，使用时通过```os.environ.get('NAME')```获取值

# 生产环境
1. **本地**构建镜像
```
docker build -t movier/peidi-django ./djangoapi
```
2. 推送镜像
```
docker push movier/peidi-django
```
3. **服务器**拉取镜像
```
docker pull movier/peidi-django
```
4. 拉取最新代码（可选，如果修改了环境变量、docker compose 文件则**必须**拉取代码）
```
git pull
```
5. 重启服务
```
docker compose down
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
