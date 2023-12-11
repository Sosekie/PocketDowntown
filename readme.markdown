# Pocketdowntown

## Introduction
"Pocketdowntown is my favorite mobile game in elementary school. At that time, I thought: driving a cab is a tedious process, if only there was an algorithm to automate the driving of cabs. When I got to graduate school, I realized that it wasn't that hard to implement these functions, so I started to try it out.
This project also implements the auto-feed function.

## Method&Update
### 2023/11/18
1. use an app such as `Anlink` to project a cell phone screen onto a computer;
2. take the whole computer screenshot as input, judge whether there is a corresponding target image in the picture, get the position area of the corresponding image, and then input it to the `pyautogui` library to perform operations such as mouse clicking and pressing and releasing, in order to realize the auto-driving of the cab in the game;
3. Instead of judging the location the passenger is going to and the current location during the driving process, traverse all the buildings by stopping every time a small step is taken (a trip takes about a minute).
### 2023/11/19
1. change to get the phone screen location instead of the whole image as input, speed up a lot, a template lookup took about 0.28 seconds;
2. wrapped most of the functions to simplify the code;
3. add the judgment of whether the vehicle can continue to drive during the driving process, instead of waiting for the end of a fixed period of time to stop clicking; the vehicle stopping time needs to satisfy 0.5 seconds before triggering the judgment of getting off the vehicle, and `0.5-last_time` can prevent the time wasted due to the judgment.
4. the relative position of the destination is obtained by the position of the cab, and the destination digital picture is obtained;
### 2023/11/20
1. passes through the top two-thirds of the mask picture to find any of the blue squares below and clicks on them;
2. look through the lower third of the mask image, and the left and right third of the area, to find if there is a store in the center area that needs to be stocked;
3. double-click to enter the store, look for the "stock" option, click and close the window. 4. loop until the store is traversed;
4. Loop until you have traversed all the actions you need to take.
### 4. Loop until you have traversed all the actions you need to take.
1. drag the screen to go through all the stores and find out if you need to restock yourself. 2. try to identify items that are sold out;
2. try to identify sold out items but fail, instead click on them one by one to see if they can be restocked. 3. change to a binary lookup to see if they can be restocked;
3. change to a bisection lookup, where each loop determines if it's left-to-right or vice versa, and only checks half the stores to shorten the time.
### 2023/11/21
1. "and a third of the area to the left and a third of the area to the right" was changed to two-fifths of each, because my phone screen shows up to five stores, so I only need to keep the middle store.

## Pip list

```bash
pip install -r requirements.txt
```

## Run
Execute the following command in the root directory to start the script:
```bash
python main.py
```

! [Result](screen.png)

Chinese Version

# Pocketdowntown

## Introduction
“口袋商业街”是我小学时候非常喜欢的手机经营游戏。那时，我就在想：开出租车过程很繁琐，如果有算法可以实现出租车的自动驾驶就好了。到了研究生阶段，我发现实现这些功能其实并不难，于是我开始动手尝试。
此项目还实现了自动进货功能。

## Method&Update
### 2023/11/18
1. 使用`Anlink`等应用将手机画面投影到电脑上；
2. 将整张电脑截图作为输入，判断图片中有无对应目标图像，获取对应图像的位置区域，然后输入给`pyautogui`库进行鼠标点击和按下放开等操作，来实现对游戏中出租车的自动驾驶；
3. 驾驶过程中不对乘客要去的地点和当前地点进行判断，而采用每次移动一小步就停下的方式，对所有楼房进行遍历（一趟大概花费一分钟）。
### 2023/11/19
1. 改为获取手机画面位置以取代整张图片作为输入，速度提升很多，一次template查找耗时大约0.28秒；
2. 封装了大部分函数，简化代码；
3. 在行驶过程中增加是否还可以继续行驶的判断，而不是等待固定时间结束才停止点击；车辆停止时间需满足0.5秒才可触发下车判断，`0.5-last_time`可防止因判断而导致的时间浪费;
4. 通过出租车的位置获得了目的地的相对位置，得到目的地数字图片；
### 2023/11/20
1. 通过mask图片上方三分之二部分来查找下方任意一个蓝色方块并点击；
2. 通过mask图片下方三分之一部分，以及左右各三分之一部分区域，来查找中间区域有无需要进货的商店；
3. 两次点击进入商店，查找有无“进货”选项，点击并关闭窗口；
4. 循环执行直到遍历完所有需要进行的操作。
### 2023/11/20
1. 拖动屏幕来遍历所有商店，查找是否需要自行补货；
2. 尝试识别售空的商品，但是失败，改用逐个点击查看是否可以进货；
3. 改为二分查找，每个循环判断是从左到右还是相反，只检查一半的商店，以缩短时间。
### 2023/11/21
1. “以及左右各三分之一部分区域”改为各五分之二，因为我的手机屏幕最多显示五个商店，所以只需要保留中间的商店即可。

## Pip list

```bash
pip install -r requirements.txt
```

## Run
在根目录中执行以下命令来启动脚本：
```bash
python main.py
```

![Result](screen.png)
