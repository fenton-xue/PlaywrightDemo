### Pytest.ini ###

#### addopts: 参数 ####
- --headed
    > 有头模式
- --slowmo=2_000
    > 每个操作直接间隔2s
- --output=test_res
    > 指定输出路径，和--video配合使用
- video=on
    > 出现test-results/*/video.webm文件，有一个录像
- screenshot=on
    > 可以调整成只在失败的时候截图

### Playwright ###
#### 命令 ####
- playwright codegen https://www.baidu.com
    > 开启录制
- playwright open https://www.baidu.com
    > 这种方式一开始不会进入录制，可以手动进入record