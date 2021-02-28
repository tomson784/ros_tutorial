# ROS入門

課題を交えてROSの使い方をべんきょうしてもらいます．  
気になったワードは逐一ググることをお勧めします．

## できるようになってほしいこと
- ROSの基本的なデータの受け渡しについての概要を理解し，実装できること
- ROSを使ったArduinoの制御
- ROSに流れてくるデータの保存

## やること

[ROS Wiki](http://wiki.ros.org/ROS/Tutorials) に準拠した内容で行います．  
ROSはOSのバージョンに合わせてインストールする必要があるので気をつけてください．  

今回の構成はいかのようにします．
| 項目 | 値 |
|:-:|:-:|
| 仮想環境 | VMware |
| OS | Ubuntu18.04 LTS |
| ROS Version | Melodic |


## PC上にROSを扱える仮想環境を構築

仮想環境については[このサイト](https://bcblog.sios.jp/what-is-virtualenvironment-vmware/)などを参照してください．


仮想環境の作り方は
[ROS講座54 VMWare上でROSを使う](https://qiita.com/srs/items/25efd45641c274bb8415)  
を参考にUbuntuの環境を作成してください．


## ROSをインストール

ROS Wiki は日本語ページも存在しますが，日本語版は古いものしか存在しないので，英語版を参照することをおすすめします．
- [日本語版](http://wiki.ros.org/ja/ROS/Tutorials)
- [英語版](http://wiki.ros.org/ROS/Tutorials)


ROSのインストールは[このサイト](http://wiki.ros.org/melodic/Installation/Ubuntu)に従って行います．

以下のコマンドを順番に実行して，ROSのインストールをしてください．  

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt update

sudo apt upgrade

sudo apt install ros-melodic-desktop-full

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

source ~/.bashrc

sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

sudo rosdep init

rosdep update

mkdir -p ~/catkin_ws/src

cd ~/catkin_ws && catkin_make

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

source ~/.bashrc
```

端末を開いて`roscore`ができることを確認してください．  
`roscore`が正常に動作すればROS環境の構築完了です．

<br>

こまったとき(ROSが正常に作動しない，再インストールしたいときなど)は以下のコマンドでROS関連のパッケージを削除することができます．
```
sudo apt-get purge ros-melodic-*
```

## その他
Dockerを用いればROSを試す環境を簡単に構築することができます．  
興味があれば以下のYoutubeを見てください．  
[ロボットシステム学第12回（Docker）](https://www.youtube.com/watch?v=Utvf4YmMJpk&list=PLbUh9y6MXvjdIB5A9uhrZVrhAaXc61Pzz&index=16)