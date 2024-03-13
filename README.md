# Refresh_wot_daily_tasks
用于自动刷新坦克世界的每日任务

1、安装依赖：
pip install pyautogui deps/opencv_python-3.3.0.10-cp36-cp36m-win_amd64.whl


python版本必须为3.6！

2、将期望的任务类型截图，保存为模版

3、执行run.py对当前任务进行截图，并于模版截图对比，不同就控制鼠标进行任务刷新动作。任务优先级为3>2>1。
