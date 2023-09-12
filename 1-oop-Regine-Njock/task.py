class TV:
    def __init__(self, channel, volume_level, turned_on=False):
        """The constructor. Called when you instantiate a TV."""
        self.channel = channel
        self.volume_level = volume_level
        self.turned_on = turned_on
    
    def checkRange(self, new_channel_num: int, end_of_range=101) -> bool:
        temp = self.channel + new_channel_num
        return temp in range(1, end_of_range)

    def checkRangeVol(self, new_volume_num: int, end_of_range: int=11) -> bool:
        temp = self.volume_level + new_volume_num
        return temp in range(1, end_of_range)

    def turn_on(self):
        """Turns the TV on."""
        self.turned_on = True

    def turn_off(self):
        """Turns the TV off."""
        self.turned_on = False

    def channel_up(self):
        """Scrolls the channel up."""
        if self.turned_on and self.checkRange(1):
            self.channel = 1 + self.channel
        else:
            print('Turned off or out of range')

    def channel_down(self):
        """Scrolls the channel down."""
        if self.turned_on and self.checkRange(-1):
            self.channel -= 1
        else:
            print('Turned off or out of range')

    def set_channel(self, new_channel: int):
        """
        Sets the channel to the desired channel.

        :param int new_channel: The new channel
        """
        if self.turned_on and self.checkRange(new_channel - self.channel):
            self.channel = new_channel
        else:
            print('Turned off or out of range')

    def volume_up(self):
        """Increases the volume."""
        if self.turned_on and self.checkRangeVol(1):
            self.volume_level += 1
        else:
            print('Turned off or out of range')

    def volume_down(self):
        """Decreases the volume."""
        if self.turned_on and self.checkRangeVol(-1):
            self.volume_level -= 1
        else:
            print('Turned off or out of range')

    def is_on(self):
        """Returns 'on' when the TV is on and otherwise 'off'."""
        if self.turned_on:
            return "on"
        return "off"

tv_obj = TV(1, 10)
tv_obj2 = TV(2,2)
print('My two object are distinct and have different memory addresses', tv_obj, tv_obj2)
print('channel of tv1:', tv_obj.channel)
print('volume_level of tv1',tv_obj.volume_level)
print('turned_on tv1:',tv_obj.turned_on)

#####turning on and off my tv_obj on
tv_obj.turn_on()   # here I changed the turned_on boolean to true
print('Turn on:',tv_obj.turned_on)
tv_obj.turn_off()   # here I changed the turned_on boolean to true
print('Turn off:', tv_obj.turned_on)

### channel_up and channel_down

tv_obj.turn_on()
# tv_obj.channel_up()
# tv_obj.channel_up()
# tv_obj.channel_down()


#### set channel

# tv_obj.channel_up()
# tv_obj.set_channel(1)
# print(tv_obj.channel)
# tv_obj.channel_down()
# print('Result',tv_obj.channel)

## change volume

# tv_obj.volume_down()
# tv_obj.volume_down()
# tv_obj.volume_down()
tv_obj.volume_down()
# tv_obj.volume_up()

# print('tv1:', tv_obj.turned_on, tv_obj.channel, tv_obj.volume_level)
# print('tv2:', tv_obj2.turned_on, tv_obj2.channel, tv_obj2.volume_level)