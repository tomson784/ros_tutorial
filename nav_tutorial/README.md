# ROSのナビゲーションチュートリアル

roswikiの[navigation](http://wiki.ros.org/navigation)に準拠した内容を行う．  
現在はtfよりtf2が推奨されているが，ここではtfで行う．

1. Configuring and Using the Navigation Stack
    1. Setting up your robot using tf (robot_setup_tf)


## memo

> まず始めに、tfには大きく分けて二つのクラスがあります．  
> 一つ目は座標系の登録を行う、Broadcaster  
> 二つ目は登録された座標系を使用して座標変換などを行えるListenterです．  

https://myenigma.hatenablog.com/entry/20130210/1360491625 より引用