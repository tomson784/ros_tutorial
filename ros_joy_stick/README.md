# ros joy stick

ホストPCにPS4を接続する．Bluetoothであればそのためのドライバが必要なので，以下のコマンドでインストールする．

```
# apt install -y bluez
apt install -y python-pip
pip install ds4drv
```

接続後`/dev/input/js*`を確認する．  
その後，以下のコマンドを実行してrosのjoy_nodeを実行することができた．  
以下のコマンドのうちのどれが必須なのか確認していないので，今度試す．

```
docker run \
-it \
--net=host \
--privileged \
--device=/dev/ttyACM0:/dev/ttyACM0:rwm \
--device=/dev/input/:/dev/input/:rwm \
--rm \
ros:melodic \
/bin/bash
```

デバイスに対する権限などは[このリンク](http://docs.docker.jp/v1.10/engine/reference/run.html#linux-lxc)を要参照
