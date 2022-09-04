# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, x_coord, y_coord, field, state, speed):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.field = field
        self.state = state
        self.speed = speed

    def move(self, direction):

        self.speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y_coord=self.y_coord + self.speed, x_coord=self.x_coord)
        elif direction == 'DOWN':
            self.field.set_unit(y_coord=self.y_coord - self.speed, x_coord=self.x_coord)
        elif direction == 'LEFT':
            self.field.set_unit(y_coord=self.y_coord, x_coord=self.x_coord - self.speed)
        elif direction == 'RIGTH':
            self.field.set_unit(y_coord=self.y_coord, x_coord=self.x_coord + self.speed)

    def _get_speed(self):

        if self.state == 'fly':
            return self.speed * 0.5
        elif self.state == 'crawl':
            return self.speed * 1.5
        else:
            raise ValueError('У Вас явные проблемы с самоопределением')
