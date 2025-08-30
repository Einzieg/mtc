from abc import ABC, abstractmethod
from typing import List, Tuple


class Touch(ABC):
    @abstractmethod
    async def click(self, x: int, y: int, duration: int = 100):
        """
        点击某个坐标点
        :param x: x
        :param y: y
        :param duration: 持续时间. Defaults to 100ms
        :return:
        """

    @abstractmethod
    async def swipe(self, points: List[Tuple[int, int]], duration: int = 500):
        """
        模拟手势(滑动)
        :param points: list[Point(x,y)] 坐标点列表
        :param duration: 持续时间. Defaults to 500ms
        :return:
        """

    @abstractmethod
    async def pinch(self, start1, start2, end1, end2, duration: int = 300, pressure: int = 100):
        """
        模拟手势(缩放)
        :param start1: 缩放起点1
        :param start2: 缩放起点2
        :param end1: 缩放终点1
        :param end2: 缩放终点2
        :param duration: 持续时间. Defaults to 300ms
        :param pressure: 压力. Defaults to 100
        :return:
        """
