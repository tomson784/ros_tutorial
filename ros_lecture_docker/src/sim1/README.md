# メモ

# urdf(gazenp)
- inertial: 慣性モーメント
    - origin: 
    - mass: 
    - inertia: 
- collision: 衝突判定
    - origin: 
    - geometry: 
- gazebo: 
    - material: 色
    - mu1,mu2: 摩擦係数（mu1,mu2は基本的に同じもの）
    - 
- joint
    - dynamics 
        - damping: 軸のダンピングの係数(減衰係数)
- transmission
    - joint
        - hardwareInterface

# launch(gazebo)
- rosparam: ros_control用のパラメータ
    - pid: PIDゲイン

# キーボードで操作

- [ROS演習４-2020:トピック通信しよう！](https://demura.net/education/lecture/19641.html)

## 参考
- [ROS講座26 シミュレーターを作る](https://qiita.com/srs/items/f1a7c8abe577eaf3d0b9)
- [ROS講座27 gazeboでjointを動かす](https://qiita.com/srs/items/8868a8bef3752c3464a2)
- [ros_controls/ros_controllers の制御の仕組み (position/effort/velocity_controllers の基礎)](https://qiita.com/MoriKen/items/78b0ad8c1eae257646dd)
- [Gazebo + ROS で自分だけのロボットをつくる 1.完成までの手順](https://qiita.com/RyodoTanaka/items/c3014fd6d0f06d12814f)
