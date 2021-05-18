# rosdoc_lite

`rosdoc_lite`はドキュメント自動生成ツールであり，デフォルトではDoxygenベースになっている．  
DoxygenはMarkDown形式で記述でき，数式もMathJaxの形式で出力することができる．  
しかし，数式を出力するためにはtex関連のツールが揃っている必要がある．  
ここでは，`rosdoc_lite`とtex関連のツールがインストールされた docker image を用いて，簡単にドキュメント自動生成ができるようにする．

ファイルを共有した状態でコンテナを開く．
```
cd <ros_project_path_on_host>
docker run -it --rm -v "$(pwd)/<ros_project_path_on_host>:/<ros_project_path_on_docker>" --workdir="/<ros_project_path_on_docker>" <rosdoc_lite_image> 
```

コンテナの起動と同時にコマンドの実行
```
docker run --rm -v "$(pwd)/<ros_project_path_on_host>:/<ros_project_path_on_docker>" <rosdoc_lite_image> rosdoc_lite .
```


以下のコマンドで`Dockerfile`をimageにしたものをダウンロードできる
```
docker pull tomson784/rosdoc-lite:latest
```

