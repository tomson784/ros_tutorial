# rosdoc_lite

`rosdoc_lite`はドキュメント自動生成ツールであり，デフォルトではDoxygenベースになっている．  
DoxygenはMarkDown形式で記述でき，数式もMathJaxの形式で出力することができる．  
しかし，数式を出力するためにはtex関連のツールが揃っている必要がある．  
ここでは，`rosdoc_lite`とtex関連のツールがインストールされた docker image を用いて，簡単にドキュメント自動生成ができるようにする．

ファイルを共有した状態でコンテナを開く
```
docker run -it --rm -v "$(pwd)/test:/home/test" rosdoc_test 
```

コンテナの起動と同時にコマンドの実行
```
docker run --rm -v "$(pwd)/test:/home/test" rosdoc_test rosdoc_lite /home/test
```

