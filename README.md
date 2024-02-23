# image-FFT

## Introducion

|origin|canny|
|:--:|:--:|
|![origin](https://raw.githubusercontent.com/learner-lu/picbed/master/202203010339386.png)|![fft](https://raw.githubusercontent.com/learner-lu/picbed/master/202203010340775.png)|

|origin|fft|
|:--:|:--:|
|![origin](https://raw.githubusercontent.com/learner-lu/picbed/master/202203010333845.png)|![fft](https://raw.githubusercontent.com/learner-lu/picbed/master/202203010334621.png)|
|![origin](https://raw.githubusercontent.com/learner-lu/picbed/master/202203010337157.png)|![fft](https://raw.githubusercontent.com/learner-lu/picbed/master/202203010338099.png)|

## Requirements

### part1: This project

```shell
pip install -r requirements.txt
```

- opencv `pip install opencv-python`
- pyqt5 `pip install pyqt5`
- numpy `pip install numpy`
- pygame `pip install pygame`

### Vscode extenstion for opencv(cv2)

easier for you to write code with cv2

- Python (Microsoft)
- Python Extension Pack (Don Jayamanne)
- Pylance (Microsoft)

### part2: manim(不须)

找到了一篇比较详细的[安装说明](https://zhuanlan.zhihu.com/p/354130270),大部分跟着做就行,不过有小问题,我的踩坑记录在下面

- `conda install ffmpeg`
- dvisvgm 不能下最新版的,要下2.11低版本,[网址](https://github.com/mgieseki/dvisvgm/releases)往下找2.11
- 用miktex就行,tex太慢了
- 不要用git clone,,切一下分支,直接zip下载manim-cairo-backend(branch)

```python
python mainm.py /xxx/xxx.py
```

`mainm.py`为主程序入口,后面的py文件为当前文件,它会找到其中所有可运行类,输入数字标号生成视频,一些例子可以查看`\manim-cairo-backend\from_3b1b\active\diffyq\part2\fourier_series.py`

## Use

```python
python GUI.py
```

- 退出pygame画图按`Ese`正常退出画下一个图
- 可以更改`GUI.py-InteractiveWindow-loadPicture`中的路径为你自己文件夹的路径,方便每次搜索结果

## Referance

- [3b1b fft](https://www.bilibili.com/video/av19141078?from=search&seid=5255738869667352545&spm_id_from=333.337.0.0)
- [3b1b fft draw](https://www.bilibili.com/video/BV1vt411N7Ti/?spm_id_from=333.788.recommend_more_video.3)
- [转换成svg格式](https://zhuanlan.zhihu.com/p/398237689)
- [成熟的GitHub项目](https://github.com/ruanluyu/FourierCircleDrawing)
- [fft画图](https://github.com/VacantHusky/Fourier-2dLine-drawing)
- [SVG知识](https://zhuanlan.zhihu.com/p/96444730)
- [SVG知识](https://zhuanlan.zhihu.com/p/421624191)
- [浅显易懂傅里叶变换](https://blog.csdn.net/tMb8Z9Vdm66wH68VX1/article/details/123058897)
- [fft demo](https://www.jezzamon.com/fourier/zh-cn.html),这个真的强烈建议看
