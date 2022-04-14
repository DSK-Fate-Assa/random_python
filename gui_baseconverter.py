import pandas
import kivy
from kivy.uix.widget import Widget
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics','resizable',0)
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import string
raw_data = {
    'Binary': ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'],
    'Octal' : ['0', '1', '2', '3', '4', '5', '6', '7', None, None, None, None, None, None, None, None],
    'Hexadecimal' : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
}

df = pandas.DataFrame(raw_data, columns = ['Binary', 'Octal', 'Hexadecimal'], index = range(16))
print(df)
#print(df.Binary.where(df.Octal == '7')[7])
#print(df.Binary[list(df.Octal.values).index('7')])
#print(dir(df))
print('\n')

def den(val, prod, n=20):
    if prod == 'Binary':
        if len(val.split('.')) == 1:
            return '{0:b}'.format(int(val))
        elif len(val.split('.')) == 2:
            one = val.split('.')[0]
            two = val.split('.')[1]
            st = ''
            st += '{0:b}'.format(int(one))
            s = []
            c = float('0.'+two)
            for i in range(len(two)*n):
                if c <1 and c>0:
                    c = c*2
                else:
                    c = (c-1)*2
                s.append(str(c).split('.')[0])
            st += ('.'+''.join(s))
            return st.split('-')[0]
        else:
            print('Invalid Number')
    elif prod == 'Hexadecimal':
        if len(val.split('.')) == 1:
            return '{0:X}'.format(int(val))
        elif len(val.split('.')) == 2:
            return bin(den(val, 'Binary', n=80), 'Hexadecimal')
        else:
            print('Invalid Number')
    elif prod == 'Octal':
        if len(val.split('.')) == 1:
            return '{0:o}'.format(int(val))
        elif len(val.split('.')) == 2:
            return bin(den(val, 'Binary', n=48), 'Octal').strip('0')
        else:
            print('Invalid Number')

    else:
        return val


def oct_to_bin(val):
    st = ''
    if len(val.split('.'))==1:
        for i in val:
            st += df.Binary[list(df.Octal.values).index(i)][1:]
    elif len(val.split('.'))==2:
        for i in val.split('.')[0]:
            st += df.Binary[list(df.Octal.values).index(i)][1:]
        st += '.'
        for i in val.split('.')[1]:
            st += df.Binary[list(df.Octal.values).index(i)][1:]
    else:
        print('Invalid number')
    return st

def hex_to_bin(val):
    st = ''
    if len(val.split('.'))==1:
        for i in val:
            st += df.Binary[list(df.Hexadecimal.values).index(i)]
    elif len(val.split('.'))==2:
        for i in val.split('.')[0]:
            st += df.Binary[list(df.Hexadecimal.values).index(i)]
        st += '.'
        for i in val.split('.')[1]:
            st += df.Binary[list(df.Hexadecimal.values).index(i)]
    else:
        print('Invalid Number')
    return st

def bin(val, prod):
    if len(val.split('.')) == 1:
        if prod == 'Hexadecimal':
            opstr = ('0'*(4-(len(val)%4))) + val
            spliced = [opstr[i:i+4] for i in range(0, len(opstr), 4)]
            st = ''
            for i in spliced:
                st += df.Hexadecimal[list(df.Binary.values).index(i)]
            return st
        elif prod == 'Octal':
            opstr = ('0'*(3-(len(val)%3))) + val
            spliced = [opstr[i:i+3] for i in range(0, len(opstr), 3)]
            st = ''
            for i in spliced:
                st += df.Octal[list(df.Binary.values).index('0'+i)]
            return st
        elif prod == 'Denary':
            st = 0
            for i in range(len(val)-1, -1, -1):
                st += int(val[len(val)-1-i]) * (2**i) 
            return str(st)
        else:
            return val
    elif len(val.split('.')) == 2:
        if prod == 'Hexadecimal':
            st = ''
            opstr = ('0'*(4-(len(val.split('.')[0])%4))) + val.split('.')[0]
            spliced = [opstr[i:i+4] for i in range(0, len(opstr), 4)]
            for i in spliced:
                st += df.Hexadecimal[list(df.Binary.values).index(i)]
            st += '.'
            opstr = (val.split('.')[1] + '0'*(4-(len(val.split('.')[1])%4))) 
            spliced = [opstr[i:i+4] for i in range(0, len(opstr), 4)]
            for i in spliced:
                st += df.Hexadecimal[list(df.Binary.values).index(i)]
            return st
        elif prod == 'Octal':
            st = ''
            opstr = ('0'*(3-(len(val.split('.')[0])%3))) + val.split('.')[0]
            spliced = [opstr[i:i+3] for i in range(0, len(opstr), 3)]
            for i in spliced:
                st += df.Octal[list(df.Binary.values).index('0'+i)]
            st += '.'
            opstr = (val.split('.')[1] + '0'*(3-(len(val.split('.')[1])%3))) 
            spliced = [opstr[i:i+3] for i in range(0, len(opstr), 3)]
            for i in spliced:
                st += df.Hexadecimal[list(df.Binary.values).index('0'+i)]
            return st
        elif prod == 'Denary':
            st = 0
            s = 0
            one = val.split('.')[0]
            two = val.split('.')[1]
            for i in range(len(one)-1, -1, -1):
                st += int(one[len(one)-1-i]) * (2**i) 
            for i in range(-1, -1*(len(two))-1, -1):
                s += int(two[-1*i-1]) * (2**i)
            st += s 
            return str(st)
        else:
            return val
    else:
        print('Invalid Number')
        return('')     


