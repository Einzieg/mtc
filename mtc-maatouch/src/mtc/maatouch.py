import os.path
import socket

from adbutils import adb
from loguru import logger
from mtc.touch import Touch
from mtc.utils import CommandBuilder, str2byte


class MaaTouch(Touch):
    """
    Control method that implements the same as scrcpy and has an interface similar to minitouch.
    https://github.com/MaaAssistantArknights/MaaTouch
    """

    max_x: int
    max_y: int
    _maatouch_stream = socket.socket
    _maatouch_stream_storage = None

    MAATOUCH_FILEPATH_REMOTE = "/data/local/tmp/maatouch"
    MAATOUCH_FILEPATH_LOCAL = f"{os.path.dirname(__file__)}/bin/maatouch"
    DEFAULT_BUFFER_SIZE = 0

    def __init__(self, serial):
        self.__adb = adb.device(serial)
        logger.debug("MaaTouch install")
        self.__adb.push(self.MAATOUCH_FILEPATH_LOCAL, self.MAATOUCH_FILEPATH_REMOTE)
        logger.info("MaaTouch init")

        # CLASSPATH=/data/local/tmp/maatouch app_process / com.shxyke.MaaTouch.App
        stream = self.__adb.shell(
            [
                "CLASSPATH=/data/local/tmp/maatouch",
                "app_process",
                "/",
                "com.shxyke.MaaTouch.App",
            ],
            stream=True,
        )
        # Prevent shell stream from being deleted causing socket close
        self._maatouch_stream_storage = stream
        stream = stream.conn
        stream.settimeout(10)
        self._maatouch_stream = stream

        # get minitouch server info
        socket_out = stream.makefile()

        # v <version>
        # protocol version, usually it is 1. needn't use this
        # ^ <max-contacts> <max-x> <max-y> <max-pressure>
        _, max_contacts, max_x, max_y, max_pressure, *_ = (
            socket_out.readline().replace("\n", "").replace("\r", "").split(" ")
        )
        self.max_contacts = max_contacts
        self.max_x = max_x
        self.max_y = max_y
        self.max_pressure = max_pressure
        logger.info(
            "max_contact: {}; max_x: {}; max_y: {}; max_pressure: {}".format(
                max_contacts, max_x, max_y, max_pressure
            )
        )

    def send(self, content):
        """send message and get its response"""
        byte_content = str2byte(content)
        self._maatouch_stream.sendall(byte_content)
        return self._maatouch_stream.recv(self.DEFAULT_BUFFER_SIZE)

    async def __tap(self, points, pressure=100, duration=None, no_up=None):
        """
        tap on screen, with pressure/duration

        :param points: list, looks like [(x1, y1), (x2, y2)]
        :param pressure: default == 100
        :param duration:
        :param no_up: if true, do not append 'up' at the end
        :return:
        """
        points = [list(map(int, each_point)) for each_point in points]

        _builder = CommandBuilder()
        for point_id, each_point in enumerate(points):
            x, y = each_point
            _builder.down(point_id, x, y, pressure)
        _builder.commit()

        # apply duration
        if duration:
            _builder.wait(duration)
            _builder.commit()

        # need release?
        if not no_up:
            for each_id in range(len(points)):
                _builder.up(each_id)

        await _builder.publish(self)

    async def __swipe(self, points, pressure=100, duration=None, no_down=None, no_up=None):
        """
        swipe between points, one by one

        :param points: [(400, 500), (500, 500)]
        :param pressure: default == 100
        :param duration:
        :param no_down: will not 'down' at the beginning
        :param no_up: will not 'up' at the end
        :return:
        """
        points = [list(map(int, each_point)) for each_point in points]

        _builder = CommandBuilder()
        point_id = 0

        # tap the first point
        if not no_down:
            x, y = points.pop(0)
            _builder.down(point_id, x, y, pressure)
            await _builder.publish(self)

        # start swiping
        for each_point in points:
            x, y = each_point
            _builder.move(point_id, x, y, pressure)

            # add delay between points
            if duration:
                _builder.wait(duration)
            _builder.commit()

        await _builder.publish(self)

        # release
        if not no_up:
            _builder.up(point_id)
            await _builder.publish(self)

    async def __pinch(self, start1, start2, end1, end2, duration: int = 300, pressure: int = 100):
        # start1 = self.__convert(*start1)
        # start2 = self.__convert(*start2)
        # end1 = self.__convert(*end1)
        # end2 = self.__convert(*end2)

        steps = 10
        step_duration = duration // steps

        x1s = [start1[0] + (end1[0] - start1[0]) * i / steps for i in range(steps + 1)]
        y1s = [start1[1] + (end1[1] - start1[1]) * i / steps for i in range(steps + 1)]
        x2s = [start2[0] + (end2[0] - start2[0]) * i / steps for i in range(steps + 1)]
        y2s = [start2[1] + (end2[1] - start2[1]) * i / steps for i in range(steps + 1)]

        _builder = CommandBuilder()

        # 两指按下
        _builder.down(0, int(x1s[0]), int(y1s[0]), pressure)
        _builder.down(1, int(x2s[0]), int(y2s[0]), pressure)
        _builder.commit()
        await _builder.publish(self)

        # 移动
        for i in range(1, steps + 1):
            _builder.move(0, int(x1s[i]), int(y1s[i]), pressure)
            _builder.move(1, int(x2s[i]), int(y2s[i]), pressure)
            _builder.wait(step_duration)
            _builder.commit()
            await _builder.publish(self)

        # 抬起
        _builder.up(0)
        _builder.up(1)
        _builder.commit()
        await _builder.publish(self)

    async def pinch(self, start1, start2, end1, end2, duration: int = 300, pressure: int = 100):
        return await self.__pinch(start1, start2, end1, end2, duration, pressure)

    async def click(self, x: int, y: int, duration: int = 100):
        return await self.__tap([(x, y)], duration=duration)

    async def swipe(self, points: list, duration: int = 500):
        return await self.__swipe(points, duration=duration / len(points))


if __name__ == "__main__":
    touch = MaaTouch("127.0.0.1:16384")
    touch.click(100, 100, 10000)
