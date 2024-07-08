# TODO
- [ ] 修改后台界面，实现类似旺店通那样点击原始订单可以查看货品列表的功能
- [ ] CD
- [ ] 更换一个功能丰富一些的 Python 镜像，至少可以使用 nano, vi 等编辑器

# 基本操作
复制 .env.example 文件，并修改相应环境变量的值
```
cp .env.example .env
```
构建并启动容器
```
docker compose up --build
```
Django
```
docker exec -ti peidi-django /bin/bash
```
MySQL
```
docker exec -ti peidi-mysql mysql -uroot -p
```
Redis
```
docker exec -ti peidi-redis redis-cli
```
停止并移除容器
```
docker compose down
```
清空数据库，MySQL 数据全部保存在`mysql/data`这个目录，删除这个目录相当于重置了 MySQL
```
sudo rm -rf ./mysql/data
```

# 环境变量
所有环境变量全部放入`.env`文件，修改`docker-compose.yml`文件，在 Django 部分添加相关环境变量，使用时通过```os.environ.get('NAME')```获取值

# 生产环境
1. 拉取最新代码
```
git pull
```
2. 如果修改了环境变量，则修改`.env`文件进行相应设置
3. 重启服务
```
docker compose down
docker compose up --build -d
```