def run(to, fro, num):
    if num == '':
        return 'Output'
    else:
        if fro == 'Denary':
            if num.isnumeric() or (num.split('.')[0].isnumeric and num.split('.')[-1].isnumeric):
                fin = den(num, to)
            else:
                fin = 'Invalid input'
        elif fro == 'Octal':
            if (set(num).difference(set(string.octdigits)) == set()) or (set(num.split('.')[0]).difference(set(string.octdigits)) == set() and set(num.split('.')[-1]).difference(set(string.octdigits)) == set()):
                if to == 'Denary':
                    fin = bin(oct_to_bin(num), 'Denary')
                elif to == 'Binary':
                    fin = oct_to_bin(num)
                elif to == 'Hexadecimal':
                    fin = bin(oct_to_bin(num), 'Hexadecimal')
                else:
                    fin = num
            else:
                fin = 'Invalid Input'
        elif fro == 'Hexadecimal':
            if (set(num).difference(set(string.hexdigits)) == set()) or (set(num.split('.')[0]).difference(set(string.hexdigits)) == set() and set(num.split('.')[-1]).difference(set(string.hexdigits)) == set()):
                if to == 'Denary':
                    fin = bin(hex_to_bin(num.upper()), 'Denary')
                elif to == 'Binary':
                    fin = hex_to_bin(num.upper())
                elif to == 'Octal':
                    fin = bin(hex_to_bin(num.upper()), 'Octal')
                else:
                    fin = num
            else:
                fin = 'Invalid Input'
        elif fro == 'Binary':
            if ((num.split('.')[0].count('1')+ num.split('.')[0].count('0')) == len(num.split('.')[0])) and ((num.split('.')[-1].count('1')+ num.split('.')[-1].count('0')) == len(num.split('.')[-1])) :
                fin = bin(num, to)
            else:
                fin = 'Invalid input' 
        else:
            fin = 'Invalid Input'
        return fin
