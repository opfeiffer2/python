class Television:
    """
    A class representing the functions of a tv remote on a television.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to set default values of television
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to change power setting of television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to change mute setting of television.
        """
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self)-> None:
        """
        Method to increase channel number
        If maximum channel is reached, it will cycle back to the minimum channel.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self)-> None:
        """
        Method to decrease channel number
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self)-> None:
        """
        Method to increase television volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self)-> None:
        """
        Method to decrease television volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self)-> str:
        """
        Method to show television settings.
        :return: Television settings
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

