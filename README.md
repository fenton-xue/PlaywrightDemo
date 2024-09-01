### Pytest.ini ###

#### addopts: 参数 ####
- --headed
    > 有头模式
- --slowmo=2_000
    > 每个操作直接间隔2s
- --output=test_res
    > 指定输出路径，和--video配合使用
- --video=on
    > 出现test-results/*/video.webm文件，有一个录像
- --screenshot=on
    > 可以调整成只在失败的时候截图
- --base-url=http://www.自动化测试.com
    > 此时page.goto("/demo/button")，就能够直接进入了

### Playwright ###
#### 命令 ####
- playwright codegen https://www.baidu.com
    > 开启录制
- playwright open https://www.baidu.com
    > 这种方式一开始不会进入录制，可以手动进入record

#### Method ####
- .click()
  - button="right" 
    > 右键点击
  - click_count=3
    > 点击次数
  - delay=1_000
    > 鼠标按下到松开的时间
  - timeout=3_000
    > 默认是30s
  - force=True
    > playwright在执行操作前有Auto-waiting的功能，如果force=True则不进行这些检查，直接执行
  - trial=True
    > 与force相反，值为True时只会等待那些auto-waiting，可以当作等待使用
  - modifiers=["Control", "..."]
    > 点击时按住Ctrl，可以继续加新的参数
  - position={"x": 15, "y": 20}
    > 这里的x和y可以参见下面的bounding_box()，如果输入的x和y的值，比元素的x，y要大，会点不到<br>但是它是div的宽度，如果输入的x和真实的x比较接近的话，也有可能能够点到
  - no_wait_after=True
    > 如果点击事件后出现了阻断性的弹出，此时可以令其为True，避免click的动作一直没有结束而失败

- page.locator("xxx").bounding_box()
  > 求xxx元素的大小，x、y、width、height、\_\_len__, x和y是在页面的绝对位置

#### 小技巧 ####
- Alt + P
  > 看方法入参