'''
def x():
    try:
        while True:
            run()
    except:
        print('Error, make sure inputted values are valid.')
        x()
x()
'''
#Window.minimum_height = 9*80
#Window.minimum_width  = 16*80
Window.size= (1280, 720)
Builder.load_string('''
#:import Factory kivy.factory.Factory
<myspinneroption@SpinnerOption>:
    background_normal : \'\'
    background_color: 235/255, 99/255, 2/255, 1
    font_size: 25
    font_name: \'fonts/nicko.ttf\'
    
<converter>:
    #output_type : output_type
    input_val : input_val
    #input_type: input_type
    FloatLayout:
        size: 1280, 720
        canvas:
            Rectangle:
                size: 1280, 720
                pos: self.pos
                source: \'images/binary_falling.jpeg\'
        Label:
            pos_hint: {\'x\': 0.2, \'y\':0.6}
            size_hint_x : None
            width : root.width*0.6
            size_hint_y: None
            height: root.height*(1/3)
            text : \'DrHakeshi\\\'''s Base \\nConverter\'
            halign: \'center\'
            valign : \'top\'
            color: 77/255,238/255,234/255, 1
            canvas.before:
                Color:
                    rgba: 176/255, 46/255, 7/255, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
            font_size: 50
            font_name: \'fonts/rust3.otf\'
        Label:
            pos_hint: {\'x\': 2/15, \'y\':0.4}
            size_hint_x : None
            width : root.width*(2/15)
            size_hint_y: None
            height: root.height*(0.1)
            text : \'From\'
            halign: \'center\'
            valign : \'top\'
            color: 77/255,238/255,234/255, 1
            canvas.before:
                Color:
                    rgba: 176/255, 46/255, 7/255, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
            font_size: 35
            font_name: \'fonts/nicko.ttf\'
        Spinner:
            id: input_type
            pos_hint: {\'x\': 4.2/15, \'y\':0.4}
            size_hint_x : None
            width : root.width*(3/15)
            size_hint_y: None
            height: root.height*(0.1)
            text : \'Select -/-\'
            values: [\'Denary\',\'Binary\',\'Hexadecimal\',\'Octal\']
            halign: \'center\'
            valign : \'top\'
            color: 27/255,232/255,0/255, 1
            background_normal: \'\'
            background_color: 176/255, 46/255, 7/255, 1
            font_size: 32
            font_name: \'fonts/nicko.ttf\'
            on_text: root.assign_inputtype(input_type.text)
            option_cls: Factory.get(\'myspinneroption\')
        Label:
            pos_hint: {\'x\': 8/16, \'y\':0.4}
            size_hint_x : None
            width : root.width*(1/15)
            size_hint_y: None
            height: root.height*(0.1)
            text : \'To\'
            halign: \'center\'
            valign : \'top\'
            color: 77/255,238/255,234/255, 1
            canvas.before:
                Color:
                    rgba: 176/255, 46/255, 7/255, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
            font_size: 35
            font_name: \'fonts/nicko.ttf\'
        Spinner:
            id: output_type
            pos_hint: {\'x\': 9.4/16, \'y\':0.4}
            size_hint_x : None
            width : root.width*(3/15)
            size_hint_y: None
            height: root.height*(0.1)
            text : \'Select -/-\'
            values: [\'Denary\',\'Binary\',\'Hexadecimal\',\'Octal\']
            halign: \'center\'
            valign : \'top\'
            color: 27/255,232/255,0/255, 1
            background_normal: \'\'
            background_color: 176/255, 46/255, 7/255, 1
            font_size: 32
            font_name: \'fonts/nicko.ttf\'
            on_text: root.assign_outputtype(output_type.text)
            option_cls: Factory.get(\'myspinneroption\')
        TextInput:
            id: input_val
            hint_text: \'Input\'
            pos_hint: {\'x\': 3/15, \'y\':0.1}
            size_hint_x : None
            width : root.width*(4/15)
            size_hint_y: None
            height: root.height*(0.2)
            write_tab: False
            multiline: True
            background_normal: \'\'
            background_color: 176/255, 46/255, 7/255, 1
            foreground_color: 1, 1, 1, 1
            font_size: 24  if self.text != '' else 75
            hint_font_size : 30
            cursor_color: self.foreground_color
            font_name: \'fonts/rust.otf\'
        Image:
            source: \'images/arrow.png\'
            pos_hint: {\'center_x\': 8/15, \'center_y\':0.2}
            size_hint_x: 1/15
        TextInput:
            id: output_val
            pos_hint: {\'x\': 9/15, \'y\':0.1}
            size_hint_x : None
            width : root.width*(4/15)
            size_hint_y: None
            height: root.height*(0.2)
            hint_text: \'Output\'
            text: str(root.output_val.val)
            #text : \'Output\' if root.input_val.text == None else root.input_val.runner()
            #halign: \'center\'
            #valign : \'top\'
            foreground_color: 77/255,238/255,234/255, 1
            
            background_color: 176/255, 46/255, 7/255, 1
            font_size: 75 if self.text in (\'\', \'Output\') else 24
            font_name: \'fonts/rust.otf\'

            
''')
class final(Widget):
    val = StringProperty()

class converter(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.outtie, 1.0/3.0)
    output_val = final()
    output_type = 'otype'
    input_type = 'itype'

    runners = 0
    def assign_inputtype(self, itype):
        converter.input_type = itype
    def assign_outputtype(self, otype):
        converter.output_type = otype
    def outtie(self, *args):
        try:
            input_val = self.ids.input_val.text
            self.output_val.val = run(converter.output_type, converter.input_type, input_val)
        except ValueError:
            self.output_val.val = 'Invalid Input'
        #self.runners += 1
        #print(converter.output_type, converter.input_type, input_val, end = ' ')
        #print(self.output_val.val, self.runners, run(converter.output_type, converter.input_type, input_val))

class themain(App):
    def build(self):
        return converter()

themain().run()